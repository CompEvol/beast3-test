import java.io.File;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import javafx.application.Platform;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.stage.Stage;
import beastfx.app.beauti.BeautiTabPane;
import beastfx.app.inputeditor.BeautiDoc;

/** Drives the real BEAUti window (headless): import, choose from combo boxes, save. */
public class Driver {
    static BeautiTabPane pane; static BeautiDoc doc;
    static final AtomicInteger errors = new AtomicInteger();

    static void fx(Callable<Void> c) throws Exception {
        CountDownLatch l = new CountDownLatch(1);
        Platform.runLater(() -> { try { c.call(); } catch (Throwable t) { errors.incrementAndGet(); System.out.println("DRIVER EXCEPTION"); t.printStackTrace(System.out); } l.countDown(); });
        if (!l.await(90, TimeUnit.SECONDS)) { System.out.println("DRIVER TIMEOUT on FX thread"); System.exit(3); }
        // let queued layout and listeners run
        for (int i = 0; i < 3; i++) { CountDownLatch l2 = new CountDownLatch(1); Platform.runLater(l2::countDown); l2.await(30, TimeUnit.SECONDS); Thread.sleep(150); }
    }
    static CountDownLatch pending;
    /** start something on the FX thread that may open a modal dialog; later steps answer it, then "await" */
    static void async(Callable<Void> c) throws Exception {
        pending = new CountDownLatch(1); final CountDownLatch mine = pending;
        Platform.runLater(() -> { try { c.call(); } catch (Throwable t) { errors.incrementAndGet(); System.out.println("DRIVER EXCEPTION"); t.printStackTrace(System.out); } mine.countDown(); });
        Thread.sleep(3000);
    }
    static List<ComboBox<?>> combos() {
        List<ComboBox<?>> r = new ArrayList<>();
        for (Node n : nodes(".combo-box")) if (n instanceof ComboBox<?> cb && cb.isVisible()) r.add(cb);
        Tab t = pane.getSelectionModel().getSelectedItem();
        if (t != null && t.getContent() != null) for (Node n : t.getContent().lookupAll(".combo-box")) if (n instanceof ComboBox<?> cb && !r.contains(cb)) r.add(cb);
        return r;
    }
    /** nodes matching a selector in every open window, dialogs first */
    static List<Node> nodes(String selector) {
        List<Node> r = new ArrayList<>();
        List<javafx.stage.Window> ws = new ArrayList<>(javafx.stage.Window.getWindows());
        Collections.reverse(ws);
        for (javafx.stage.Window w : ws) if (w.getScene() != null && w.getScene().getRoot() != null) r.addAll(w.getScene().getRoot().lookupAll(selector));
        return r;
    }
    static ButtonBase button(String key) {
        for (String sel : new String[]{".button", ".radio-button", ".check-box"})
            for (Node n : nodes(sel)) if (n instanceof ButtonBase b && b.isVisible() && (key.equals(b.getId()) || key.equals(b.getText()))) return b;
        return null;
    }
    public static void main(String[] a) throws Exception {
        beast.base.core.ProgramStatus.name = "BEAUti";
        System.setProperty("beast.is.junit.testing", "true");
        Thread.setDefaultUncaughtExceptionHandler((th, t) -> { errors.incrementAndGet(); System.out.println("DRIVER UNCAUGHT in " + th.getName()); t.printStackTrace(System.out); });
        CountDownLatch l = new CountDownLatch(1); Platform.startup(l::countDown); l.await();
        fx(() -> { Stage st = new Stage(); pane = BeautiTabPane.main2(new String[]{}, st); doc = pane.doc; st.show(); return null; });
        String out = null;
        for (int i = 0; i < a.length; i++) {
            final String s = a[i];
            System.out.println("DRIVER STEP " + s);
            if (s.equals("-out")) { out = a[++i]; }
            else if (s.equals("-template")) { final String f = a[++i]; fx(() -> { doc.loadNewTemplate(f); doc.beauti.refreshPanel(); return null; }); }
            else if (s.equals("-nex")) { final File f = new File(a[++i]); fx(() -> { doc.importNexus(f); doc.beauti.refreshPanel(); return null; }); }
            else if (s.startsWith("tab=")) { fx(() -> { String want = s.substring(4).replace(" ", ""); boolean ok = false;
                    for (Tab t : pane.getTabs()) if (want.equals(t.getId())) { pane.getSelectionModel().select(t); ok = true; }
                    if (!ok) { errors.incrementAndGet(); List<String> ids = new ArrayList<>(); for (Tab t : pane.getTabs()) ids.add(t.getId()); System.out.println("DRIVER NO TAB " + want + " in " + ids); }
                    doc.beauti.refreshPanel(); return null; }); }
            else if (s.equals("dump")) { fx(() -> { for (ComboBox<?> cb : combos()) System.out.println("  COMBO id=" + cb.getId() + " value=" + cb.getValue() + " items=" + cb.getItems()); return null; }); }
            else if (s.startsWith("pick=")) { String[] p = s.substring(5).split("\\|"); fx(() -> { boolean ok = false;
                    for (ComboBox<?> cb : combos()) { String v = String.valueOf(cb.getValue());
                        if (!(p[0].equals(cb.getId()) || p[0].equals(v))) continue;
                        for (int k = 0; k < cb.getItems().size(); k++) if (String.valueOf(cb.getItems().get(k)).equals(p[1])) { cb.getSelectionModel().select(k); ok = true; break; }
                        if (ok) break; }
                    if (!ok) { errors.incrementAndGet(); System.out.println("DRIVER COULD NOT PICK " + s); }
                    return null; });
                fx(() -> { doc.beauti.refreshPanel(); return null; }); }
            else if (s.equals("await")) { if (pending != null && !pending.await(90, TimeUnit.SECONDS)) { System.out.println("DRIVER TIMEOUT awaiting import"); System.exit(3); } fx(() -> { doc.beauti.refreshPanel(); return null; }); }
            else if (s.equals("providers")) { fx(() -> { for (Object o : doc.beautiConfig.alignmentProvider) System.out.println("  PROVIDER " + o + " (" + o.getClass().getName() + ")"); return null; }); }
            else if (s.equals("-provider")) { final String name = a[++i]; final String[] fs = a[++i].split(","); async(() -> {
                    beastfx.app.inputeditor.BeautiAlignmentProvider prov = null;
                    for (beastfx.app.inputeditor.BeautiAlignmentProvider o : doc.beautiConfig.alignmentProvider) if (o.getClass().getName().contains(name) || o.toString().contains(name)) prov = o;
                    if (prov == null) { errors.incrementAndGet(); System.out.println("DRIVER NO PROVIDER " + name); return null; }
                    File[] files = new File[fs.length]; for (int k = 0; k < fs.length; k++) files[k] = new File(fs[k]);
                    // the same steps as the File > Add ... menu action in BeautiTabPane
                    List<beast.base.core.BEASTInterface> objs = prov.getAlignments(doc, files);
                    System.out.println("  PROVIDER " + prov + " returned " + (objs == null ? "null" : objs.size() + " objects"));
                    if (objs != null) for (beast.base.core.BEASTInterface o : objs) if (o instanceof beast.base.evolution.alignment.Alignment al) BeautiDoc.createTaxonSet(al, doc);
                    doc.connectModel(); doc.fireDocHasChanged();
                    if (objs != null) for (beast.base.core.BEASTInterface o : objs) if (o instanceof beast.base.spec.evolution.tree.MRCAPrior m) doc.addMRCAPrior(m);
                    doc.beauti.refreshPanel(); return null; }); }
            else if (s.startsWith("click=") || s.startsWith("clicknowait=")) { final String key = s.substring(s.indexOf('=') + 1); final boolean wait = s.startsWith("click=");
                final ButtonBase[] b = new ButtonBase[1]; fx(() -> { b[0] = button(key); if (b[0] == null) { errors.incrementAndGet(); System.out.println("DRIVER NO BUTTON " + key); } return null; });
                if (b[0] != null) { if (wait) fx(() -> { b[0].fire(); return null; }); else { Platform.runLater(() -> b[0].fire()); Thread.sleep(2500); } } }
            else if (s.startsWith("text=")) { String[] p = s.substring(5).split("\\|", -1); fx(() -> { boolean ok = false;
                    for (Node n : nodes(".text-field")) if (n instanceof TextField tf && p[0].equals(tf.getId())) { tf.setText(p[1]); tf.fireEvent(new javafx.event.ActionEvent()); ok = true; break; }
                    if (!ok) { errors.incrementAndGet(); System.out.println("DRIVER NO TEXT FIELD " + p[0]); } return null; }); }
            else if (s.equals("windows")) { fx(() -> { for (javafx.stage.Window w : javafx.stage.Window.getWindows()) System.out.println("  WINDOW " + w.getClass().getSimpleName() + " showing=" + w.isShowing()); for (String sel : new String[]{".button", ".radio-button"}) for (Node n : nodes(sel)) if (n instanceof ButtonBase bb && bb.isVisible()) System.out.println("  BUTTON id=" + bb.getId() + " text=" + bb.getText()); return null; }); }
            else { System.out.println("DRIVER UNKNOWN STEP " + s); errors.incrementAndGet(); }
        }
        if (out != null) { final String o = out; fx(() -> { doc.save(new File(o)); return null; }); System.out.println("DRIVER SAVED " + o); }
        System.out.println("DRIVER DONE errors=" + errors.get());
        System.exit(errors.get() == 0 ? 0 : 2);
    }
}

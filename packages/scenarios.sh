# BEAUti scenarios, sourced by check_packages.sh. Each line starts a fresh BEAUti with all
# packages installed, carries out the steps, saves the XML and runs it in BEAST.
#
#   sc <name> <step> ...
#
# Steps (see Driver.java):
#   -nex FILE                  File > Import Alignment (the core importer)
#   -provider NAME FILE[,FILE] File > <a package's own importer>; NAME is part of its class
#                              name. It may open a dialog: answer it with click=, then "await"
#   -template FILE             File > Template
#   tab=NAME                   go to a tab (its name without spaces)
#   pick=COMBO|ITEM            choose ITEM in the combo box whose id or current value is COMBO
#   click=BUTTON               press a button, radio button or check box (by id or text)
#   clicknowait=BUTTON         press a button that opens a dialog; later steps fill it in
#   text=FIELD|VALUE           type into a text field (by id)
#   await                      wait for a -provider import to finish
#   dump, windows, providers   print the combo boxes / buttons / importers (for writing steps)
#
# $NEXUS is beast3's beast-base/examples/nexus, $PKG the folder with the package clones,
# $INSTALLED the folder with the unpacked package zips.

# --- core template with the packages installed --------------------------------------------
sc default        -nex $NEXUS/dna.nex
sc core-HKY       -nex $NEXUS/dna.nex tab=SiteModel "pick=substModelComboBox|HKY"
sc core-TN93      -nex $NEXUS/dna.nex tab=SiteModel "pick=substModelComboBox|TN93"
sc core-GTR       -nex $NEXUS/dna.nex tab=SiteModel "pick=substModelComboBox|GTR"

# --- bModelTest ----------------------------------------------------------------------------
sc bModelTest     -nex $NEXUS/dna.nex tab=SiteModel "pick=Gamma Site Model|BEAST Model Test"

# --- SSM -----------------------------------------------------------------------------------
for m in Standard_K80 Standard_HKY "Standard_Tr N" Standard_TVM Standard_SYM Standard_GTR; do
    sc "SSM-${m// /_}" -nex $NEXUS/dna.nex tab=SiteModel "pick=substModelComboBox|$m"
done

# --- ORC -----------------------------------------------------------------------------------
sc ORC            -nex $NEXUS/dna.nex tab=ClockModel "pick=Strict Clock|Optimised Relaxed Clock"

# --- SA ------------------------------------------------------------------------------------
sc SA-FBD         -nex $NEXUS/dna.nex tab=Priors "pick=TreeDistribution|Fossilized Birth Death Model"

# --- several packages in one analysis ------------------------------------------------------
sc bModelTest-ORC-FBD -nex $NEXUS/dna.nex \
    tab=SiteModel "pick=Gamma Site Model|BEAST Model Test" \
    tab=ClockModel "pick=Strict Clock|Optimised Relaxed Clock" \
    tab=Priors "pick=TreeDistribution|Fossilized Birth Death Model"

# --- MM: its importer asks whether to condition on variable characters ---------------------
MM=$PKG/morph-models/examples/nexus
for answer in Yes No; do
    sc MM-M3982-$answer    -provider BeautiMorphModelAlignmentProvider $MM/M3982.nex click=$answer await tab=SiteModel
    sc MM-penguins-$answer -nex $MM/penguins_dna.nex \
        -provider BeautiMorphModelAlignmentProvider $MM/penguins_morph.nex click=$answer await tab=SiteModel
done

# --- StarBeast3: its own template and importer, species from the Guess dialog --------------
sc StarBeast3     -template $INSTALLED/starbeast3/fxtemplates/StarBeast3.xml \
    -provider StarBeastAlignmentProvider3 $NEXUS/26.nex,$NEXUS/29.nex await \
    tab=TaxonSets clicknowait=Guess "click=split on character" "pick=splitCombo|2" "text=SplitChar2|_" click=OK \
    tab=SiteModel tab=GeneClockModel tab=SpeciesClockModel tab=Priors tab=MCMC

# Data files

- `anolis-start.newick`: a starting tree for C22 (BEAUti › Starting tree › Newick), because the
  shipped `examples/nexus/anolis.nex_phyml_tree.txt` is empty (0 bytes) in beast2 v2.7.7, v2.7.8
  and master, and in beast3 master. It is the last tree (state 3,000,000) of
  `beast3/log/C01-slide/rep1/C01-b3-slide-anolis.trees` in Dropbox: anolis.nex, JC69, strict clock
  1.0, Yule, so branch lengths are in substitutions per site. Its 29 taxa are those of anolis.nex.
  Use the same file in both versions.

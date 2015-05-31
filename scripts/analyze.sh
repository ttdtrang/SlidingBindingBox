preliminary_experiments=(WT H274Y N294S)
# write lowest energy conformation from largest cluster
for d in ${preliminary_experiments[@]};do
    cd autodock/$d
    OFILE=$d-100runs-BC.pdbqt
    pythonsh ../../scripts/write_largest_cluster_ligand_1.py -l $d-100runs.dlg -o $OFILE
    sed '1 i MODEL 1' $OFILE | sed '$ a ENDMDL' > tmp && mv tmp $OFILE
    cd ../../
done;

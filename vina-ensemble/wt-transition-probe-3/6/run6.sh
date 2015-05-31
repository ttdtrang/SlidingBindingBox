for f in `ls ../../../receptors/wt-ensemble/*.pdbqt`;do
    prefix=`basename $f .pdbqt`
    vina --config config6.txt --receptor $f --ligand ../../../ligands/osel.pdbqt --out $prefix.pdbqt --log $prefix.log --cpu 4
done

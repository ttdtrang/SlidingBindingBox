preliminary_experiments=(WT H274Y N294S)
#	# autodock
#	for d in ${preliminary_experiments[@]};do
#	    cd autodock/$d
#	
#	    #autogrid4 -p grid.gpf -l $d.glg
#	    autodock4 -p dock-200runs.dpf -l $d-200runs.dlg &
#	
#	    cd ../../
#	done;

# vina
for d in ${preliminary_experiments[@]};do
    cd vina/$d
    vina --config config.txt --out $d.pdbqt --log $d.log --exhaustiveness 16
    cd ../../
done;

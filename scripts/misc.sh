# backing up old results
# generate new dpf for 200 ga_run
dirs=(WT H274Y N294S)
for d in ${dirs[@]};do
    cd autodock/$d
    #mv $d.glg $d-100runs.glg
    #mv $d.dlg $d-100runs.dlg
    #sed s/ga_run\ 100/ga_run\ 200/ dock.dpf > dock-200runs.dpf 

    cd ../../
done;

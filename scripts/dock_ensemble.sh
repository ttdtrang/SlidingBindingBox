vina=vina # vina path
NCPU=4 # number of cpus for vina 
LIGAND='../../ligands/osel.pdbqt'
RECEPTOR_DIR='../../receptors/wt-ensemble'

#x_center=-2.08
y_center=79.43
z_center=114.68
# z_centers=(122.43 119.805 117.18 114.555 111.93 109.305 ) # wt
z_centers=(117.18 116.18 115.18 114.18) # wt-transition-probe-21
z_centers=(119.18 118.18 117.18 116.18 115.18 ) # wt-transition-probe-18
z_centers=(120.18 119.18 118.18 117.18 116.18 115.18 ) # wt-transition-probe-3
x_centers=(-4.81 -3.81 -2.81 -1.81 0.81 1.81) # wt-transition-probe-4
i=1
for ptn in ${x_centers[@]};do
    mkdir $i
    config_file=$i/config$i.txt
    touch $config_file
(cat << EOF
size_x =  10.5          
size_y =  10.5          
size_z =  10.5       
center_x =  $ptn 
center_y =  $y_center 
center_z = $z_center       
EOF
) > $config_file
    touch $i/run$i.sh
    ##### generating a script in the dir of each box
    # the script is to be executed in output dir 
(    cat << EOF
for f in \`ls ../$RECEPTOR_DIR/*.pdbqt\`;do
    prefix=\`basename \$f .pdbqt\`
    $vina --config config$i.txt --receptor \$f --ligand ../$LIGAND --out \$prefix.pdbqt --log \$prefix.log --cpu $NCPU
done
EOF
) > $i/run$i.sh
    chmod +x $i/run$i.sh
    #####
    i=$((i+1))
done

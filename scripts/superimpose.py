# running by command
# pymol -cqr this_script.py

from pymol import cmd
import os,glob,re

# working dir of the script, also output dir for prepare_receptor4.py
pdbqt_dir = 'receptors/wt-ensemble'

# relative path from working dir above
reference_structure = "../../structures/NA_2HU4.pdb"
pdb_dir = '../../clustering/WT/tmp/'
pdb_aligned_dir = '../../clustering/WT/ensemble/'
cmd_PREPARE_RECEPTOR = 'pythonsh /home/Ubuntu/tk/Programs/mgltools_i86Linux2_1.5.4/\
MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'

os.chdir(pdbqt_dir)
cmd.load(reference_structure, 'ref')
for f in glob.glob(pdb_dir+'/cluster-????.pdb'):
    cmd.load(f, 'obj1')
    new_pdb = re.sub("^.*\/",pdb_aligned_dir,f)
    # print new_pdb
    cmd.super('obj1','ref')
    cmd.save(new_pdb,'obj1')
    cmd.delete('obj1')
    os.system("%s -r %s" % (cmd_PREPARE_RECEPTOR, new_pdb) )


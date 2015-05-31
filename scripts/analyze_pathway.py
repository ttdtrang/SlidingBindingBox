#   favorable_interactions{'hydrophobic':  { 81: 0.2,
#                                             153: 0.3,
#                                             160: 0.27 },
#                           'saltbridge': {}
#                         }
#   

for p in ligand_poses_along_pathway:
    for interaction_type in favorable_interactions:
                                                                 number of occurences
    residues_with_interactions = { <resid>, < frequency = __________________________________________  > }
                                                              number of cluster representatives
#   # ensemble-based docking only
#       for each representative in clusters:
#           binana -ligand docked_ligand.pdbqt -receptor receptor.pdbqt -ouput_file interactions.pdb
#           interactions['hydrophobic'].append
#       

class LigandPose:
    '''Each LigandPose object corresponds to a ligand pose along the binding pathway,
contaning information about
    ligand_center
    ligand_head
    ligand_tail
and allowing retrieval of information about interation with receptor, such as
    residues_in_contact(cutoff=)
    residues_in_hydrophobic(cutoff=)
    residues_in_saltbrige(cutoff=)
    (retrieval of interation information is performed using functions provided by binana.py )
'''
    def __init__(self,center,head,tail):
        self.ligand_center = center
        self.ligand_head = head
        self.ligand_tail = tail
    def residues_in_contact(cutoff_1=0,cutoff_2=0):
        if cutoff_1 == 0: # set default
        if cutoff_2 == 0: # set default

    def __init__(self):
        

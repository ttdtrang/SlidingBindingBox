# run in wt/visual-cluster
import os.path
import sys
import clustering
from Interactions import *

number_of_clusters = 7
cutoff = 2.0
weight_be = 0.7
points = []

IFILE = open('../../../notes/pathway_points.pdb','r')
j = 1
for l in IFILE:
    values = l.split()
    at = atom()
    at.PDBIndex = values[1]
    at.atomname = values[2]
    at.residue = values[3]
    at.chain    = values[4]
    at.resid    = values[5]
    at.coordinates = point(float(values[6]), float(values[7]), float(values[8]) )
    at.bfactor = float(values[10])* weight_be
    at.atomtype = values[11]
    at.element = 'H'
    coords = [at.coordinates.x, at.coordinates.y, at.coordinates.z, at.bfactor]
    p = clustering.Point(coords , reference=at)
    points.append(p)

clusters = clustering.kmeans(points, number_of_clusters, cutoff)
for i in range(len(clusters)):
    if ( not os.path.exists(str(i+1))  ): os.mkdir(str(i+1))
    pdb_cluster = PDB()
    tot_be = 0.0
    for p in clusters[i].points:
        p.reference.bfactor = p.reference.bfactor / weight_be
        pdb_cluster.AddNewAtom(p.reference)
        tot_be += p.reference.bfactor
        (box_num, cluster_id) = (ord(p.reference.chain) - ord('A') +1, p.reference.resid)
        target = "../../%s/cluster-%04d.pdbqt" % (box_num, int(cluster_id) )
        link_name = "./cluster-%04d-box%s.pdbqt" % (int(cluster_id), box_num)  
        os.chdir(str(i+1))
        os.system("ln -sf %s %s" % (target, link_name) )
        os.chdir("..")
    pdb_cluster.UserNotes.append("STATISTICS")
    pdb_cluster.UserNotes.append("NUMBER OF POINTS: %s" % len(clusters[i].points))
    pdb_cluster.UserNotes.append("AVERAGE BINDING ENERGY: %s" % (tot_be/ len(clusters[i].points)))
    pdb_cluster.SavePDB("visual_cluster-%s.pdb" % (i+1))
        
# for i in range(len(clusters)):
#     IFILE = open("%s.txt" % i, 'r')
#     if ( not os.path.exists(str(i))  ):
#         os.mkdir(str(i))
#     j = 1
#     for l in IFILE:
#         (box_num, cluster_id) = l.split("-")
#         target = "../../%s/cluster-%04d.pdbqt" % (box_num, int(cluster_id) )
#         link_name = "./cluster-%04d.pdbqt" % j # sequentially re-numbered
#         j +=1
#         os.chdir(str(i))
#         os.system("ln -sf %s %s" % (target, link_name) )
#         os.chdir("..")

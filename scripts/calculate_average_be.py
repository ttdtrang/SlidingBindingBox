# run in wt/visual-cluster
from statlib import stats
OFILE = open("stats.txt",'w')
for i in range(1,8):
    BEs = []
    IFILE = open("visual_cluster-%s.pdb" % i, 'r')
    for l in IFILE:
        values = l.split()
        BEs.append(float(values[9]) / 0.7) # if given BEs are weighted
    OFILE.write("visual_cluster-%s: %s, stddev %s, lower %s, upper %s, min %s, max %s, median %s \n" % (i,stats.mean(BEs), 
stats.stdev(BEs), 
stats.scoreatpercentile(BEs,25), 
stats.scoreatpercentile(BEs,75),
min(BEs), max(BEs),
stats.median(BEs) ))
OFILE.close()
    

import os,getopt,sys
def usage():
    print """
-------------------------------------------------------
Usage: Splitting multiple-model PDB into single-model PDBs
-i OR --input-cluters=input_cluters, in PDB format 
-o OR --output-dir=output_dir, directory to store single pdb files 
-p OR --prefix=output_prefix [cluster], 
        output files will be named in the format PREFIX-xxxx, 
        with xxxx is zero-padded index
-h OR --help            print out this usage
-------------------------------------------------------
"""

def main():
    try:
        # getopt() puts string into options, e.g.
        # t --> -t
        # and return opts()
        # take input parameter values and return the remainder as args()
        opts,args = getopt.getopt(sys.argv[1:],"i:o:p:h",["input-cluters=", \
                                                        "output-dir=", \
                                                        "output-prefix=", \
                                                        "help"])
    except getopt.GetoptError as err:
        print err
        usage()
        sys.exit(2)

    ##### default values #####
    in_cluster = "clusters-06.pdb"
    out_dir = "cluters-06"
    out_prefix = 'cluster'

    ##### read values in #####
    for o,a in opts:
        if o in ("-i","--input-clusters"):
            in_cluster = a
        elif o in ("-o","--output-dir"):                out_dir = a
        elif o in ("-p","--output-prefix"):             out_prefix = a
        elif o in ("-h","--help"):
            usage()
            sys.exit()
        else:
            assert False,"unhandled option"

    ##### #####
    split_clusters(in_cluster,out_dir,out_prefix)

    exit()

def split_clusters(in_cluster,out_dir,out_prefix):
    IFILE = open(in_cluster,'r')
    i = 1
    for l in IFILE:
        if (l[0:5] == 'TITLE'):
            OPREFIX = "%s/%s-%04d" % (out_dir, out_prefix ,i)
            OPDB = open(OPREFIX+".pdb",'w')
            OPDB.write(l)
        elif (l[0:6] == 'ENDMDL'):
            OPDB.write(l)
            i += 1
            OPDB.close()
        else:
            OPDB.write(l)



if __name__ == '__main__':
    main() 

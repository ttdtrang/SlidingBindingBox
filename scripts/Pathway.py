from Interactions import *
from AutodockVina import *
from datetime import datetime
from statlib import stats
import glob

__metaclass__ = type

class Residue:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __hash__(self):
        return hash((self.name, self.number))
    def __eq__(self, another):
        if (self.name == another.name and self.number == another.number):
            return True
        else:
            return False
    def __gt__(self,another):
        if self.number > another.number: return True
        return False
    def __lt__(self,another):
        if self.number < another.number: return True
        return False
    def __str__(self):
        return '%s %s' % (self.name, self.number) 

class InteractionProfile:
    '''describe a set of interactions between a ligand and receptor residues along with frequencies'''
    def __init__(self, docked_dir, ensemble_dir, glob_pattern):
        '''calculate frequencies from set of Interactions provided'''
        #   # datastructure example
        #   Residue    | interaction_type  |  interaction_lists
        #   -----------|-------------------|-------------------
        #   ILE 437    | electrostatic     |  i1, i2, ... in   
        #   TRP 483    | electrostatic     |                  
        #    ...       |                   |                   
        #   ---------------------------------------------------
        self.interaction_tables = []
        self.binding_energies = []
        self.docked_ligands = [] # class PDB
        self.centers_of_geometry = []
        self.centers_of_mass = []
        self.statistics = {}
        self._frequencies = {}
        self._fill_in_data(docked_dir, ensemble_dir, glob_pattern)
        self._statistics()
        self._centroid = self._get_centroid()
        
    def __len__(self):
        return len(self.interaction_tables)
    def _fill_in_data(self,docked_dir, ensemble_dir, glob_pattern):
        # assume same names for receptor and docked results
        receptor_ensemble = glob.glob(ensemble_dir+ '/' + glob_pattern)
        # quick fix, truncate '-boxj' from  'cluster-xxxx-boxj.pdbqt'
        receptor_ensemble.sort()
        all_residues = []
        self._ensemble_size = len(receptor_ensemble)
        receptor_states_by_residue = {}
        for rec in receptor_ensemble:
            itable = {}
            base = os.path.basename(rec)
            # if there are many docked results for the same receptor
            ligs = glob.glob(docked_dir+ '/' + base[:base.find(".")] + '*.pdbqt')  # remove extension, add * to make regexp
            for li in ligs:
                vinaio = VinaIO(receptor_pdbqt=rec,docked_pdbqt=docked_dir+ '/' + base)
                pick_out = 'tmp.pdbqt'
                vinaio.write_conformation(pick_out,1)
                cmd_params = command_line_parameters("")
                d = Interactions(pick_out,rec,cmd_params)
            self.binding_energies.append(d.binding_energy)
            self.docked_ligands.append(d.ligand)
            self.centers_of_geometry.append(d.ligand.functions.centroid( *[ d.ligand.AllAtoms[i].coordinates for i in d.ligand.AllAtoms ] ) )
            self.centers_of_mass.append(d.ligand.functions.center_of_mass( *[ d.ligand.AllAtoms[i] for i in d.ligand.AllAtoms ] ))
            # ----Data fill-in-----------------------------
            #   elec = d.electrostatic_interactions()
            #   for i in elec:
            #       print  i.receptor_atom.residue + " " + str(i.receptor_atom.resid)
            for i in d:
                # print i.receptor_atom.residue + " "  + str(i.receptor_atom.resid)
                res = Residue(i.receptor_atom.residue, i.receptor_atom.resid)
                if res not in all_residues: all_residues.append(res)
                #
                if receptor_states_by_residue.has_key(res): receptor_states_by_residue[res].append(os.path.basename(d.receptor_pdbqt_filename))
                else:
                    receptor_states_by_residue[res] = [os.path.basename(d.receptor_pdbqt_filename)]
                #
                if itable.has_key(res):
                    if not (itable[res].has_key(i.type)):
                        itable[res][i.type] = []
                    itable[res][i.type].append(i)
                else:
                    itable[res] = {i.type: [i]}
            # ---------------------------------------------
            os.system('rm %s' % pick_out)
            self.interaction_tables.append(itable)
            self._all_residues = tuple(all_residues)
            self._receptor_states_by_residue = receptor_states_by_residue
    def frequency(self, residue, interaction='all', weighted=False):
        '''return frequency of specific interaction of given residue'''
        if self._frequencies == {}: self._fill_frequencies()
        return self._frequencies[residue][interaction]
    def _fill_frequencies(self,weighted=False):
        if weighted == False:
            for res in self._all_residues:
                self._frequencies[res] = {'all' : 0,
                                         'electrostatic' : 0,
                                         'hydrophobic'   : 0,
                                         'hydrogen'      : 0,
                                         'closecontact'  : 0
                                        }
                for itable in self.interaction_tables:
                    if itable.has_key(res):
                        self._frequencies[res]['all'] += 1
                        for interaction in ['electrostatic', 'hydrophobic', 'hydrogen', 'closecontact']:
                            if itable[res].has_key(interaction): self.frequencies[res][interaction] += 1
                self._frequencies[res] = dict(( k , (float(v) / self._ensemble_size)) for (k,v) in self._frequencies[res].items() )
        else:
            pass # handle later

    def coulomb_energies(self,residue=None):
        '''variation of coulomb energies of all residues (or given residue) through the ensemble'''
        energies = []
        if residue is None:
            # check if the calculation was already performed
            if self.statistics.has_key('coulomb_energies'): return self.statistics['coulomb_energies']
            for itable in self.interaction_tables:
                e = 0.0
                for res in itable.keys():
                    if itable[res].has_key('electrostatic'):
                        for i in itable[res]['electrostatic']:
                            e += i.coulomb_energy
                    energies.append(e)
            self.statistics['coulomb_energies'] = energies
        else:
            for itable in self.interaction_tables:
                e = 0.0
                if itable.has_key(residue):
                    for  i in itable[residue]['electrostatic']:
                        e += i.coulomb_energy
                energies.append(e)
        return energies 
    def __str__(self):
        outstr = ""
        for itable in self.interaction_tables:
            for res in itable.keys():
                for i in itable[res].keys():
                    line = "%s %15s %s\n" % (res, i, itable[res][i])
                    outstr += line
        return outstr
    def _statistics(self):
        if self.statistics == {}:
            self.statistics['coulomb_energies'] = self.coulomb_energies()
            self.statistics['sum'] = 0
            self.statistics['electrostatic'] = 0
            self.statistics['hydrogen'] = 0
            self.statistics['hydrophobic'] = 0
            self.statistics['closecontact'] = 0
            for itable in self.interaction_tables:
                for res in itable.keys():
                    for t in itable[res].keys():
                        self.statistics['sum'] += len(itable[res][t])
                        if self.statistics.has_key(t): self.statistics[t] += len(itable[res][t])
                        else: self.statistics[t] = len(itable[res][t])
    def _get_centroid(self):
        num_points = len(self.centers_of_geometry)
        if num_points ==0: return point(99999, 99999, 99999)
        (x,y,z) = (0.0, 0.0, 0.0)
        for p in self.centers_of_geometry:
            x += p.x
            y += p.y
            z += p.z
        return point(x/num_points, y/num_points , z/num_points )
    def __getattr__(self,name):
        name = '_' + name
        return self.__dict__[name]
#   class Point:
#       '''instances of Point make up a Pathway'''
#       pass

class Pathway:
    '''defined by a sequence of anchors'''
    def __init__(self):
        self.points = []
    def __iter__(self):
        return iter(self.points)
    def append(self,value):
        self.points.append(value)
    def __getitem__(self,index): return self.points[index]
    def __setitem__(self,index,value): self.points[index] = value
    def __len__(self):
        return len(self.points)

if __name__ == '__main__':
#    # Illustrative use
#    i_profile_1 = InteractionProfile(docked_dir = '../vina-ensemble/wt/1/',
#                                    ensemble_dir= '../receptors/wt-ensemble/',
#                                    glob_pattern= '*-000?.pdbqt')
#    target_res= Residue('ILE',437)
#    print len(i_profile_1)
#    print "Frequency of %s %s having interactions (of any type) in the ensemble: %f" % (target_res.name, target_res.number, i_profile_1.frequency(target_res))
#    print "Frequency of %s %s having hydrogen bonds in the ensemble: %f" % (target_res.name, target_res.number, i_profile_1.frequency(target_res,interaction='hydrogen'))
#    print "Frequency of %s %s having electrostatic interactions in the ensemble: %f" % (target_res.name, target_res.number, i_profile_1.frequency(target_res,interaction='electrostatic'))
#    print "Coulomb energies of %s %s through the ensemble: " % (target_res.name, target_res.number)
#    print (i_profile_1.coulomb_energies(target_res))
#    print "Coulomb energies through the ensemble: " 
#    print i_profile_1.coulomb_energies()
#    freqs = i_profile_1.frequencies
#    receptor_indexes= set([ int(f[8:12]) for f in i_profile_1.receptor_states_by_residue[target_res] ]) # extract the indexing part from receptor filename, remove duplicate indexes
#    print "Receptor conformations having interactions with %s: %s" % (target_res, receptor_indexes )
#    #for r in freqs.keys():
#    #    print str(r) + " - "  + str(freqs[r])

    
    # Analyzing docked results in vina-ensemble
    p = Pathway()
    RESULT_DIR = '../vina-ensemble/wt/'
    is_testing = True # switch to avoid messing up analyzed data
    for i in range(6):
        iprofile = InteractionProfile( docked_dir = RESULT_DIR + str(i+1),
                                       ensemble_dir= '../receptors/wt-ensemble/',
                                       glob_pattern= 'cluster-*.pdbqt')
        p.append(iprofile)
    output = "Pathway analysis. Result dir: %s. Performed at %s" % (RESULT_DIR, str(datetime.now()))
    output += "\n1. Statistics\n"
    output += "----------------------------------------------------------------------------------------------------------------------------\n"
    output += "                                             Interaction_component_counts            CoulombEnergy_Contribution             \n"
    output += " Box Sum_of_interacting_atoms CloseContact Hydrophobic HydrogenBond Electrostatic   mean      stddev                        \n"
    output += "----------------------------------------------------------------------------------------------------------------------------\n"
    pattern1= " %s  %4s                      %s           %s          %s           %s              %10.3f    %10.3f                        \n"
    for i in range(len(p)):
        elec_energies = p[i].statistics['coulomb_energies']
        output += pattern1 % (i+1, p[i].statistics['sum'],
                                    p[i].statistics['closecontact'],
                                    p[i].statistics['hydrophobic'],
                                    p[i].statistics['hydrogen'],
                                    p[i].statistics['electrostatic'],
                                    (stats.mean(elec_energies),0.0)[len(elec_energies) == 0],
                                    (stats.stdev(elec_energies),0.0)[len(elec_energies) == 0]
                              )
    OFILE = open('pathway_analysis.txt','w')
    OFILE.write(output)

    output  = "\n2.Details. List of residues with high-frequency (>= 40%) of interactions in each box\n"
    output += "---------------------------------------------------------------------------------------------\n"
    output += " Box Residue                 Interaction_frequency                            Receptor_states\n"
    output += "               CloseContact Hydrophobic HydrogenBond Electrostatic All                       \n"
    output += "---------------------------------------------------------------------------------------------\n" 
    pattern2= " %s  %s        %7.3f        %7.3f       %7.3f        %7.3f         %7.3f      %s\n"
    residue_set = [] 
    for i in range(len(p)):
        residue_set.append( [] )
        for res in p[i].all_residues:
            if p[i].frequency(res) >= 0.3:
                # get list of receptors by specified residue
                freqs = p[i].frequencies[res]
                conformations = set([ int(f[8:12]) for f in p[i].receptor_states_by_residue[res] ])
                output += pattern2 % ( i+1, str(res),
                                            freqs['closecontact'],
                                            freqs['hydrophobic'],
                                            freqs['hydrogen'],
                                            freqs['electrostatic'],
                                            freqs['all'],
                                            str(conformations)
                                     )
    OFILE.write(output)
    
    output  = "\n3.Average of binding energies\n"
    output += "------------------------------------------------\n"
    output += " Box  Binding energy (kcal/mol)\n"
    output += "       mean      stddev       min         max \n"
    output += "------------------------------------------------\n"
    pattern3=" %s     %.2f        %.2f       %.2f         %.2f      \n"
    for i in range(len(p)):
        output += pattern3 % (i+1, stats.mean(p[i].binding_energies),stats.stdev(p[i].binding_energies),min(p[i].binding_energies), max(p[i].binding_energies) )
    OFILE.write(output)
    
    output  = "\n4.Average center of geometry \n"
    output += "------------------------------\n"
    output += " Box      Centroid            \n"
    output += "------------------------------\n"
    pattern4=" %s     %s                    \n"
    for i in range(len(p)):
        output += pattern4 % (i+1, p[i].centroid  )
    OFILE.write(output)
    OFILE.close()

    OFILE = open('BindingEnergies.txt','w')
    output   = '# Result dir: %s. Performed at %s\n' % (RESULT_DIR, datetime.now() )
    output  += '# Binding energies of docked conformations, attached to ligand center of mass\n'
    output  += '# Box Cluster      Center_of_mass(x,y,z)       BindingEnergy    Center_of_geometry(x,y,z)\n'
    pattern5 = '  %s   %s        % .3f      % .3f      % .3f       %.3f       % .3f      % .3f       % .3f\n'

    for i in range(len(p)):
        ### Writing data for plotting Binding energies vs coordinates
        for j in range(len(p[i].binding_energies)):
            cog = p[i].centers_of_geometry[j]
            com = p[i].centers_of_mass[j]
            output += pattern5 % (i+1,j+1,com.x, com.y, com.z, p[i].binding_energies[j],
                                          cog.x, cog.y, cog.z)
        output += "\n\n"
        ### Plotting using PDB, centroid coordinates are visualized as atoms,
        ### centroids of the same box belong to the same chain
        pdb_centroids = PDB()
        pdb_centers_of_mass = PDB()
        pdb_NCvector = PDB() # PDB describing vector N13 - C22
        for j in range(len(p[i].centers_of_geometry)):
            centroid_atom = atom()
            centroid_atom.atomname = "C"
            centroid_atom.residue = "CTR" # centroid
            centroid_atom.coordinates = p[i].centers_of_geometry[j] #point(99999, 99999, 99999)
            centroid_atom.element = "H"
            centroid_atom.PDBIndex = j+1
            centroid_atom.atomtype="R"
            centroid_atom.charge = 0
            centroid_atom.resid = j+1
            centroid_atom.chain = chr(ord('A') + i)
            centroid_atom.bfactor = p[i].binding_energies[j]
            pdb_centroids.AddNewAtom(centroid_atom)
        pdb_centroids.SavePDB("centroids-box%s.pdb" % (i+1) )
        for j in range(len(p[i].centers_of_mass)):
            com_atom = atom()
            com_atom.atomname = "COM"
            com_atom.residue = "COM" # centroid
            com_atom.coordinates = p[i].centers_of_mass[j] #point(99999, 99999, 99999)
            com_atom.element = "H"
            com_atom.PDBIndex = j+1
            com_atom.atomtype="R"
            com_atom.charge = 0
            com_atom.resid = j+1
            com_atom.chain = chr(ord('A') + i)
            com_atom.bfactor = p[i].binding_energies[j]
            pdb_centers_of_mass.AddNewAtom(com_atom)
        pdb_centers_of_mass.SavePDB("com-box%s.pdb" % (i+1) )
        for j in range(len(p[i].docked_ligands)):
            N13 = p[i].docked_ligands[j].AllAtoms[13].copy_of()
            C22 = p[i].docked_ligands[j].AllAtoms[22].copy_of()
            N13.residue = "VEC"
            C22.residue = "VEC"
            N13.resid = j+1
            C22.resid = j+1
            pdb_NCvector.AddNewAtom(N13)
            pdb_NCvector.AddNewAtom(C22)
            pdb_NCvector.connectivities.append((2*j+1,2*j+2))  # j starts at 0
        pdb_NCvector.SavePDB("NCvector-box%s.pdb" % (i+1))
    OFILE.write(output)
    OFILE.close()
    if is_testing == False:
        os.system('cp pathway_analysis.txt %s/' % RESULT_DIR)
        os.system("cp centroids-box*.pdb %s/" % RESULT_DIR))
        os.system("cp com-box*.pdb %s/" % RESULT_DIR)
        os.system("cp NCvector-box*.pdb %s/"% RESULT_DIR)

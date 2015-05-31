# Modified version of binana program

import os,sys
sys.path.append(os.environ['HOME']+'/python/VirtualScreening/')

import math
import textwrap
from AutodockVina import VinaIO

__metaclass__ = type # new-style class
class PeriodicTable:
    atomic_mass = {'H' : 1.00794 ,
                            'C' :12.0107 ,
                            'N' :14.00674 ,
                            'O' :15.9994 ,
                            'S' :32.066 ,
                            'P' :30.973761,
                            'F' :18.9984032,
                            'Cl':35.4527 ,
                            'Br':79.904 ,
                            'I' :126.90447 
                            }

    def __init__(self):
        pass
        
class point:
    x=99999.0
    y=99999.0
    z=99999.0
    
    def __init__ (self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z

    def copy_of(self):
        return point(self.x, self.y, self.z)

    def print_coors(self):
        print str(self.x)+"\t"+str(self.y)+"\t"+str(self.z)
        
    def snap(self,reso): # snap the point to a grid
        self.x = round(self.x / reso) * reso
        self.y = round(self.y / reso) * reso
        self.z = round(self.z / reso) * reso
        
    def dist_to(self,apoint):
        return math.sqrt(math.pow(self.x - apoint.x,2) + math.pow(self.y - apoint.y,2) + math.pow(self.z - apoint.z,2))

    def description(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)
    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def Magnitude(self):
        return self.dist_to(point(0,0,0))
        
    def CreatePDBLine(self, index):

        output = "ATOM "
        output = output + str(index).rjust(6) + "X".rjust(5) + "XXX".rjust(4)
        output = output + ("%.3f" % self.x).rjust(18)
        output = output + ("%.3f" % self.y).rjust(8)
        output = output + ("%.3f" % self.z).rjust(8)
        output = output + "X".rjust(24) 
        return output

class atom:
    def __init__ (self):
        self.atomname = ""
        self.residue = ""
        self.coordinates = point(99999, 99999, 99999)
        self.element = ""
        self.PDBIndex = ""
        self.line=""
        self.atomtype=""
        self.IndeciesOfAtomsConnecting=[]
        self.charge = 0
        self.resid = 0
        self.chain = ""
        self.structure = ""
        self.comment = ""
        self.bfactor = 0.0
        
    def copy_of(self):
        theatom = atom()
        theatom.atomname = self.atomname 
        theatom.residue = self.residue 
        theatom.coordinates = self.coordinates.copy_of()
        theatom.element = self.element 
        theatom.PDBIndex = self.PDBIndex 
        theatom.line= self.line
        theatom.atomtype= self.atomtype
        theatom.IndeciesOfAtomsConnecting = self.IndeciesOfAtomsConnecting[:]
        theatom.charge = self.charge 
        theatom.resid = self.resid 
        theatom.chain = self.chain 
        theatom.structure = self.structure 
        theatom.comment = self.comment
        theatom.bfactor = self.bfactor
        
        return theatom

    def CreatePDBLine(self, index):
        
        output = "ATOM "
        output = output + str(index).rjust(6) + self.atomname.rjust(5) + self.residue.rjust(4)
        # TK, 2012-04-11
        output = output + self.chain.rjust(2) + str(self.resid).rjust(4)
        output = output + ("%.3f" % self.coordinates.x).rjust(12) # original rjust(18) 
        output = output + ("%.3f" % self.coordinates.y).rjust(8)
        output = output + ("%.3f" % self.coordinates.z).rjust(8)
        output = output + ("%.2f" % self.bfactor).rjust(12) # bfactor added to store binding energy, 2012-06-20
        output = output + self.element.rjust(12) 
        return output

    def NumberOfNeighbors(self):
        return len(self.IndeciesOfAtomsConnecting)

    def AddNeighborAtomIndex(self, index):
        if not (index in self.IndeciesOfAtomsConnecting):
            self.IndeciesOfAtomsConnecting.append(index)
    
    def SideChainOrBackBone(self): # only really applies to proteins, assuming standard atom names
        if self.atomname.strip() == "CA" or self.atomname.strip() == "C" or self.atomname.strip() == "O" or self.atomname.strip() == "N":
            return "BACKBONE"
        else:
            return "SIDECHAIN"
    
    def ReadPDBLine(self, Line):
        self.line = Line
        self.atomname = Line[11:16].strip()
        
        if len(self.atomname)==1:
            self.atomname = self.atomname + "  "
        elif len(self.atomname)==2:
            self.atomname = self.atomname + " "
        elif len(self.atomname)==3:
            self.atomname = self.atomname + " " # This line is necessary for babel to work, though many PDBs in the PDB would have this line commented out
        
        self.coordinates = point(float(Line[30:38]), float(Line[38:46]), float(Line[46:54]))
        
        # now atom type (for pdbqt)
        self.atomtype = Line[77:79].strip().upper()

        if Line[69:76].strip() != "":
            self.charge = float(Line[69:76])
        else:
            self.charge = 0.0
        
        if self.element == "": # try to guess at element from name
            two_letters = self.atomname[0:2].strip().upper()
            if two_letters=='BR':
                self.element='BR'
            elif two_letters=='CL':
                self.element='CL'
            elif two_letters=='BI':
                self.element='BI'
            elif two_letters=='AS':
                self.element='AS'
            elif two_letters=='AG':
                self.element='AG'
            elif two_letters=='LI':
                self.element='LI'
            #elif two_letters=='HG':
            #    self.element='HG'
            elif two_letters=='MG':
                self.element='MG'
            elif two_letters=='MN':
                self.element='MN'
            elif two_letters=='RH':
                self.element='RH'
            elif two_letters=='ZN':
                self.element='ZN'
            elif two_letters=='FE':
                self.element='FE'
            else: #So, just assume it's the first letter.
                # Any number needs to be removed from the element name
                self.element = self.atomname
                self.element = self.element.replace('0','')
                self.element = self.element.replace('1','')
                self.element = self.element.replace('2','')
                self.element = self.element.replace('3','')
                self.element = self.element.replace('4','')
                self.element = self.element.replace('5','')
                self.element = self.element.replace('6','')
                self.element = self.element.replace('7','')
                self.element = self.element.replace('8','')
                self.element = self.element.replace('9','')
                self.element = self.element.replace('@','')

                self.element = self.element[0:1].strip().upper()
                
        self.PDBIndex = Line[6:12].strip()
        self.residue = Line[16:20]
        #self.residue = " " + self.residue[-3:] # this only uses the rightmost three characters, essentially removing unique rotamer identification
        self.residue = self.residue[-3:] # this only uses the rightmost three characters, essentially removing unique rotamer identification
        self.resid = int(Line[23:26])
        self.chain = Line[21:22]
        if self.residue.strip() == "": self.residue = " MOL"
        
class PDB:

    def __init__ (self):
        self.AllAtoms={}
        self.NonProteinAtoms = {}
        self.max_x = -9999.99
        self.min_x = 9999.99
        self.max_y = -9999.99
        self.min_y = 9999.99
        self.max_z = -9999.99
        self.min_z = 9999.99
        self.rotateable_bonds_count = 0
        self.functions = MathFunctions()
        self.protein_resnames = ["ALA", "ARG", "ASN", "ASP", "ASH", "ASX", "CYS", "CYM", "CYX", "GLN", "GLU", "GLH", "GLX", "GLY", "HIS", "HID", "HIE", "HIP", "ILE", "LEU", "LYS", "LYN", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
        self.aromatic_rings = []
        self.charges = [] # a list of points
        self.connectivities = [] # list of tuples 
        self.UserNotes = []
    def LoadPDB(self, FileName, min_x=-9999.99, max_x=9999.99, min_y=-9999.99, max_y=9999.99, min_z=-9999.99, max_z=9999.99):

        autoindex = 1

        self.__init__()
        
        # Now load the file into a list
        file = open(FileName,"r")
        lines = file.readlines()
        file.close()
        
        atom_already_loaded = [] # going to keep track of atomname_resid_chain pairs, to make sure redundants aren't loaded. This basically
                                 # gets rid of rotomers, I think.
        
        for t in range(0,len(lines)):
            line=lines[t]
            
            if "between atoms" in line and " A " in line:
                    self.rotateable_bonds_count = self.rotateable_bonds_count + 1
                    
            if len(line) >= 7:
                if line[0:4]=="ATOM" or line[0:6]=="HETATM": # Load atom data (coordinates, etc.)
                    TempAtom = atom()
                    TempAtom.ReadPDBLine(line)
                    
                    if TempAtom.coordinates.x > min_x and TempAtom.coordinates.x < max_x and TempAtom.coordinates.y > min_y and TempAtom.coordinates.y < max_y and TempAtom.coordinates.z > min_z and TempAtom.coordinates.z < max_z:
                        
                        if self.max_x < TempAtom.coordinates.x: self.max_x = TempAtom.coordinates.x
                        if self.max_y < TempAtom.coordinates.y: self.max_y = TempAtom.coordinates.y
                        if self.max_z < TempAtom.coordinates.z: self.max_z = TempAtom.coordinates.z
                        
                        if self.min_x > TempAtom.coordinates.x: self.min_x = TempAtom.coordinates.x
                        if self.min_y > TempAtom.coordinates.y: self.min_y = TempAtom.coordinates.y
                        if self.min_z > TempAtom.coordinates.z: self.min_z = TempAtom.coordinates.z

                        key = TempAtom.atomname.strip() + "_" + str(TempAtom.resid) + "_" + TempAtom.residue.strip() + "_" + TempAtom.chain.strip() # this string unique identifies each atom
                        
                        if key in atom_already_loaded and TempAtom.residue.strip() in self.protein_resnames: # so this is a protein atom that has already been loaded once
                            self.printout("Warning: Duplicate protein atom detected: \"" + TempAtom.line.strip() + "\". Not loading this duplicate.")
                            print ""
                        
                        if not key in atom_already_loaded or not TempAtom.residue.strip() in self.protein_resnames: # so either the atom hasn't been loaded, or else it's a non-protein atom
                                                                                                            # so note that non-protein atoms can have redundant names, but protein atoms cannot.
                                                                                                            # This is because protein residues often contain rotamers
                            atom_already_loaded.append(key) # so each atom can only be loaded once. No rotamers.
                            self.AllAtoms[autoindex] = TempAtom # So you're actually reindexing everything here.
                            if not TempAtom.residue[-3:] in self.protein_resnames: self.NonProteinAtoms[autoindex] = TempAtom
                            
                            autoindex = autoindex + 1
                        
        self.CheckProteinFormat()

        self.CreateBondsByDistance() # only for the ligand, because bonds can be inferred based on atomnames from PDB
        self.assign_aromatic_rings()
        self.assign_charges()
 
    def CreateCONECTRecord(self,*atom_indices):
        output = "CONECT"
        for i in atom_indices:
            output += str(i).rjust(5)
        return output
    def CreateUSERRecord(self):
        output = ""
        for i in range(len(self.UserNotes)):
            output += "USER  "
            output += str(i+1).rjust(4)
            output += " "+ (self.UserNotes[i] + "\n")
        return output[:-1]
   
    def printout(self, thestring):
        lines = textwrap.wrap(thestring, 80)
        for line in lines:
            print line
            
    def SavePDB(self, filename):
        f = open(filename, 'w')
        towrite = self.SavePDBString()
        if towrite.strip() == "": towrite = "ATOM      1  X   XXX             0.000   0.000   0.000                       X" # just so no PDB is empty, VMD will load them all
        f.write(towrite)
        f.close()
    
    def SavePDBString(self):
        ToOutput = ""
        # write user notes
        ToOutput = ToOutput + self.CreateUSERRecord() + "\n"
        # write coordinates
        for atomindex in self.AllAtoms:
            ToOutput = ToOutput + self.AllAtoms[atomindex].CreatePDBLine(atomindex) + "\n"
        # write connectivities
        if len(self.connectivities) > 0:
            for con in self.connectivities:
                ToOutput += self.CreateCONECTRecord(*con) + "\n"
        return ToOutput
    
    def AddNewAtom(self, atom):
        
        # first get available index
        t = 1
        while t in self.AllAtoms.keys():
            t = t + 1
    
        # now add atom
        self.AllAtoms[t] = atom
    
    def SetResname(self, resname):
        for atomindex in self.AllAtoms:
            self.AllAtoms[atomindex].residue = resname

    def connected_atoms_of_given_element(self, index, connected_atom_element):
        atom = self.AllAtoms[index]
        connected_atoms = []
        for index2 in atom.IndeciesOfAtomsConnecting:
            atom2 = self.AllAtoms[index2]
            if atom2.element == connected_atom_element:
                connected_atoms.append(index2)
        return connected_atoms
    
    def connected_heavy_atoms(self, index):
        atom = self.AllAtoms[index]
        connected_atoms = []
        for index2 in atom.IndeciesOfAtomsConnecting:
            atom2 = self.AllAtoms[index2]
            if atom2.element != "H": connected_atoms.append(index2)
        return connected_atoms

    def CheckProteinFormat(self):
        curr_res = ""
        first = True
        residue = []
        
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            
            key = atom.residue + "_" + str(atom.resid) + "_" + atom.chain
            
            if first == True:
                curr_res = key
                first = False
                
            if key != curr_res: 

                self.CheckProteinFormat_process_residue(residue, last_key)
                
                residue = []
                curr_res = key
            
            residue.append(atom.atomname.strip())
            last_key = key
        
        self.CheckProteinFormat_process_residue(residue, last_key)


    def CheckProteinFormat_process_residue(self, residue, last_key): 
        temp = last_key.strip().split("_")
        resname = temp[0]
        real_resname = resname[-3:]
        resid = temp[1]
        chain = temp[2]
                
        if real_resname in self.protein_resnames: # so it's a protein residue
            
            if not "N" in residue:
                self.printout('Warning: There is no atom named "N" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine secondary structure. If this residue is far from the active site, this warning may not affect the NNScore.')
                print ""
            if not "C" in residue:
                self.printout('Warning: There is no atom named "C" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine secondary structure. If this residue is far from the active site, this warning may not affect the NNScore.')
                print ""
            if not "CA" in residue:
                self.printout('Warning: There is no atom named "CA" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine secondary structure. If this residue is far from the active site, this warning may not affect the NNScore.')
                print ""
            
            if real_resname == "GLU" or real_resname == "GLH" or real_resname == "GLX":
                if not "OE1" in residue:
                    self.printout('Warning: There is no atom named "OE1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "OE2" in residue:
                    self.printout('Warning: There is no atom named "OE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""

            if real_resname == "ASP" or real_resname == "ASH" or real_resname == "ASX":
                if not "OD1" in residue:
                    self.printout('Warning: There is no atom named "OD1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "OD2" in residue:
                    self.printout('Warning: There is no atom named "OD2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "LYS" or real_resname == "LYN":
                if not "NZ" in residue:
                    self.printout('Warning: There is no atom named "NZ" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-cation and salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "ARG":
                if not "NH1" in residue:
                    self.printout('Warning: There is no atom named "NH1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-cation and salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "NH2" in residue:
                    self.printout('Warning: There is no atom named "NH2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-cation and salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "HIS" or real_resname == "HID" or real_resname == "HIE" or real_resname == "HIP":
                if not "NE2" in residue:
                    self.printout('Warning: There is no atom named "NE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-cation and salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "ND1" in residue:
                    self.printout('Warning: There is no atom named "ND1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-cation and salt-bridge interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "PHE":
                if not "CG" in residue:
                    self.printout('Warning: There is no atom named "CG" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD1" in residue:
                    self.printout('Warning: There is no atom named "CD1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD2" in residue:
                    self.printout('Warning: There is no atom named "CD2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE1" in residue:
                    self.printout('Warning: There is no atom named "CE1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE2" in residue:
                    self.printout('Warning: There is no atom named "CE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CZ" in residue:
                    self.printout('Warning: There is no atom named "CZ" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "TYR":
                if not "CG" in residue:
                    self.printout('Warning: There is no atom named "CG" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD1" in residue:
                    self.printout('Warning: There is no atom named "CD1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD2" in residue:
                    self.printout('Warning: There is no atom named "CD2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE1" in residue:
                    self.printout('Warning: There is no atom named "CE1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE2" in residue:
                    self.printout('Warning: There is no atom named "CE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CZ" in residue:
                    self.printout('Warning: There is no atom named "CZ" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "TRP":
                if not "CG" in residue:
                    self.printout('Warning: There is no atom named "CG" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD1" in residue:
                    self.printout('Warning: There is no atom named "CD1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD2" in residue:
                    self.printout('Warning: There is no atom named "CD2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "NE1" in residue:
                    self.printout('Warning: There is no atom named "NE1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE2" in residue:
                    self.printout('Warning: There is no atom named "CE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE3" in residue:
                    self.printout('Warning: There is no atom named "CE3" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CZ2" in residue:
                    self.printout('Warning: There is no atom named "CZ2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CZ3" in residue:
                    self.printout('Warning: There is no atom named "CZ3" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CH2" in residue:
                    self.printout('Warning: There is no atom named "CH2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
            if real_resname == "HIS" or real_resname == "HID" or real_resname == "HIE" or real_resname == "HIP":
                if not "CG" in residue:
                    self.printout('Warning: There is no atom named "CG" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "ND1" in residue:
                    self.printout('Warning: There is no atom named "ND1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CD2" in residue:
                    self.printout('Warning: There is no atom named "CD2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "CE1" in residue:
                    self.printout('Warning: There is no atom named "CE1" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
                if not "NE2" in residue:
                    self.printout('Warning: There is no atom named "NE2" in the protein residue ' + last_key + '. Please use standard naming conventions for all protein residues. This atom is needed to determine pi-pi and pi-cation interactions. If this residue is far from the active site, this warning may not affect the NNScore.')
                    print ""
            
                        
    # Functions to determine the bond connectivity based on distance
    # ==============================================================
    
    def CreateBondsByDistance(self):
        for AtomIndex1 in self.NonProteinAtoms:
            atom1 = self.NonProteinAtoms[AtomIndex1]
            if not atom1.residue[-3:] in self.protein_resnames: # so it's not a protein residue            
                for AtomIndex2 in self.NonProteinAtoms:
                    if AtomIndex1 != AtomIndex2:
                        atom2 = self.NonProteinAtoms[AtomIndex2]
                        if not atom2.residue[-3:] in self.protein_resnames: # so it's not a protein residue
                            dist = self.functions.distance(atom1.coordinates, atom2.coordinates)
                            
                            if (dist < self.BondLength(atom1.element, atom2.element) * 1.2):
                                atom1.AddNeighborAtomIndex(AtomIndex2)
                                atom2.AddNeighborAtomIndex(AtomIndex1)

    def BondLength(self, element1, element2):
        
        '''Bond lengths taken from Handbook of Chemistry and Physics. The information provided there was very specific,
        so I tried to pick representative examples and used the bond lengths from those. Sitautions could arise where these
        lengths would be incorrect, probably slight errors (<0.06) in the hundreds.'''
        
        distance = 0.0
        if element1 == "C" and element2 == "C": distance = 1.53
        if element1 == "N" and element2 == "N": distance = 1.425
        if element1 == "O" and element2 == "O": distance = 1.469
        if element1 == "S" and element2 == "S": distance = 2.048
        if (element1 == "C" and element2 == "H") or (element1 == "H" and element2 == "C"): distance = 1.059
        if (element1 == "C" and element2 == "N") or (element1 == "N" and element2 == "C"): distance = 1.469
        if (element1 == "C" and element2 == "O") or (element1 == "O" and element2 == "C"): distance = 1.413
        if (element1 == "C" and element2 == "S") or (element1 == "S" and element2 == "C"): distance = 1.819
        if (element1 == "N" and element2 == "H") or (element1 == "H" and element2 == "N"): distance = 1.009
        if (element1 == "N" and element2 == "O") or (element1 == "O" and element2 == "N"): distance = 1.463
        if (element1 == "O" and element2 == "S") or (element1 == "S" and element2 == "O"): distance = 1.577
        if (element1 == "O" and element2 == "H") or (element1 == "H" and element2 == "O"): distance = 0.967
        if (element1 == "S" and element2 == "H") or (element1 == "H" and element2 == "S"): distance = 2.025/1.5 # This one not from source sited above. Not sure where it's from, but it wouldn't ever be used in the current context ("AutoGrow")
        if (element1 == "S" and element2 == "N") or (element1 == "H" and element2 == "N"): distance = 1.633
    
        if (element1 == "C" and element2 == "F") or (element1 == "F" and element2 == "C"): distance = 1.399
        if (element1 == "C" and element2 == "CL") or (element1 == "CL" and element2 == "C"): distance = 1.790
        if (element1 == "C" and element2 == "BR") or (element1 == "BR" and element2 == "C"): distance = 1.910
        if (element1 == "C" and element2 == "I") or (element1 == "I" and element2 == "C"): distance=2.162
    
        if (element1 == "S" and element2 == "BR") or (element1 == "BR" and element2 == "S"): distance = 2.321
        if (element1 == "S" and element2 == "CL") or (element1 == "CL" and element2 == "S"): distance = 2.283
        if (element1 == "S" and element2 == "F") or (element1 == "F" and element2 == "S"): distance = 1.640
        if (element1 == "S" and element2 == "I") or (element1 == "I" and element2 == "S"): distance= 2.687
    
        if (element1 == "P" and element2 == "BR") or (element1 == "BR" and element2 == "P"): distance = 2.366
        if (element1 == "P" and element2 == "CL") or (element1 == "CL" and element2 == "P"): distance = 2.008
        if (element1 == "P" and element2 == "F") or (element1 == "F" and element2 == "P"): distance = 1.495
        if (element1 == "P" and element2 == "I") or (element1 == "I" and element2 == "P"): distance= 2.490
        if (element1 == "P" and element2 == "O") or (element1 == "O" and element2 == "P"): distance= 1.6 # estimate based on eye balling Handbook of Chemistry and Physics
    
        if (element1 == "N" and element2 == "BR") or (element1 == "BR" and element2 == "N"): distance = 1.843
        if (element1 == "N" and element2 == "CL") or (element1 == "CL" and element2 == "N"): distance = 1.743
        if (element1 == "N" and element2 == "F") or (element1 == "F" and element2 == "N"): distance = 1.406
        if (element1 == "N" and element2 == "I") or (element1 == "I" and element2 == "N"): distance= 2.2
    
        if (element1 == "SI" and element2 == "BR") or (element1 == "BR" and element2 == "SI"): distance = 2.284
        if (element1 == "SI" and element2 == "CL") or (element1 == "CL" and element2 == "SI"): distance = 2.072
        if (element1 == "SI" and element2 == "F") or (element1 == "F" and element2 == "SI"): distance = 1.636
        if (element1 == "SI" and element2 == "P") or (element1 == "P" and element2 == "SI"): distance= 2.264
        if (element1 == "SI" and element2 == "S") or (element1 == "S" and element2 == "SI"): distance= 2.145
        if (element1 == "SI" and element2 == "SI") or (element1 == "SI" and element2 == "SI"): distance= 2.359
        if (element1 == "SI" and element2 == "C") or (element1 == "C" and element2 == "SI"): distance= 1.888
        if (element1 == "SI" and element2 == "N") or (element1 == "N" and element2 == "SI"): distance= 1.743
        if (element1 == "SI" and element2 == "O") or (element1 == "O" and element2 == "SI"): distance= 1.631
        
        return distance;
    
    # Functions to identify positive charges
    # ======================================
    
    def assign_charges(self):
        # Get all the quartinary amines on non-protein residues (these are the only non-protein groups that will be identified as positively charged)
        AllCharged = []
        for atom_index in self.NonProteinAtoms:
            atom = self.NonProteinAtoms[atom_index]
            if atom.element == "MG" or atom.element == "MN" or atom.element == "RH" or atom.element == "ZN" or atom.element == "FE" or atom.element == "BI" or atom.element == "AS" or atom.element == "AG":
                    chrg = self.charged(atom.coordinates, [atom_index], True)
                    self.charges.append(chrg)
            
            if atom.element == "N":
                if atom.NumberOfNeighbors() == 4: # a quartinary amine, so it's easy
                    indexes = [atom_index]
                    indexes.extend(atom.IndeciesOfAtomsConnecting) 
                    chrg = self.charged(atom.coordinates, indexes, True) # so the indicies stored is just the index of the nitrogen and any attached atoms
                    self.charges.append(chrg)
                elif atom.NumberOfNeighbors() == 3: # maybe you only have two hydrogen's added, by they're sp3 hybridized. Just count this as a quartinary amine, since I think the positive charge would be stabalized.
                    nitrogen = atom
                    atom1 = self.AllAtoms[atom.IndeciesOfAtomsConnecting[0]]
                    atom2 = self.AllAtoms[atom.IndeciesOfAtomsConnecting[1]]
                    atom3 = self.AllAtoms[atom.IndeciesOfAtomsConnecting[2]]
                    angle1 = self.functions.angle_between_three_points(atom1.coordinates, nitrogen.coordinates, atom2.coordinates) * 180.0 / math.pi
                    angle2 = self.functions.angle_between_three_points(atom1.coordinates, nitrogen.coordinates, atom3.coordinates) * 180.0 / math.pi
                    angle3 = self.functions.angle_between_three_points(atom2.coordinates, nitrogen.coordinates, atom3.coordinates) * 180.0 / math.pi
                    average_angle = (angle1 + angle2 + angle3) / 3
                    if math.fabs(average_angle - 109.0) < 5.0:
                        indexes = [atom_index]
                        indexes.extend(atom.IndeciesOfAtomsConnecting)
                        chrg = self.charged(nitrogen.coordinates, indexes, True) # so indexes added are the nitrogen and any attached atoms.
                        self.charges.append(chrg)
            
            if atom.element == "C": # let's check for guanidino-like groups (actually H2N-C-NH2, where not CN3.)
                if atom.NumberOfNeighbors() == 3: # the carbon has only three atoms connected to it
                    nitrogens = self.connected_atoms_of_given_element(atom_index,"N")
                    if len(nitrogens) >= 2: # so carbon is connected to at least two nitrogens
                        # now we need to count the number of nitrogens that are only connected to one heavy atom (the carbon)
                        nitrogens_to_use = []
                        all_connected = atom.IndeciesOfAtomsConnecting[:]
                        not_isolated = -1
                        
                        for atmindex in nitrogens:
                            if len(self.connected_heavy_atoms(atmindex)) == 1:
                                nitrogens_to_use.append(atmindex)
                                all_connected.remove(atmindex)
                            
                        if len(all_connected) > 0: not_isolated = all_connected[0] # get the atom that connects this charged group to the rest of the molecule, ultimately to make sure it's sp3 hybridized

                        if len(nitrogens_to_use) == 2 and not_isolated != -1: # so there are at two nitrogens that are only connected to the carbon (and probably some hydrogens)

                            # now you need to make sure not_isolated atom is sp3 hybridized
                            not_isolated_atom = self.AllAtoms[not_isolated]
                            if (not_isolated_atom.element == "C" and not_isolated_atom.NumberOfNeighbors()==4) or (not_isolated_atom.element == "O" and not_isolated_atom.NumberOfNeighbors()==2) or not_isolated_atom.element == "N" or not_isolated_atom.element == "S" or not_isolated_atom.element == "P":
                            
                                pt = self.AllAtoms[nitrogens_to_use[0]].coordinates.copy_of()
                                pt.x = pt.x + self.AllAtoms[nitrogens_to_use[1]].coordinates.x
                                pt.y = pt.y + self.AllAtoms[nitrogens_to_use[1]].coordinates.y
                                pt.z = pt.z + self.AllAtoms[nitrogens_to_use[1]].coordinates.z
                                pt.x = pt.x / 2.0
                                pt.y = pt.y / 2.0
                                pt.z = pt.z / 2.0
                                
                                indexes = [atom_index]
                                indexes.extend(nitrogens_to_use)
                                indexes.extend(self.connected_atoms_of_given_element(nitrogens_to_use[0],"H"))
                                indexes.extend(self.connected_atoms_of_given_element(nitrogens_to_use[1],"H"))
                                
                                chrg = self.charged(pt, indexes, True) # True because it's positive
                                self.charges.append(chrg)
            
            if atom.element == "C": # let's check for a carboxylate
                if atom.NumberOfNeighbors() == 3: # a carboxylate carbon will have three items connected to it.
                    oxygens = self.connected_atoms_of_given_element(atom_index,"O")
                    if len(oxygens) == 2: # a carboxylate will have two oxygens connected to it.
                        # now, each of the oxygens should be connected to only one heavy atom (so if it's connected to a hydrogen, that's okay)
                        if len(self.connected_heavy_atoms(oxygens[0])) == 1 and len(self.connected_heavy_atoms(oxygens[1])) == 1:
                            # so it's a carboxylate! Add a negative charge.
                            pt = self.AllAtoms[oxygens[0]].coordinates.copy_of()
                            pt.x = pt.x + self.AllAtoms[oxygens[1]].coordinates.x
                            pt.y = pt.y + self.AllAtoms[oxygens[1]].coordinates.y
                            pt.z = pt.z + self.AllAtoms[oxygens[1]].coordinates.z
                            pt.x = pt.x / 2.0
                            pt.y = pt.y / 2.0
                            pt.z = pt.z / 2.0
                            chrg = self.charged(pt, [oxygens[0], atom_index, oxygens[1]], False)
                            self.charges.append(chrg)
            
            if atom.element == "P": # let's check for a phosphate or anything where a phosphorus is bound to two oxygens where both oxygens are bound to only one heavy atom (the phosphorus). I think this will get several phosphorus substances.
                oxygens = self.connected_atoms_of_given_element(atom_index,"O")
                if len(oxygens) >=2: # the phosphorus is bound to at least two oxygens
                    # now count the number of oxygens that are only bound to the phosphorus
                    count = 0
                    for oxygen_index in oxygens:
                        if len(self.connected_heavy_atoms(oxygen_index)) == 1: count = count + 1
                    if count >=2: # so there are at least two oxygens that are only bound to the phosphorus
                        indexes = [atom_index]
                        indexes.extend(oxygens)
                        chrg = self.charged(atom.coordinates, indexes, False)
                        self.charges.append(chrg)
            
            if atom.element == "S": # let's check for a sulfonate or anything where a sulfur is bound to at least three oxygens and at least three are bound to only the sulfur (or the sulfur and a hydrogen).
                oxygens = self.connected_atoms_of_given_element(atom_index,"O")
                if len(oxygens) >=3: # the sulfur is bound to at least three oxygens
                    # now count the number of oxygens that are only bound to the sulfur
                    count = 0
                    for oxygen_index in oxygens:
                        if len(self.connected_heavy_atoms(oxygen_index)) == 1: count = count + 1
                    if count >=3: # so there are at least three oxygens that are only bound to the sulfur
                        indexes = [atom_index]
                        indexes.extend(oxygens)
                        chrg = self.charged(atom.coordinates, indexes, False)
                        self.charges.append(chrg)
            
        # Now that you've found all the positive charges in non-protein residues, it's time to look for aromatic rings in protein residues
        curr_res = ""
        first = True
        residue = []
        
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            
            key = atom.residue + "_" + str(atom.resid) + "_" + atom.chain
            
            if first == True:
                curr_res = key
                first = False
                
            if key != curr_res: 

                self.assign_charged_from_protein_process_residue(residue, last_key)
                
                residue = []
                curr_res = key
            
            residue.append(atom_index)
            last_key = key
        
        self.assign_charged_from_protein_process_residue(residue, last_key)

    def assign_charged_from_protein_process_residue(self, residue, last_key): 
        temp = last_key.strip().split("_")
        resname = temp[0]
        real_resname = resname[-3:]
        resid = temp[1]
        chain = temp[2]

        if real_resname == "LYS" or real_resname == "LYN": # regardless of protonation state, assume it's charged.
            for index in residue: 
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "NZ":
                    
                    # quickly go through the residue and get the hydrogens attached to this nitrogen to include in the index list
                    indexes = [index]
                    for index2 in residue:
                        atom2 = self.AllAtoms[index2]
                        if atom2.atomname.strip() == "HZ1": indexes.append(index2)
                        if atom2.atomname.strip() == "HZ2": indexes.append(index2)
                        if atom2.atomname.strip() == "HZ3": indexes.append(index2)
                    
                    chrg = self.charged(atom.coordinates, indexes, True)
                    self.charges.append(chrg)
		    break

        if real_resname == "ARG":
	    charge_pt = point(0.0,0.0,0.0)
            count = 0.0
            indices = []
            for index in residue: 
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "NH1": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
                if atom.atomname.strip() == "NH2": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
                if atom.atomname.strip() == "2HH2": indices.append(index)
                if atom.atomname.strip() == "1HH2": indices.append(index)
                if atom.atomname.strip() == "CZ": indices.append(index)
                if atom.atomname.strip() == "2HH1": indices.append(index)
                if atom.atomname.strip() == "1HH1": indices.append(index)
                
	    if count != 0.0:
                
                charge_pt.x = charge_pt.x / count
                charge_pt.y = charge_pt.y / count
                charge_pt.z = charge_pt.z / count
                
                if charge_pt.x != 0.0 or charge_pt.y != 0.0 or charge_pt.z != 0.0:
                    chrg = self.charged(charge_pt, indices, True)
                    self.charges.append(chrg)

        if real_resname == "HIS" or real_resname == "HID" or real_resname == "HIE" or real_resname == "HIP": # regardless of protonation state, assume it's charged. This based on "The Cation-Pi Interaction," which suggests protonated state would be stabalized. But let's not consider HIS when doing salt bridges.
	    charge_pt = point(0.0,0.0,0.0)
            count = 0.0
            indices = []
            for index in residue: 
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "NE2": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
		if atom.atomname.strip() == "ND1": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
                if atom.atomname.strip() == "HE2": indices.append(index)
                if atom.atomname.strip() == "HD1": indices.append(index)
                if atom.atomname.strip() == "CE1": indices.append(index)
                if atom.atomname.strip() == "CD2": indices.append(index)
                if atom.atomname.strip() == "CG": indices.append(index)

            if count != 0.0:
                charge_pt.x = charge_pt.x / count
                charge_pt.y = charge_pt.y / count
                charge_pt.z = charge_pt.z / count
                if charge_pt.x != 0.0 or charge_pt.y != 0.0 or charge_pt.z != 0.0:
                    chrg = self.charged(charge_pt, indices, True)
                    self.charges.append(chrg)
    
        if real_resname == "GLU" or real_resname == "GLH" or real_resname == "GLX": # regardless of protonation state, assume it's charged. This based on "The Cation-Pi Interaction," which suggests protonated state would be stabalized.
	    charge_pt = point(0.0,0.0,0.0)
            count = 0.0
            indices = []
            for index in residue: 
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "OE1": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
		if atom.atomname.strip() == "OE2": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
                if atom.atomname.strip() == "CD": indices.append(index)

            if count != 0.0:
                charge_pt.x = charge_pt.x / count
                charge_pt.y = charge_pt.y / count
                charge_pt.z = charge_pt.z / count
                if charge_pt.x != 0.0 or charge_pt.y != 0.0 or charge_pt.z != 0.0:
                    chrg = self.charged(charge_pt, indices, False) # False because it's a negative charge
                    self.charges.append(chrg)
    
        if real_resname == "ASP" or real_resname == "ASH" or real_resname == "ASX": # regardless of protonation state, assume it's charged. This based on "The Cation-Pi Interaction," which suggests protonated state would be stabalized.
	    charge_pt = point(0.0,0.0,0.0)
            count = 0.0
            indices = []
            for index in residue: 
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "OD1": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
		if atom.atomname.strip() == "OD2": 
		    charge_pt.x = charge_pt.x + atom.coordinates.x
		    charge_pt.y = charge_pt.y + atom.coordinates.y
		    charge_pt.z = charge_pt.z + atom.coordinates.z
                    indices.append(index)
                    count = count + 1.0
                if atom.atomname.strip() == "CG": indices.append(index)

            if count != 0.0:
                charge_pt.x = charge_pt.x / count
                charge_pt.y = charge_pt.y / count
                charge_pt.z = charge_pt.z / count
                if charge_pt.x != 0.0 or charge_pt.y != 0.0 or charge_pt.z != 0.0:
                    chrg = self.charged(charge_pt, indices, False) # False because it's a negative charge
                    self.charges.append(chrg)
    
    class charged():
        def __init__(self, coordinates, indices, positive):
            self.coordinates = coordinates
            self.indices = indices
            self.positive = positive # true or false to specifiy if positive or negative charge

    # Functions to identify aromatic rings
    # ====================================

    def add_aromatic_marker(self, indicies_of_ring):
        # first identify the center point
        points_list = []
        total = len(indicies_of_ring)
        x_sum = 0.0
        y_sum = 0.0
        z_sum = 0.0
        
        for index in indicies_of_ring:
            atom = self.AllAtoms[index]
            points_list.append(atom.coordinates)
            x_sum = x_sum + atom.coordinates.x
            y_sum = y_sum + atom.coordinates.y
            z_sum = z_sum + atom.coordinates.z
        
        if total == 0: return # to prevent errors in some cases
        
        center = point(x_sum / total, y_sum / total, z_sum / total)
 
        # now get the radius of the aromatic ring
        radius = 0.0
        for index in indicies_of_ring:
            atom = self.AllAtoms[index]
            dist = center.dist_to(atom.coordinates)
            if dist > radius: radius = dist
            
        # now get the plane that defines this ring
        if len(indicies_of_ring) < 3:
            return # to prevent an error in some cases. If there aren't three point, you can't define a plane
        elif len(indicies_of_ring) == 3:
            A = self.AllAtoms[indicies_of_ring[0]].coordinates
            B = self.AllAtoms[indicies_of_ring[1]].coordinates
            C = self.AllAtoms[indicies_of_ring[2]].coordinates
        elif len(indicies_of_ring) == 4:
            A = self.AllAtoms[indicies_of_ring[0]].coordinates
            B = self.AllAtoms[indicies_of_ring[1]].coordinates
            C = self.AllAtoms[indicies_of_ring[3]].coordinates
        else: # best, for 5 and 6 member rings
            A = self.AllAtoms[indicies_of_ring[0]].coordinates
            B = self.AllAtoms[indicies_of_ring[2]].coordinates
            C = self.AllAtoms[indicies_of_ring[4]].coordinates
        
        AB = self.functions.vector_subtraction(B,A)
        AC = self.functions.vector_subtraction(C,A)
        ABXAC = self.functions.CrossProduct(AB,AC)
        
        # formula for plane will be ax + by + cz = d
        x1 = self.AllAtoms[indicies_of_ring[0]].coordinates.x
        y1 = self.AllAtoms[indicies_of_ring[0]].coordinates.y
        z1 = self.AllAtoms[indicies_of_ring[0]].coordinates.z
        
        a = ABXAC.x
        b = ABXAC.y
        c = ABXAC.z
        d = a*x1 + b*y1 + c*z1
        
        ar_ring = self.aromatic_ring(center, indicies_of_ring, [a,b,c,d], radius)
        self.aromatic_rings.append(ar_ring)
                
    class aromatic_ring():
        def __init__(self, center, indices, plane_coeff, radius):
            self.center = center
            self.indices = indices
            self.plane_coeff = plane_coeff # a*x + b*y + c*z = dI think that
            self.radius = radius

    def assign_aromatic_rings(self):
        # Get all the rings containing each of the atoms in the ligand
        AllRings = []
        for atom_index in self.NonProteinAtoms:
            AllRings.extend(self.all_rings_containing_atom(atom_index))
        
        for ring_index_1 in range(len(AllRings)):
            ring1 = AllRings[ring_index_1]
            if len(ring1) != 0:
                for ring_index_2 in range(len(AllRings)):
                    if ring_index_1 != ring_index_2:
                        ring2 = AllRings[ring_index_2]
                        if len(ring2) != 0:
                            if self.set1_is_subset_of_set2(ring1, ring2) == True: AllRings[ring_index_2] = []

        while [] in AllRings: AllRings.remove([])
        
        # Now we need to figure out which of these ligands are aromatic (planar)
        
        for ring_index in range(len(AllRings)):
            ring = AllRings[ring_index]
            is_flat = True
            for t in range(-3, len(ring)-3):
                pt1 = self.NonProteinAtoms[ring[t]].coordinates
                pt2 = self.NonProteinAtoms[ring[t+1]].coordinates
                pt3 = self.NonProteinAtoms[ring[t+2]].coordinates
                pt4 = self.NonProteinAtoms[ring[t+3]].coordinates
                
                # first, let's see if the last atom in this ring is a carbon connected to four atoms. That would be a quick way of telling this is not an aromatic ring
                cur_atom = self.NonProteinAtoms[ring[t+3]]
                if cur_atom.element == "C" and cur_atom.NumberOfNeighbors() == 4:
                    is_flat = False
                    break
                
                # now check the dihedral between the ring atoms to see if it's flat
                angle = self.functions.dihedral(pt1, pt2, pt3, pt4) * 180 / math.pi
                if (angle > -165 and angle < -15) or (angle > 15 and angle < 165): # 15 degress is the cutoff #, ring[t], ring[t+1], ring[t+2], ring[t+3] # range of this function is -pi to pi
                    is_flat = False
                    break

                # now check the dihedral between the ring atoms and an atom connected to the current atom to see if that's flat too.
                for substituent_atom_index in cur_atom.IndeciesOfAtomsConnecting:
                    pt_sub = self.NonProteinAtoms[substituent_atom_index].coordinates
                    angle = self.functions.dihedral(pt2, pt3, pt4, pt_sub) * 180 / math.pi
                    if (angle > -165 and angle < -15) or (angle > 15 and angle < 165): # 15 degress is the cutoff #, ring[t], ring[t+1], ring[t+2], ring[t+3] # range of this function is -pi to pi
                        is_flat = False
                        break

            if is_flat == False: AllRings[ring_index] = []
            if len(ring) < 5: AllRings[ring_index] = [] # While I'm at it, three and four member rings are not aromatic
            if len(ring) > 6: AllRings[ring_index] = [] # While I'm at it, if the ring has more than 6, also throw it out. So only 5 and 6 member rings are allowed.



        while [] in AllRings: AllRings.remove([])
        
        for ring in AllRings:
            self.add_aromatic_marker(ring)
            
        # Now that you've found all the rings in non-protein residues, it's time to look for aromatic rings in protein residues
        curr_res = ""
        first = True
        residue = []
        
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            
            key = atom.residue + "_" + str(atom.resid) + "_" + atom.chain
            
            if first == True:
                curr_res = key
                first = False
                
            if key != curr_res: 

                self.assign_aromatic_rings_from_protein_process_residue(residue, last_key)
                
                residue = []
                curr_res = key
            
            residue.append(atom_index)
            last_key = key
        
        self.assign_aromatic_rings_from_protein_process_residue(residue, last_key)

    def assign_aromatic_rings_from_protein_process_residue(self, residue, last_key): 
        temp = last_key.strip().split("_")
        resname = temp[0]
        real_resname = resname[-3:]
        resid = temp[1]
        chain = temp[2]

        if real_resname == "PHE":
            indicies_of_ring = []

            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CG": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CZ": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD2": indicies_of_ring.append(index)
                
            self.add_aromatic_marker(indicies_of_ring)

        if real_resname == "TYR": 
            indicies_of_ring = []

            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CG": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CZ": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD2": indicies_of_ring.append(index)
                
            self.add_aromatic_marker(indicies_of_ring)

        if real_resname == "HIS" or real_resname == "HID" or real_resname == "HIE" or real_resname == "HIP": 
            indicies_of_ring = []

            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CG": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "ND1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "NE2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD2": indicies_of_ring.append(index)
                
            self.add_aromatic_marker(indicies_of_ring)
        
        if real_resname == "TRP": 
            indicies_of_ring = []

            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CG": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "NE1": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD2": indicies_of_ring.append(index)
            
            self.add_aromatic_marker(indicies_of_ring)

            indicies_of_ring = []

            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CD2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CE3": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CZ3": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CH2": indicies_of_ring.append(index)
            for index in residue: # written this way because order is important
                atom = self.AllAtoms[index]
                if atom.atomname.strip() == "CZ2": indicies_of_ring.append(index)
                
            self.add_aromatic_marker(indicies_of_ring)
        
    def set1_is_subset_of_set2(self, set1, set2):
        is_subset = True
        for item in set1:
            if not item in set2:
                is_subset = False
                break
        return is_subset
            
    def all_rings_containing_atom(self, index):
        
        AllRings = []
        
        atom = self.AllAtoms[index]
        for conneceted_atom in atom.IndeciesOfAtomsConnecting:
            self.ring_recursive(conneceted_atom, [index], index, AllRings)
 
        return AllRings
            
    def ring_recursive(self, index, AlreadyCrossed, orig_atom, AllRings):

        if len(AlreadyCrossed) > 6: return # since you're only considering aromatic rings containing 5 or 6 members anyway, save yourself some time.

        atom = self.AllAtoms[index]

        temp = AlreadyCrossed[:]
        temp.append(index)

        for conneceted_atom in atom.IndeciesOfAtomsConnecting:
            if not conneceted_atom in AlreadyCrossed:
                self.ring_recursive(conneceted_atom, temp, orig_atom, AllRings)
            if conneceted_atom == orig_atom and orig_atom != AlreadyCrossed[-1]:
                AllRings.append(temp)
    
    # Functions to assign secondary structure to protein residues
    # ===========================================================
    
    def assign_secondary_structure(self):
        # first, we need to know what resid's are available
        resids = []
        last_key = "-99999_Z"
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            key = str(atom.resid) + "_" + atom.chain
            if key != last_key:
                last_key = key
                resids.append(last_key)
        
        structure = {}
        for resid in resids:
            structure[resid] = "OTHER"
        
        atoms = []
        
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            if atom.SideChainOrBackBone() == "BACKBONE":
                if len(atoms) < 8:
                    atoms.append(atom)
                else:
                    atoms.pop(0)
                    atoms.append(atom)
                
                    # now make sure the first four all have the same resid and the last four all have the same resid
                    if atoms[0].resid == atoms[1].resid and atoms[0].resid == atoms[2].resid and atoms[0].resid == atoms[3].resid and atoms[0] != atoms[4].resid and atoms[4].resid == atoms[5].resid and atoms[4].resid == atoms[6].resid and atoms[4].resid == atoms[7].resid and atoms[0].resid + 1 == atoms[7].resid and atoms[0].chain == atoms[7].chain:
                        resid1 = atoms[0].resid
                        resid2 = atoms[7].resid
                        
                        # Now give easier to use names to the atoms
                        for atom in atoms:
                            if atom.resid == resid1 and atom.atomname.strip() == "N": first_N = atom
                            if atom.resid == resid1 and atom.atomname.strip() == "C": first_C = atom
                            if atom.resid == resid1 and atom.atomname.strip() == "CA": first_CA = atom
                        
                            if atom.resid == resid2 and atom.atomname.strip() == "N": second_N = atom
                            if atom.resid == resid2 and atom.atomname.strip() == "C": second_C = atom
                            if atom.resid == resid2 and atom.atomname.strip() == "CA": second_CA = atom
                        
                        # Now compute the phi and psi dihedral angles
                        phi = self.functions.dihedral(first_C.coordinates, second_N.coordinates, second_CA.coordinates, second_C.coordinates) * 180.0 / math.pi
                        psi = self.functions.dihedral(first_N.coordinates, first_CA.coordinates, first_C.coordinates, second_N.coordinates) * 180.0 / math.pi

                        # Now use those angles to determine if it's alpha or beta
                        if phi > -145 and phi < -35 and psi > -70 and psi < 50:
                            key1 = str(first_C.resid) + "_" + first_C.chain
                            key2 = str(second_C.resid) + "_" + second_C.chain
                            structure[key1] = "ALPHA"
                            structure[key2] = "ALPHA"
                        if (phi >= -180 and phi < -40 and psi <= 180 and psi > 90) or (phi >= -180 and phi < -70 and psi <= -165): # beta. This gets some loops (by my eye), but it's the best I could do.
                            key1 = str(first_C.resid) + "_" + first_C.chain
                            key2 = str(second_C.resid) + "_" + second_C.chain
                            structure[key1] = "BETA"
                            structure[key2] = "BETA"
                
        # Now update each of the atoms with this structural information
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            key = str(atom.resid) + "_" + atom.chain
            atom.structure = structure[key]
            
        # Some more post processing. 
        CA_list = [] # first build a list of the indices of all the alpha carbons
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            if atom.residue.strip() in self.protein_resnames and atom.atomname.strip() == "CA": CA_list.append(atom_index)
            
        # some more post processing. 
        change = True
        while change == True:
            change = False
            
            # A residue of index i is only going to be in an alpha helix its CA is within 6 A of the CA of the residue i + 3
            for CA_atom_index in CA_list:
                CA_atom = self.AllAtoms[CA_atom_index]
                if CA_atom.structure == "ALPHA": # so it's in an alpha helix
                    another_alpha_is_close = False
                    for other_CA_atom_index in CA_list: # so now compare that CA to all the other CA's
                        other_CA_atom = self.AllAtoms[other_CA_atom_index]
                        if other_CA_atom.structure == "ALPHA": # so it's also in an alpha helix
                            if other_CA_atom.resid - 3 == CA_atom.resid or other_CA_atom.resid + 3 == CA_atom.resid: # so this CA atom is one of the ones the first atom might hydrogen bond with
                                if other_CA_atom.coordinates.dist_to(CA_atom.coordinates) < 6.0: # so these two CA atoms are close enough together that their residues are probably hydrogen bonded
                                    another_alpha_is_close = True
                                    break
                    if another_alpha_is_close == False:
                        self.set_structure_of_residue(CA_atom.chain, CA_atom.resid, "OTHER")
                        change = True

            # Alpha helices are only alpha helices if they span at least 4 residues (to wrap around and hydrogen bond). I'm going to require them to span at least 5 residues, based on examination of many structures.
            for index_in_list in range(len(CA_list)-5): 
                
                index_in_pdb1 = CA_list[index_in_list]
                index_in_pdb2 = CA_list[index_in_list+1]
                index_in_pdb3 = CA_list[index_in_list+2]
                index_in_pdb4 = CA_list[index_in_list+3]
                index_in_pdb5 = CA_list[index_in_list+4]
                index_in_pdb6 = CA_list[index_in_list+5]

                atom1 = self.AllAtoms[index_in_pdb1]
                atom2 = self.AllAtoms[index_in_pdb2]
                atom3 = self.AllAtoms[index_in_pdb3]
                atom4 = self.AllAtoms[index_in_pdb4]
                atom5 = self.AllAtoms[index_in_pdb5]
                atom6 = self.AllAtoms[index_in_pdb6]
                
                if atom1.resid + 1 == atom2.resid and atom2.resid + 1 == atom3.resid and atom3.resid + 1 == atom4.resid and atom4.resid + 1 == atom5.resid and atom5.resid + 1 == atom6.resid: # so they are sequential
                    
                    if atom1.structure != "ALPHA" and atom2.structure == "ALPHA" and atom3.structure != "ALPHA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        change = True
                    if atom2.structure != "ALPHA" and atom3.structure == "ALPHA" and atom4.structure != "ALPHA":
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        change = True
                    if atom3.structure != "ALPHA" and atom4.structure == "ALPHA" and atom5.structure != "ALPHA":
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        change = True
                    if atom4.structure != "ALPHA" and atom5.structure == "ALPHA" and atom6.structure != "ALPHA":
                        self.set_structure_of_residue(atom5.chain, atom5.resid, "OTHER")
                        change = True
                        
                    if atom1.structure != "ALPHA" and atom2.structure == "ALPHA" and atom3.structure == "ALPHA" and atom4.structure != "ALPHA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        change = True
                    if atom2.structure != "ALPHA" and atom3.structure == "ALPHA" and atom4.structure == "ALPHA" and atom5.structure != "ALPHA":
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        change = True
                    if atom3.structure != "ALPHA" and atom4.structure == "ALPHA" and atom5.structure == "ALPHA" and atom6.structure != "ALPHA":
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        self.set_structure_of_residue(atom5.chain, atom5.resid, "OTHER")
                        change = True

                    if atom1.structure != "ALPHA" and atom2.structure == "ALPHA" and atom3.structure == "ALPHA" and atom4.structure == "ALPHA" and atom5.structure != "ALPHA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        change = True
                    if atom2.structure != "ALPHA" and atom3.structure == "ALPHA" and atom4.structure == "ALPHA" and atom5.structure == "ALPHA" and atom6.structure != "ALPHA":
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        self.set_structure_of_residue(atom5.chain, atom5.resid, "OTHER")
                        change = True

                    if atom1.structure != "ALPHA" and atom2.structure == "ALPHA" and atom3.structure == "ALPHA" and atom4.structure == "ALPHA" and atom5.structure == "ALPHA" and atom6.structure != "ALPHA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        self.set_structure_of_residue(atom4.chain, atom4.resid, "OTHER")
                        self.set_structure_of_residue(atom5.chain, atom5.resid, "OTHER")
                        change = True

            # now go through each of the BETA CA atoms. A residue is only going to be called a beta sheet if CA atom is within 6.0 A of another CA beta, same chain, but index difference > 2.
            for CA_atom_index in CA_list:
                CA_atom = self.AllAtoms[CA_atom_index]
                if CA_atom.structure == "BETA": # so it's in a beta sheet
                    another_beta_is_close = False
                    for other_CA_atom_index in CA_list:
                        if other_CA_atom_index != CA_atom_index: # so not comparing an atom to itself
                            other_CA_atom = self.AllAtoms[other_CA_atom_index]
                            if other_CA_atom.structure == "BETA": # so you're comparing it only to other BETA-sheet atoms
                                if other_CA_atom.chain == CA_atom.chain: # so require them to be on the same chain. needed to indecies can be fairly compared
                                    if math.fabs(other_CA_atom.resid - CA_atom.resid) > 2: # so the two residues are not simply adjacent to each other on the chain
                                        if CA_atom.coordinates.dist_to(other_CA_atom.coordinates) < 6.0: # so these to atoms are close to each other
                                            another_beta_is_close = True
                                            break
                    if another_beta_is_close == False:
                        self.set_structure_of_residue(CA_atom.chain, CA_atom.resid, "OTHER")
                        change = True
                
            # Now some more post-processing needs to be done. Do this again to clear up mess that may have just been created (single residue beta strand, for example)
            # Beta sheets are usually at least 3 residues long
            
            for index_in_list in range(len(CA_list)-3):
                
                index_in_pdb1 = CA_list[index_in_list]
                index_in_pdb2 = CA_list[index_in_list+1]
                index_in_pdb3 = CA_list[index_in_list+2]
                index_in_pdb4 = CA_list[index_in_list+3]
                
                atom1 = self.AllAtoms[index_in_pdb1]
                atom2 = self.AllAtoms[index_in_pdb2]
                atom3 = self.AllAtoms[index_in_pdb3]
                atom4 = self.AllAtoms[index_in_pdb4]
                
                if atom1.resid + 1 == atom2.resid and atom2.resid + 1 == atom3.resid and atom3.resid + 1 == atom4.resid: # so they are sequential
                    
                    if atom1.structure != "BETA" and atom2.structure == "BETA" and atom3.structure != "BETA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        change = True
                    if atom2.structure != "BETA" and atom3.structure == "BETA" and atom4.structure != "BETA":
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        change = True
                    if atom1.structure != "BETA" and atom2.structure == "BETA" and atom3.structure == "BETA" and atom4.structure != "BETA":
                        self.set_structure_of_residue(atom2.chain, atom2.resid, "OTHER")
                        self.set_structure_of_residue(atom3.chain, atom3.resid, "OTHER")
                        change = True
            
    def set_structure_of_residue(self, chain, resid, structure):
        for atom_index in self.AllAtoms:
            atom = self.AllAtoms[atom_index]
            if atom.chain == chain and atom.resid == resid:
                atom.structure = structure

class MathFunctions:
    
    def planrity(self, point1, point2, point3, point4):
    
            x1 = point1.x
            y1 = point1.y
            z1 = point1.z
            x2 = point2.x
            y2 = point2.y
            z2 = point2.z
            x3 = point3.x
            y3 = point3.y
            z3 = point3.z
            x4 = point4.x
            y4 = point4.y
            z4 = point4.z
    
    
            A = (y1*(z2-z3))+(y2*(z3-z1))+(y3*(z1-z2))
            B = (z1*(x2-x3))+(z2*(x3-x1))+(z3*(x1-x2))
            C = (x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2))
            D = ((-x1)*((y2*z3)-(y3*z2)))+((-x2)*((y3*z1)-(y1*z3)))+((-x3)*((y1*z2)-(y2*z1)))
            distance=(math.fabs((A*x4)+(B*y4)+(C*z4)+D))/(math.sqrt(math.pow(A,2) + math.pow(B,2) + math.pow(C,2)))
            
            A1 = (y1*(z2-z4))+(y2*(z4-z1))+(y4*(z1-z2))
            B1 = (z1*(x2-x4))+(z2*(x4-x1))+(z4*(x1-x2))
            C1 = (x1*(y2-y4))+(x2*(y4-y1))+(x4*(y1-y2))
            D1 = ((-x1)*((y2*z4)-(y4*z2)))+((-x2)*((y4*z1)-(y1*z4)))+((-x4)*((y1*z2)-(y2*z1)))
            distance1=(math.fabs((A1*x3)+(B1*y3)+(C1*z3)+D1))/(math.sqrt(math.pow(A1,2) + math.pow(B1,2) + math.pow(C1,2)))
            
            A2 = (y1*(z4-z3))+(y4*(z3-z1))+(y3*(z1-z4))
            B2 = (z1*(x4-x3))+(z4*(x3-x1))+(z3*(x1-x4))
            C2 = (x1*(y4-y3))+(x4*(y3-y1))+(x3*(y1-y4))
            D2 = ((-x1)*((y4*z3)-(y3*z4)))+((-x4)*((y3*z1)-(y1*z3)))+((-x3)*((y1*z4)-(y4*z1)))
            distance2=(math.fabs((A2*x2)+(B2*y2)+(C2*z2)+D2))/(math.sqrt(math.pow(A2,2) + math.pow(B2,2) + math.pow(C2,2)))
            
            A3 = (y4*(z2-z3))+(y2*(z3-z4))+(y3*(z4-z2))
            B3 = (z4*(x2-x3))+(z2*(x3-x4))+(z3*(x4-x2))
            C3 = (x4*(y2-y3))+(x2*(y3-y4))+(x3*(y4-y2))
            D3 = ((-x4)*((y2*z3)-(y3*z2)))+((-x2)*((y3*z4)-(y4*z3)))+((-x3)*((y4*z2)-(y2*z4)))
            distance3=(math.fabs((A3*x1)+(B3*y1)+(C3*z1)+D3))/(math.sqrt(math.pow(A3,2) + math.pow(B3,2) + math.pow(C3,2)))
    
            final_dist = -1
    
            if (distance < distance1 and distance < distance2 and distance < distance3):
                    final_dist = distance
            elif (distance1 < distance and distance1 < distance2 and distance1 < distance3):
                    final_dist = distance1
            elif (distance2 < distance and distance2 < distance1 and distance2 < distance3):
                    final_dist = distance2
            elif (distance3 < distance and distance3 < distance1 and distance3 < distance2):
                    final_dist = distance3
    
            # Now normalize by the length of the longest bond
    
            return final_dist

    def vector_subtraction(self, vector1, vector2): # vector1 - vector2
        return point(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
    
    def CrossProduct(self, Pt1, Pt2): # never tested
        Response = point(0,0,0)
    
        Response.x = Pt1.y * Pt2.z - Pt1.z * Pt2.y
        Response.y = Pt1.z * Pt2.x - Pt1.x * Pt2.z
        Response.z = Pt1.x * Pt2.y - Pt1.y * Pt2.x
    
        return Response;
    
    def vector_scalar_multiply(self, vector, scalar):
        return point(vector.x * scalar, vector.y * scalar, vector.z * scalar)
    
    def dot_product(self, point1, point2):
        return point1.x * point2.x + point1.y * point2.y + point1.z * point2.z
    
    def dihedral(self, point1, point2, point3, point4): # never tested
    
        b1 = self.vector_subtraction(point2, point1)
        b2 = self.vector_subtraction(point3, point2)
        b3 = self.vector_subtraction(point4, point3)
    
        b2Xb3 = self.CrossProduct(b2,b3)
        b1Xb2 = self.CrossProduct(b1,b2)
    
        b1XMagb2 = self.vector_scalar_multiply(b1,b2.Magnitude())
        radians = math.atan2(self.dot_product(b1XMagb2,b2Xb3), self.dot_product(b1Xb2,b2Xb3))
        return radians
    
    def angle_between_three_points(self, point1, point2, point3): # As in three connected atoms
        vector1 = self.vector_subtraction(point1, point2)
        vector2 = self.vector_subtraction(point3, point2)
        return self.angle_between_points(vector1, vector2)
    
    def angle_between_points(self, point1, point2):
        new_point1 = self.return_normalized_vector(point1)
        new_point2 = self.return_normalized_vector(point2)
        dot_prod = self.dot_product(new_point1, new_point2)
        if dot_prod > 1.0: dot_prod = 1.0 # to prevent errors that can rarely occur
        if dot_prod < -1.0: dot_prod = -1.0
        return math.acos(dot_prod)
    
    def return_normalized_vector(self, vector):
        dist = self.distance(point(0,0,0), vector)
        return point(vector.x/dist, vector.y/dist, vector.z/dist)
    
    def distance(self, point1, point2):
        deltax = point1.x - point2.x
        deltay = point1.y - point2.y
        deltaz = point1.z - point2.z
    
        return math.sqrt(math.pow(deltax,2) + math.pow(deltay,2) + math.pow(deltaz,2))
        
    def project_point_onto_plane(self, apoint, plane_coefficients): # essentially finds the point on the plane that is closest to the specified point
        # the plane_coefficients are [a,b,c,d], where the plane is ax + by + cz = d

        # First, define a plane using cooeficients a, b, c, d such that ax + by + cz = d
        a = plane_coefficients[0]
        b = plane_coefficients[1]
        c = plane_coefficients[2]
        d = plane_coefficients[3]
        
        # Now, define a point in space (s,u,v)
        s = apoint.x
        u = apoint.y
        v = apoint.z
        
        # the formula of a line perpendicular to the plan passing through (s,u,v) is:
        #x = s + at
        #y = u + bt
        #z = v + ct
        
        t = (d - a*s - b*u - c*v) / (a*a + b*b + c*c)
        
        # here's the point closest on the plane
        x = s + a*t
        y = u + b*t
        z = v + c*t
        
        return point(x,y,z)
    def centroid(self, *points):
        (x, y, z) = (0.0,0.0,0.0)
        point_num = len(points)
        if point_num == 0: return None
        for p in points:
            x += p.x
            y += p.y
            z += p.z
        return point(x/point_num, y/ point_num, z/point_num )
    def center_of_mass(self,*atoms):
        (x, y, z) = (0.0,0.0,0.0)
        totmass = 0.0
        for a in atoms:
            m = PeriodicTable.atomic_mass[a.element]
            x += a.coordinates.x * m
            y += a.coordinates.y * m
            z += a.coordinates.z * m
            totmass += m
        return point(x/totmass, y/ totmass, z/totmass)

class Interaction:
    '''Initialized by a ligand atom (Atom class) and a receptor atom (Atom class), optionally a pre-computed distance'''
    def __init__(self,interaction_type, ligand_atom, receptor_atom, distance=0.0):
        self._type = interaction_type
        self._ligand_atom = ligand_atom
        self._receptor_atom  = receptor_atom
        if distance == 0.0: distance = ligand_atom.coordinates.dist_to(receptor_atom.coordinates)
        self._distance = distance
    def __getattr__(self,name):
        name = "_" + name
        return self.__dict__[name]

    def __str__(self):
        return "{%15s, %s, %s}" % (self._type, self._ligand_atom.PDBIndex, self._receptor_atom.PDBIndex)

class HydrophobicInteraction(Interaction):
    def __init__(self, ligand_atom, receptor_atom, hydrophobic_key=''):
        super(HydrophobicInteraction,self).__init__('hydrophobic',ligand_atom, receptor_atom)
        self.hydrophobic_key = hydrophobic_key
    def affinity(self):
        '''free energy contribution of this specific interaction, might depends on temperature'''
        pass
class ElectrostaticInteraction(Interaction):
    def __init__(self, ligand_atom, receptor_atom,coulomb_energy = 0.0):
        super(ElectrostaticInteraction,self).__init__('electrostatic',ligand_atom, receptor_atom)
        self._coulomb_energy = coulomb_energy 
        self._eval_coulomb_energy()
    def _eval_coulomb_energy(self):
        if self._coulomb_energy == 0.0:
            self._coulomb_energy = (self.ligand_atom.charge * self.receptor_atom.charge / self.distance) * 138.94238460104697e4 # to convert into J/mol # might be nice to double check this
        return self._coulomb_energy 

class CloseContact(Interaction):
    def __init__(self,ligand_atom,receptor_atom):
        super(CloseContact,self).__init__('closecontact',ligand_atom,receptor_atom)

class HydrogenBond(Interaction):
    def __init__(self,ligand_atom, receptor_atom,hbonds_key='', angle = 999.9):
        super(HydrogenBond, self).__init__('hydrogen',ligand_atom, receptor_atom)
        self.hbonds_key = hbonds_key
        if angle == 999.9:
            # print 'recalculating angle...'
            angle = math.fabs(180 - functions.angle_between_three_points(ligand_atom.coordinates, hydrogen.coordinates, receptor_atom.coordinates) * 180.0 / math.pi) 
        self._angle = angle
    def __getattr__(self,name):
        name = "_" + name
        return self.__dict__[name]

class Interactions:
    functions = MathFunctions()
    
    # supporting functions
    def list_alphebetize_and_combine(self, list):
        list.sort()
        return '_'.join(list)

    def hashtable_entry_add_one(self, hashtable, key, toadd = 1): # note that dictionaries (hashtables) are passed by reference in python
        if hashtable.has_key(key):
            hashtable[key] = hashtable[key] + toadd
        else:
            hashtable[key] = toadd

    def center(self, string, length):
        while len(string) < length:
            string = " " + string
            if len(string) < length:
                string = string + " "
        return string

    # The meat of the class
    def __len__(self):
        return len(self.interactions)
    def __init__(self, ligand_pdbqt_filename, receptor_pdbqt_filename, parameters):
        
        self.ligand = PDB()
        self.ligand.LoadPDB(ligand_pdbqt_filename)
        
        self.receptor = PDB()
        self.receptor.LoadPDB(receptor_pdbqt_filename)
        self.receptor_pdbqt_filename = receptor_pdbqt_filename # retain information of input receptor filename for later use
        self.receptor.assign_secondary_structure()

        self.binding_energy = self._get_binding_energy(ligand_pdbqt_filename)
        self.interactions = []  # list of all Interaction objects 
        self._distance_matrix = {} # accessed by distance_matrix[ligand_atom_index][receptor_atom_index]
        #   self._ligand_receptor_atom_type_pairs_less_than_two_half = {}
        #   self._ligand_receptor_atom_type_pairs_less_than_four = {}
        #   self._ligand_receptor_atom_type_pairs_electrostatic = {}
        #   self._active_site_flexibility = {}
        #   self._hbonds = {}
        #   self._hydrophobics = {}
        #   self._PI_interactions = {}
        
        self.functions = MathFunctions()
        
        #   pdb_close_contacts = PDB()
        #   pdb_contacts = PDB()
        #   pdb_contacts_alpha_helix = PDB()
        #   pdb_contacts_beta_sheet = PDB()
        #   pdb_contacts_other_2nd_structure = PDB()
        #   pdb_side_chain = PDB()
        #   pdb_back_bone = PDB()
        #   pdb_hydrophobic = PDB()
        #   pdb_hbonds = PDB()
        
        for  ligand_atom_index in self.ligand.AllAtoms:
            self._distance_matrix[ligand_atom_index] = {}
            for receptor_atom_index in self.receptor.AllAtoms:
                ligand_atom = self.ligand.AllAtoms[ligand_atom_index] 
                receptor_atom = self.receptor.AllAtoms[receptor_atom_index]
                dist =  ligand_atom.coordinates.dist_to(receptor_atom.coordinates)
                self._distance_matrix[ligand_atom_index][receptor_atom_index] = dist # distance matrix, for future use

                ### CloseContact
                if dist < parameters.params['close_contacts_dist1_cutoff']: # default 2.5 A
                    self.interactions.append(CloseContact(ligand_atom, receptor_atom))
                ### ElectrostaticInteraction
                if dist < parameters.params['electrostatic_dist_cutoff']:
                    # calculate electrostatic energies for all less than 4 A
                    ligand_charge = ligand_atom.charge
                    receptor_charge = receptor_atom.charge
                    coulomb_energy = (ligand_charge * receptor_charge / dist) * 138.94238460104697e4 # to convert into J/mol # might be nice to double check this
                    # restrict to interactions with energy more negative than -30kJ/mol
                    if coulomb_energy < -30000:
                        self.interactions.append(ElectrostaticInteraction(ligand_atom, receptor_atom, coulomb_energy))
                ### HydrophobicInteraction, defined as C-C contacts
                # modified to exclude polar C atoms on oseltamivir
                # polar C atoms are arbitrarily defined as having absolute charge more than 0.16
                if dist < parameters.params['hydrophobic_dist_cutoff']:
                    if (ligand_atom.element == "C") and (receptor_atom.element == "C") and (abs(ligand_atom.charge) < 0.15) and (abs(receptor_atom.charge) < 0.15 ) :
                        hydrophobic_key = receptor_atom.SideChainOrBackBone() + "_" + receptor_atom.structure
                        self.interactions.append(HydrophobicInteraction(ligand_atom, receptor_atom, hydrophobic_key))
                if dist < parameters.params['hydrogen_bond_dist_cutoff']:
                    # Now see if there's some sort of hydrogen bond between these two atoms. distance cutoff = 4, angle cutoff = 40. Note that this is liberal.
                    if (ligand_atom.element == "O" or ligand_atom.element == "N") and (receptor_atom.element == "O" or receptor_atom.element == "N"):
                        
                        # now build a list of all the hydrogens close to these atoms
                        hydrogens = []
                        
                        for atm_index in self.ligand.AllAtoms:
                            if self.ligand.AllAtoms[atm_index].element == "H": # so it's a hydrogen
                                if self.ligand.AllAtoms[atm_index].coordinates.dist_to(ligand_atom.coordinates) < 1.3: # O-H distance is 0.96 A, N-H is 1.01 A. See http://www.science.uwaterloo.ca/~cchieh/cact/c120/bondel.html
                                    self.ligand.AllAtoms[atm_index].comment = "LIGAND"
                                    hydrogens.append(self.ligand.AllAtoms[atm_index])
                            
                        for atm_index in self.receptor.AllAtoms:
                            if self.receptor.AllAtoms[atm_index].element == "H": # so it's a hydrogen
                                if self.receptor.AllAtoms[atm_index].coordinates.dist_to(receptor_atom.coordinates) < 1.3: # O-H distance is 0.96 A, N-H is 1.01 A. See http://www.science.uwaterloo.ca/~cchieh/cact/c120/bondel.html
                                    self.receptor.AllAtoms[atm_index].comment = "RECEPTOR"
                                    hydrogens.append(self.receptor.AllAtoms[atm_index])
                        
                        # now we need to check the angles
                        for hydrogen in hydrogens:
                            ang = math.fabs(180 - self.functions.angle_between_three_points(ligand_atom.coordinates, hydrogen.coordinates, receptor_atom.coordinates) * 180.0 / math.pi)
                            if ang <= parameters.params['hydrogen_bond_angle_cutoff']:
                                hbonds_key = "HDONOR_" + hydrogen.comment + "_" + receptor_atom.SideChainOrBackBone() + "_" + receptor_atom.structure
                                self.interactions.append(HydrogenBond(ligand_atom, receptor_atom, hbonds_key=hbonds_key,angle=ang ))
 
#                
#                if dist < parameters.params['close_contacts_dist1_cutoff']: # less than 2.5 A
#                    list = [ligand_atom.atomtype, receptor_atom.atomtype]
#                    self.hashtable_entry_add_one(self._ligand_receptor_atom_type_pairs_less_than_two_half, self.list_alphebetize_and_combine(list))
#                    pdb_close_contacts.AddNewAtom(ligand_atom.copy_of())
#                    pdb_close_contacts.AddNewAtom(receptor_atom.copy_of())
#                elif dist < parameters.params['close_contacts_dist2_cutoff']: # less than 4 A
#                    list = [ligand_atom.atomtype, receptor_atom.atomtype]
#                    self.hashtable_entry_add_one(self._ligand_receptor_atom_type_pairs_less_than_four, self.list_alphebetize_and_combine(list))
#                    pdb_contacts.AddNewAtom(ligand_atom.copy_of())
#                    pdb_contacts.AddNewAtom(receptor_atom.copy_of())
#
#                if dist < parameters.params['active_site_flexibility_dist_cutoff']:
#                    # Now get statistics to judge active-site flexibility
#                    flexibility_key = receptor_atom.SideChainOrBackBone() + "_" + receptor_atom.structure # first can be sidechain or backbone, second back be alpha, beta, or other, so six catagories
#                    if receptor_atom.structure == "ALPHA": pdb_contacts_alpha_helix.AddNewAtom(receptor_atom.copy_of())
#                    elif receptor_atom.structure == "BETA": pdb_contacts_beta_sheet.AddNewAtom(receptor_atom.copy_of())
#                    elif receptor_atom.structure == "OTHER": pdb_contacts_other_2nd_structure.AddNewAtom(receptor_atom.copy_of())
#
#                    if receptor_atom.SideChainOrBackBone() == "BACKBONE": pdb_back_bone.AddNewAtom(receptor_atom.copy_of())
#                    elif receptor_atom.SideChainOrBackBone() == "SIDECHAIN": pdb_side_chain.AddNewAtom(receptor_atom.copy_of())
#
#                    self.hashtable_entry_add_one(self._active_site_flexibility, flexibility_key)
#                    
#                    
#                if dist < parameters.params['hydrogen_bond_dist_cutoff']:
#                    # Now see if there's some sort of hydrogen bond between these two atoms. distance cutoff = 4, angle cutoff = 40. Note that this is liberal.
#                    if (ligand_atom.element == "O" or ligand_atom.element == "N") and (receptor_atom.element == "O" or receptor_atom.element == "N"):
#                        
#                        # now build a list of all the hydrogens close to these atoms
#                        hydrogens = []
#                        
#                        for atm_index in ligand.AllAtoms:
#                            if ligand.AllAtoms[atm_index].element == "H": # so it's a hydrogen
#                                if ligand.AllAtoms[atm_index].coordinates.dist_to(ligand_atom.coordinates) < 1.3: # O-H distance is 0.96 A, N-H is 1.01 A. See http://www.science.uwaterloo.ca/~cchieh/cact/c120/bondel.html
#                                    ligand.AllAtoms[atm_index].comment = "LIGAND"
#                                    hydrogens.append(ligand.AllAtoms[atm_index])
#                            
#                        for atm_index in receptor.AllAtoms:
#                            if receptor.AllAtoms[atm_index].element == "H": # so it's a hydrogen
#                                if receptor.AllAtoms[atm_index].coordinates.dist_to(receptor_atom.coordinates) < 1.3: # O-H distance is 0.96 A, N-H is 1.01 A. See http://www.science.uwaterloo.ca/~cchieh/cact/c120/bondel.html
#                                    receptor.AllAtoms[atm_index].comment = "RECEPTOR"
#                                    hydrogens.append(receptor.AllAtoms[atm_index])
#                        
#                        # now we need to check the angles
#                        for hydrogen in hydrogens:
#                            if math.fabs(180 - functions.angle_between_three_points(ligand_atom.coordinates, hydrogen.coordinates, receptor_atom.coordinates) * 180.0 / math.pi) <= parameters.params['hydrogen_bond_angle_cutoff']:
#                                hbonds_key = "HDONOR_" + hydrogen.comment + "_" + receptor_atom.SideChainOrBackBone() + "_" + receptor_atom.structure
#                                pdb_hbonds.AddNewAtom(ligand_atom.copy_of())
#                                pdb_hbonds.AddNewAtom(hydrogen.copy_of())
#                                pdb_hbonds.AddNewAtom(receptor_atom.copy_of())
#                                self.hashtable_entry_add_one(self._hbonds, hbonds_key)
                                                    
#        # Get the total number of each atom type in the ligand
#        ligand_atom_types = {}
#        for ligand_atom_index in ligand.AllAtoms:
#            ligand_atom = ligand.AllAtoms[ligand_atom_index]
#            self.hashtable_entry_add_one(ligand_atom_types, ligand_atom.atomtype)
#            
#        pi_padding = parameters.params['pi_padding_dist'] # This is perhaps controversial. I noticed that often a pi-cation interaction or other pi interaction was only slightly off, but looking at the structure, it was clearly supposed to be a
#        # pi-cation interaction. I've decided then to artificially expand the radius of each pi ring. Think of this as adding in a VDW radius, or accounting for poor crystal-structure resolution, or whatever you want
#        # to justify it.
#        
#        # Count pi-pi stacking and pi-T stacking interactions
#        pdb_pistack = PDB()
#        pdb_pi_T = PDB()
#        # "PI-Stacking Interactions ALIVE AND WELL IN PROTEINS" says distance of 7.5 A is good cutoff. This seems really big to me, except that pi-pi interactions (parallel) are actuall usually off centered. Interesting paper.
#        # Note that adenine and tryptophan count as two aromatic rings. So, for example, an interaction between these two, if positioned correctly, could count for 4 pi-pi interactions.
#        for aromatic1 in ligand.aromatic_rings:
#            for aromatic2 in receptor.aromatic_rings:
#                dist = aromatic1.center.dist_to(aromatic2.center)
#                if dist < parameters.params['pi_pi_interacting_dist_cutoff']: # so there could be some pi-pi interactions.
#                    # first, let's check for stacking interactions. Are the two pi's roughly parallel?
#                    aromatic1_norm_vector = point(aromatic1.plane_coeff[0], aromatic1.plane_coeff[1], aromatic1.plane_coeff[2])
#                    aromatic2_norm_vector = point(aromatic2.plane_coeff[0], aromatic2.plane_coeff[1], aromatic2.plane_coeff[2])
#                    angle_between_planes = self.functions.angle_between_points(aromatic1_norm_vector, aromatic2_norm_vector) * 180.0/math.pi
#
#                    if math.fabs(angle_between_planes-0) < parameters.params['pi_stacking_angle_tolerance'] or math.fabs(angle_between_planes-180) < parameters.params['pi_stacking_angle_tolerance']: # so they're more or less parallel, it's probably pi-pi stackingoutput_dir
#                        # now, pi-pi are not usually right on top of each other. They're often staggared. So I don't want to just look at the centers of the rings and compare. Let's look at each of the atoms.
#                        # do atom of the atoms of one ring, when projected onto the plane of the other, fall within that other ring?
#                        
#                        pi_pi = False # start by assuming it's not a pi-pi stacking interaction
#                        for ligand_ring_index in aromatic1.indices:
#                            # project the ligand atom onto the plane of the receptor ring
#                            pt_on_receptor_plane = self.functions.project_point_onto_plane(ligand.AllAtoms[ligand_ring_index].coordinates, aromatic2.plane_coeff)
#                            if pt_on_receptor_plane.dist_to(aromatic2.center) <= aromatic2.radius + pi_padding:
#                                pi_pi = True
#                                break
#                        
#                        if pi_pi == False: # if you've already determined it's a pi-pi stacking interaction, no need to keep trying
#                            for receptor_ring_index in aromatic2.indices:
#                                # project the ligand atom onto the plane of the receptor ring
#                                pt_on_ligand_plane = self.functions.project_point_onto_plane(receptor.AllAtoms[receptor_ring_index].coordinates, aromatic1.plane_coeff)
#                                if pt_on_ligand_plane.dist_to(aromatic1.center) <= aromatic1.radius + pi_padding:
#                                    pi_pi = True
#                                    break
#                        
#                        if pi_pi == True:
#                            structure = receptor.AllAtoms[aromatic2.indices[0]].structure
#                            if structure == "": structure = "OTHER" # since it could be interacting with a cofactor or something
#                            key = "STACKING_" + structure
#                            
#                            for index in aromatic1.indices: pdb_pistack.AddNewAtom(ligand.AllAtoms[index].copy_of())
#                            for index in aromatic2.indices: pdb_pistack.AddNewAtom(receptor.AllAtoms[index].copy_of())
#                            
#                            self.hashtable_entry_add_one(self._PI_interactions, key)
#                            
#                    elif math.fabs(angle_between_planes-90) < parameters.params['T_stacking_angle_tolerance'] or math.fabs(angle_between_planes-270) < parameters.params['T_stacking_angle_tolerance']: # so they're more or less perpendicular, it's probably a pi-edge interaction
#                        
#                        # having looked at many structures, I noticed the algorithm was identifying T-pi reactions when the two rings were in fact quite distant, often with other atoms
#                        # in between. Eye-balling it, requiring that at their closest they be at least 5 A apart seems to separate the good T's from the bad
#                        min_dist = 100.0
#                        for ligand_ind in aromatic1.indices:
#                            ligand_at = ligand.AllAtoms[ligand_ind]
#                            for receptor_ind in aromatic2.indices:
#                                receptor_at = receptor.AllAtoms[receptor_ind]
#                                dist = ligand_at.coordinates.dist_to(receptor_at.coordinates)
#                                if dist < min_dist: min_dist = dist
#                                
#                        if min_dist <= parameters.params['T_stacking_closest_dist_cutoff']: # so at their closest points, the two rings come within 5 A of each other.
#                        
#                            # okay, is the ligand pi pointing into the receptor pi, or the other way around?
#                            # first, project the center of the ligand pi onto the plane of the receptor pi, and vs. versa
#                            
#                            # This could be directional somehow, like a hydrogen bond.
#                            
#                            pt_on_receptor_plane = self.functions.project_point_onto_plane(aromatic1.center, aromatic2.plane_coeff)
#                            pt_on_lignad_plane = self.functions.project_point_onto_plane(aromatic2.center, aromatic1.plane_coeff)
#                            
#                            # now, if it's a true pi-T interaction, this projected point should fall within the ring whose plane it's been projected into.
#                            if (pt_on_receptor_plane.dist_to(aromatic2.center) <= aromatic2.radius + pi_padding) or (pt_on_lignad_plane.dist_to(aromatic1.center) <= aromatic1.radius + pi_padding): # so it is in the ring on the projected plane.
#                                structure = receptor.AllAtoms[aromatic2.indices[0]].structure
#                                if structure == "": structure = "OTHER" # since it could be interacting with a cofactor or something
#                                key = "T-SHAPED_" + structure
#    
#                                for index in aromatic1.indices: pdb_pi_T.AddNewAtom(ligand.AllAtoms[index].copy_of())
#                                for index in aromatic2.indices: pdb_pi_T.AddNewAtom(receptor.AllAtoms[index].copy_of())
#    
#                                self.hashtable_entry_add_one(self._PI_interactions, key)
#                            
#        # Now identify pi-cation interactions
#        pdb_pi_cat = PDB()
#        
#        for aromatic in self.receptor.aromatic_rings:
#            for charged in self.ligand.charges:
#                if charged.positive == True: # so only consider positive charges
#                    if charged.coordinates.dist_to(aromatic.center) < parameters.params['cation_pi_dist_cutoff']: # distance cutoff based on "Cation-pi interactions in structural biology."
#                        # project the charged onto the plane of the aromatic
#                        charge_projected = self.functions.project_point_onto_plane(charged.coordinates,aromatic.plane_coeff)
#                        if charge_projected.dist_to(aromatic.center) < aromatic.radius + pi_padding:
#                            structure = receptor.AllAtoms[aromatic.indices[0]].structure
#                            if structure == "": structure = "OTHER" # since it could be interacting with a cofactor or something
#                            key = "PI-CATION_LIGAND-CHARGED_" + structure
#                            
#                            for index in aromatic.indices: pdb_pi_cat.AddNewAtom(receptor.AllAtoms[index].copy_of())
#                            for index in charged.indices: pdb_pi_cat.AddNewAtom(ligand.AllAtoms[index].copy_of())
#                            
#                            self.hashtable_entry_add_one(self._PI_interactions, key)
#                    
#        for aromatic in self.ligand.aromatic_rings: # now it's the ligand that has the aromatic group
#            for charged in self.receptor.charges:
#                if charged.positive == True: # so only consider positive charges
#                    if charged.coordinates.dist_to(aromatic.center) < parameters.params['cation_pi_dist_cutoff']: # distance cutoff based on "Cation-pi interactions in structural biology."
#                        # project the charged onto the plane of the aromatic
#                        charge_projected = self.functions.project_point_onto_plane(charged.coordinates,aromatic.plane_coeff)
#                        if charge_projected.dist_to(aromatic.center) < aromatic.radius + pi_padding:
#                            structure = receptor.AllAtoms[charged.indices[0]].structure
#                            if structure == "": structure = "OTHER" # since it could be interacting with a cofactor or something
#                            key = "PI-CATION_RECEPTOR-CHARGED_" + structure
#    
#                            for index in aromatic.indices: pdb_pi_cat.AddNewAtom(ligand.AllAtoms[index].copy_of())
#                            for index in charged.indices: pdb_pi_cat.AddNewAtom(receptor.AllAtoms[index].copy_of())
#    
#                            self.hashtable_entry_add_one(self._PI_interactions, key)
#
#        # now count the number of salt bridges
#        pdb_salt_bridges = PDB()
#        salt_bridges = {}
#        for receptor_charge in self.receptor.charges:
#            for ligand_charge in self.ligand.charges:
#                if ligand_charge.positive != receptor_charge.positive: # so they have oppositve charges
#                    if ligand_charge.coordinates.dist_to(receptor_charge.coordinates) < parameters.params['salt_bridge_dist_cutoff']: # 4  is good cutoff for salt bridges according to "Close-Range Electrostatic Interactions in Proteins", but looking at complexes, I decided to go with 5.5 A
#                        structure = receptor.AllAtoms[receptor_charge.indices[0]].structure
#                        if structure == "": structure = "OTHER" # since it could be interacting with a cofactor or something
#                        key = "SALT-BRIDGE_" + structure
#                        
#                        for index in receptor_charge.indices: pdb_salt_bridges.AddNewAtom(receptor.AllAtoms[index].copy_of())
#                        for index in ligand_charge.indices: pdb_salt_bridges.AddNewAtom(ligand.AllAtoms[index].copy_of())
#                        
#                        self.hashtable_entry_add_one(salt_bridges, key)
    def close_contacts(self):
        subset = [i for i in self.interactions if i.type == 'closecontact']
        return subset 

    def hydrophobic_contacts(self):
        subset = [i for i in self.interactions if i.type == 'hydrophobic']
        return subset 

    def hbonds(self):
        subset = [i for i in self.interactions if i.type == 'hydrogen']
        return subset 

    def electrostatic_interactions(self):
        subset = [i for i in self.interactions if i.type == 'electrostatic']
        return subset 
    def __iter__(self):
        for i in self.interactions:
            yield i
    def __str__(self):
        return ""
    def _get_binding_energy(self,docked_filename):
        '''only compatible with VINA result in pdbqt format'''
        IFILE = open(docked_filename, 'r')
        for l in IFILE:
            if l[0:18] == "REMARK VINA RESULT":
                values = l.split()
                try:
                    be = float(values[3])
                    return be
                except ValueError:
                    return values[3]
         
    def write(self,output_file='interactions.out'):
        f = open(output_file,'w')
        f.write(str(self))
        f.close()

class command_line_parameters:
    
    params = {}
    
    def is_num(self, num):
        try:
            t = float(num)
            return t
        except ValueError:
            return num
    
    def __init__(self, parameters):
        
        # first, set defaults
        self.params['close_contacts_dist1_cutoff'] = 2.5
        self.params['close_contacts_dist2_cutoff'] = 4.0
        self.params['electrostatic_dist_cutoff'] = 4.0
        self.params['active_site_flexibility_dist_cutoff'] = 4.0
        self.params['hydrophobic_dist_cutoff'] = 4.0
        self.params['hydrogen_bond_dist_cutoff'] = 4.0
        self.params['hydrogen_bond_angle_cutoff'] = 40.0
        self.params['pi_padding_dist'] = 0.75
        self.params['pi_pi_interacting_dist_cutoff'] = 7.5
        self.params['pi_stacking_angle_tolerance'] = 30.0
        self.params['T_stacking_angle_tolerance'] = 30.0
        self.params['T_stacking_closest_dist_cutoff'] = 5.0
        self.params['cation_pi_dist_cutoff'] = 6.0
        self.params['salt_bridge_dist_cutoff'] = 5.5
        self.params['receptor'] = ''
        self.params['ligand'] = ''
        self.params['output_dir'] = ''
        self.params['output_file'] = ''

        # now get user inputed values
        
        for index in range(len(parameters)):
            item = parameters[index]
            if item[:1] == '-': # so it's a parameter key value
                key = item.replace('-','')
                value = self.is_num(parameters[index+1])
                if key in self.params.keys():
                    self.params[key] = value
                    parameters[index] = ""
                    parameters[index + 1] = ""
        
        # make a list of all the command-line parameters not used
        self.error = ""
        for index in range(1,len(parameters)):
            item = parameters[index]
            if item != "": self.error = self.error + item + " "
        
        # Make sure the output directory, if specified, ends in a /
        if self.params['output_dir'] != "":
            if self.params['output_dir'][-1:] != os.sep:
                self.params['output_dir'] = self.params['output_dir'] + os.sep
        
        # If an output directory is specified but a log file isn't, set a default logfile
        if self.params['output_dir'] != "" and self.params['output_file'] == '': self.params['output_file'] = self.params['output_dir'] + 'output.pdb'
        
    def okay_to_proceed(self):
        # at the very least, you need the ligand and the receptor
        if self.params['receptor'] != '' and self.params['ligand'] != '':
            return True
        else: return False


#   
#   
#   cmd_params = command_line_parameters(sys.argv[:])
#   
#   if cmd_params.okay_to_proceed() == False:
#       print "Error: You need to specify the ligand and receptor PDBQT files to analyze using\nthe -receptor and -ligand tags from the command line.\n"
#       sys.exit(0)
#       
#   if cmd_params.error != "":
#       print "Warning: The following command-line parameters were not recognized:"
#       print "   " + cmd_params.error + "\n"
#       
#   lig = cmd_params.params['ligand']
#   rec = cmd_params.params['receptor']
#   
#   ligand = PDB()
#   receptor = PDB()
#   
#   ligand.LoadPDB(lig)
#   receptor.LoadPDB(rec)
#   
#   d = binana(lig, rec, cmd_params)

if __name__ == '__main__':
#    # illustrative run
#    cmd_params = command_line_parameters("")
#    rec = '../receptors/wt-ensemble/cluster-0001.pdbqt'
#    vinaio = VinaIO(receptor_pdbqt=rec,docked_pdbqt='../vina-ensemble/wt/1/cluster-0001.pdbqt')
#    lig = './top_conf.pdbqt'
#    vinaio.write_conformation(lig,1)
#    d  = Interactions(lig,rec,cmd_params)
#    hyp = d.hydrophobic_contacts()
#    elec = d.electrostatic_interactions()
#    for i in hyp:
#        print i.receptor_atom.residue + ' ' + str(i.receptor_atom.resid)
#    print "-----------"
#    for i in elec:
#        print i.receptor_atom.residue + ' ' + str(i.receptor_atom.resid) + ' ' + str(i.coulomb_energy)
#    os.system('rm '+ lig) 

    # analyzing ensembles
    import glob
    RESULT_DIR = '../vina-ensemble/wt-transition-probe-4/'
    RECEPTOR_DIR = '../receptors/wt-ensemble/'
    receptor_ensemble = glob.glob(RECEPTOR_DIR+'*000?.pdbqt')
    for i in range(5,6):
        RESULT_DIR += str(i+1)
        for rec in receptor_ensemble:
            base = os.path.basename(rec)
            vinaio = VinaIO(receptor_pdbqt=rec,docked_pdbqt=RESULT_DIR+'/'+base)
            lig = 'tmp.pdbqt'
            vinaio.write_conformation(lig,1)
            cmd_params = command_line_parameters("")
            d = Interactions(lig,rec,cmd_params)
            print "Binding energy: %s" % d.binding_energy
            point_set = [d.ligand.AllAtoms[i].coordinates for i in d.ligand.AllAtoms ]
            print "Centroid: %s" % d.ligand.functions.centroid(*point_set)
            print len(d)
            elec = d.electrostatic_interactions()
            hbonds = d.hbonds()
            hyp = d.hydrophobic_contacts()
            ccn = d.close_contacts()
            print len(elec)
            print len(hbonds)
            print len(hyp)
            print len(ccn)
            for i in d:
                print i.type + ' ' + i.receptor_atom.residue + ' ' + str(i.receptor_atom.resid)# + ' ' + str(i.coulomb_energy)
            os.system('rm %s' % lig)
            print "---------------------"

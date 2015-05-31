##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Mon May 28 11:11:58 2012
##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path /home/Ubuntu/tk/Projects/BindingPathway/clustering/WT/middle_structure_aligned.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing npbe...
PBEparm_parseToken:  trying npbe...
NOsh: parsed npbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing gamma...
PBEparm_parseToken:  trying gamma...
MGparm_parseToken:  trying gamma...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (97, 97, 97)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 5749 atoms
Valist_getStatistics:  Max atom coordinate:  (20.26, 107.171, 126.068)
Valist_getStatistics:  Min atom coordinate:  (-34.196, 48.274, 72.93)
Valist_getStatistics:  Molecule center:  (-6.968, 77.7225, 99.499)
NOsh_setupCalcMGAUTO(nosh.c, 1526):  coarse grid center = -6.968 77.7225 99.499
NOsh_setupCalcMGAUTO(nosh.c, 1531):  fine grid center = -6.968 77.7225 99.499
NOsh_setupCalcMGAUTO (nosh.c, 1543):  Coarse grid spacing = 0.964325, 1.04297, 0.940985
NOsh_setupCalcMGAUTO (nosh.c, 1545):  Fine grid spacing = 0.775583, 0.821844, 0.761854
NOsh_setupCalcMGAUTO (nosh.c, 1547):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.804276, 0.787986, 0.809634 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (nosh.c, 1641):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (nosh.c, 1643):  coarse mesh center = -6.968 77.7225 99.499
NOsh_setupCalcMGAUTO (nosh.c, 1648):  coarse mesh upper corner = 39.3196 127.785 144.666
NOsh_setupCalcMGAUTO (nosh.c, 1653):  coarse mesh lower corner = -53.2556 27.66 54.3317
NOsh_setupCalcMGAUTO (nosh.c, 1658):  initial fine mesh upper corner = 30.26 117.171 136.068
NOsh_setupCalcMGAUTO (nosh.c, 1663):  initial fine mesh lower corner = -44.196 38.274 62.93
NOsh_setupCalcMGAUTO (nosh.c, 1724):  final fine mesh upper corner = 30.26 117.171 136.068
NOsh_setupCalcMGAUTO (nosh.c, 1729):  final fine mesh lower corner = -44.196 38.274 62.93
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 38.8386
Vpbe_ctor2:  solute dimensions = 57.348 x 61.356 x 55.344
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (67.236, 71.677, 65.918)
Vclist_setupGrid:  Grid lower corner = (-40.586, 41.884, 66.54)
Vclist_assignAtoms:  Have 5676906 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 97
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 13
Vpmg_ctor2:  PMG chose nf = 912673, nc = 2197
Vpmg_ctor2:  PMG chose narr = 1048144, narrc = 135471
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 13127137, niwk = 750
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.610000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 1.700000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 3.500000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 4.260000e+00
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  6.296854e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.080000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 5.440899e+05
PMG: contraction number = , 5.440899e+05
NEWTON: attempting damping, relres =  7.776596e-02
NEWTON: attempting damping, relres =  5.354473e-01
NEWTON: damping accepted, relres =  7.776596e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  7.776596e-02
PMG: contraction number =  7.776596e-02
NEWTON: using errtol_s:  4.896809e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 8.250000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 5.068304e+04
PMG: contraction number = , 5.068304e+04
PMG: iteration =  2
PMG: relative residual =  7.244052e-03
PMG: contraction number =  9.315197e-02
NEWTON: using errtol_s:  4.561474e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 9.770000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.173259e+03
PMG: contraction number = , 6.173259e+03
PMG: iteration =  3
PMG: relative residual =  8.823347e-04
PMG: contraction number =  1.218013e-01
NEWTON: using errtol_s:  5.555933e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.131000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 9.224484e+02
PMG: contraction number = , 9.224484e+02
PMG: iteration =  4
PMG: relative residual =  1.318442e-04
PMG: contraction number =  1.494265e-01
NEWTON: using errtol_s:  8.302036e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.285000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.726707e+02
PMG: contraction number = , 1.726707e+02
PMG: iteration =  5
PMG: relative residual =  2.467956e-05
PMG: contraction number =  1.871873e-01
NEWTON: using errtol_s:  1.554036e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.437000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 4.067674e+01
PMG: contraction number = , 4.067674e+01
PMG: iteration =  6
PMG: relative residual =  5.813866e-06
PMG: contraction number =  2.355741e-01
NEWTON: using errtol_s:  3.660907e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.589000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.199112e+01
PMG: contraction number = , 1.199112e+01
PMG: iteration =  7
PMG: relative residual =  1.713873e-06
PMG: contraction number =  2.947905e-01
NEWTON: using errtol_s:  1.079201e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.742000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 3.943342e+00
PMG: contraction number = , 3.943342e+00
PMG: iteration =  8
PMG: relative residual =  5.636159e-07
PMG: contraction number =  3.288552e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.404000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.462000e+01
Vpmg_setPart:  lower corner = (-53.2556, 27.66, 54.3317)
Vpmg_setPart:  upper corner = (39.3196, 127.785, 144.666)
Vpmg_setPart:  actual minima = (-53.2556, 27.66, 54.3317)
Vpmg_setPart:  actual maxima = (39.3196, 127.785, 144.666)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 38.8386
Vpbe_ctor2:  solute dimensions = 57.348 x 61.356 x 55.344
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (67.236, 71.677, 65.918)
Vclist_setupGrid:  Grid lower corner = (-40.586, 41.884, 66.54)
Vclist_assignAtoms:  Have 5676906 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 97
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 13
Vpmg_ctor2:  PMG chose nf = 912673, nc = 2197
Vpmg_ctor2:  PMG chose narr = 1048144, narrc = 135471
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 13127137, niwk = 750
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -44.196, 38.274, 62.93
VPMG::focusFillBound -- New mesh maxs = 30.26, 117.171, 136.068
VPMG::focusFillBound -- Old mesh mins = -53.2556, 27.66, 54.3317
VPMG::focusFillBound -- Old mesh maxs = 39.3196, 127.785, 144.666
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.920000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 1.500000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 2.700000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.271000e+01
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  7.315664e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.447000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 7.453963e+05
PMG: contraction number = , 7.453963e+05
NEWTON: attempting damping, relres =  9.170141e-02
NEWTON: attempting damping, relres =  5.426719e-01
NEWTON: damping accepted, relres =  9.170141e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  9.170141e-02
PMG: contraction number =  9.170141e-02
NEWTON: using errtol_s:  6.708567e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.665000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 7.157154e+04
PMG: contraction number = , 7.157154e+04
PMG: iteration =  2
PMG: relative residual =  8.804995e-03
PMG: contraction number =  9.601810e-02
NEWTON: using errtol_s:  6.441438e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.818000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 8.887665e+03
PMG: contraction number = , 8.887665e+03
PMG: iteration =  3
PMG: relative residual =  1.093393e-03
PMG: contraction number =  1.241788e-01
NEWTON: using errtol_s:  7.998898e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.970000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.319509e+03
PMG: contraction number = , 1.319509e+03
PMG: iteration =  4
PMG: relative residual =  1.623309e-04
PMG: contraction number =  1.484652e-01
NEWTON: using errtol_s:  1.187558e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.123000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 2.422562e+02
PMG: contraction number = , 2.422562e+02
PMG: iteration =  5
PMG: relative residual =  2.980325e-05
PMG: contraction number =  1.835957e-01
NEWTON: using errtol_s:  2.180306e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.277000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.242731e+01
PMG: contraction number = , 6.242731e+01
PMG: iteration =  6
PMG: relative residual =  7.680038e-06
PMG: contraction number =  2.576913e-01
NEWTON: using errtol_s:  5.618458e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.430000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.977492e+01
PMG: contraction number = , 1.977492e+01
PMG: iteration =  7
PMG: relative residual =  2.432784e-06
PMG: contraction number =  3.167671e-01
NEWTON: using errtol_s:  1.779743e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.584000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.728986e+00
PMG: contraction number = , 6.728986e+00
PMG: iteration =  8
PMG: relative residual =  8.278247e-07
PMG: contraction number =  3.402788e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.404000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.451000e+01
Vpmg_setPart:  lower corner = (-44.196, 38.274, 62.93)
Vpmg_setPart:  upper corner = (30.26, 117.171, 136.068)
Vpmg_setPart:  actual minima = (-44.196, 38.274, 62.93)
Vpmg_setPart:  actual maxima = (30.26, 117.171, 136.068)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 3.773000e+01
##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Thu May 31 15:28:40 2012
##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path /home/Ubuntu/tk/Projects/BindingPathway/clustering/WT/middle_structure.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing npbe...
PBEparm_parseToken:  trying npbe...
NOsh: parsed npbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing gamma...
PBEparm_parseToken:  trying gamma...
MGparm_parseToken:  trying gamma...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (97, 97, 97)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 5749 atoms
Valist_getStatistics:  Max atom coordinate:  (20.129, 107.809, 124.682)
Valist_getStatistics:  Min atom coordinate:  (-33.683, 47.724, 72.829)
Valist_getStatistics:  Molecule center:  (-6.777, 77.7665, 98.7555)
NOsh_setupCalcMGAUTO(nosh.c, 1526):  coarse grid center = -6.777 76.8785 98.7435
NOsh_setupCalcMGAUTO(nosh.c, 1531):  fine grid center = -6.777 76.8785 98.7435
NOsh_setupCalcMGAUTO (nosh.c, 1543):  Coarse grid spacing = 0.952921, 1.09546, 0.934664
NOsh_setupCalcMGAUTO (nosh.c, 1545):  Fine grid spacing = 0.768875, 0.852719, 0.758135
NOsh_setupCalcMGAUTO (nosh.c, 1547):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.806861, 0.778415, 0.811132 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (nosh.c, 1641):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (nosh.c, 1643):  coarse mesh center = -6.777 76.8785 98.7435
NOsh_setupCalcMGAUTO (nosh.c, 1648):  coarse mesh upper corner = 38.9632 129.46 143.607
NOsh_setupCalcMGAUTO (nosh.c, 1653):  coarse mesh lower corner = -52.5172 24.2966 53.8796
NOsh_setupCalcMGAUTO (nosh.c, 1658):  initial fine mesh upper corner = 30.129 117.809 135.134
NOsh_setupCalcMGAUTO (nosh.c, 1663):  initial fine mesh lower corner = -43.683 35.948 62.353
NOsh_setupCalcMGAUTO (nosh.c, 1724):  final fine mesh upper corner = 30.129 117.809 135.134
NOsh_setupCalcMGAUTO (nosh.c, 1729):  final fine mesh lower corner = -43.683 35.948 62.353
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 39.9413
Vpbe_ctor2:  solute dimensions = 56.539 x 62.406 x 54.016
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (66.592, 72.865, 64.633)
Vclist_setupGrid:  Grid lower corner = (-40.073, 41.334, 66.439)
Vclist_assignAtoms:  Have 5732586 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 97
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 13
Vpmg_ctor2:  PMG chose nf = 912673, nc = 2197
Vpmg_ctor2:  PMG chose narr = 1048144, narrc = 135471
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 13127137, niwk = 750
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.560000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 2.200000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 3.300000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 4.250000e+00
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  6.261944e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.050000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 5.498237e+05
PMG: contraction number = , 5.498237e+05
NEWTON: attempting damping, relres =  7.902360e-02
NEWTON: attempting damping, relres =  5.359408e-01
NEWTON: damping accepted, relres =  7.902360e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  7.902360e-02
PMG: contraction number =  7.902360e-02
NEWTON: using errtol_s:  4.948414e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 8.240000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 5.322204e+04
PMG: contraction number = , 5.322204e+04
PMG: iteration =  2
PMG: relative residual =  7.649355e-03
PMG: contraction number =  9.679836e-02
NEWTON: using errtol_s:  4.789983e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 9.760000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.699501e+03
PMG: contraction number = , 6.699501e+03
PMG: iteration =  3
PMG: relative residual =  9.628880e-04
PMG: contraction number =  1.258783e-01
NEWTON: using errtol_s:  6.029551e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.129000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.035749e+03
PMG: contraction number = , 1.035749e+03
PMG: iteration =  4
PMG: relative residual =  1.488633e-04
PMG: contraction number =  1.546008e-01
NEWTON: using errtol_s:  9.321736e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.281000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.965826e+02
PMG: contraction number = , 1.965826e+02
PMG: iteration =  5
PMG: relative residual =  2.825390e-05
PMG: contraction number =  1.897976e-01
NEWTON: using errtol_s:  1.769244e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.434000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 4.626657e+01
PMG: contraction number = , 4.626657e+01
PMG: iteration =  6
PMG: relative residual =  6.649679e-06
PMG: contraction number =  2.353543e-01
NEWTON: using errtol_s:  4.163992e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.586000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.254019e+01
PMG: contraction number = , 1.254019e+01
PMG: iteration =  7
PMG: relative residual =  1.802343e-06
PMG: contraction number =  2.710421e-01
NEWTON: using errtol_s:  1.128617e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.738000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 3.743757e+00
PMG: contraction number = , 3.743757e+00
PMG: iteration =  8
PMG: relative residual =  5.380726e-07
PMG: contraction number =  2.985407e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.401000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.463000e+01
Vpmg_setPart:  lower corner = (-52.5172, 24.2966, 53.8796)
Vpmg_setPart:  upper corner = (38.9632, 129.46, 143.607)
Vpmg_setPart:  actual minima = (-52.5172, 24.2967, 53.8796)
Vpmg_setPart:  actual maxima = (38.9632, 129.46, 143.607)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 39.9413
Vpbe_ctor2:  solute dimensions = 56.539 x 62.406 x 54.016
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (66.592, 72.865, 64.633)
Vclist_setupGrid:  Grid lower corner = (-40.073, 41.334, 66.439)
Vclist_assignAtoms:  Have 5732586 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 97
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 13
Vpmg_ctor2:  PMG chose nf = 912673, nc = 2197
Vpmg_ctor2:  PMG chose narr = 1048144, narrc = 135471
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 13127137, niwk = 750
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -43.683, 35.948, 62.353
VPMG::focusFillBound -- New mesh maxs = 30.129, 117.809, 135.134
VPMG::focusFillBound -- Old mesh mins = -52.5172, 24.2967, 53.8796
VPMG::focusFillBound -- Old mesh maxs = 38.9632, 129.46, 143.607
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.840000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 1.500000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 2.900000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.262000e+01
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  7.280637e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.440000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 7.350992e+05
PMG: contraction number = , 7.350992e+05
NEWTON: attempting damping, relres =  9.086969e-02
NEWTON: attempting damping, relres =  5.421399e-01
NEWTON: damping accepted, relres =  9.086969e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  9.086969e-02
PMG: contraction number =  9.086969e-02
NEWTON: using errtol_s:  6.615892e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.659000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 7.122212e+04
PMG: contraction number = , 7.122212e+04
PMG: iteration =  2
PMG: relative residual =  8.804161e-03
PMG: contraction number =  9.688777e-02
NEWTON: using errtol_s:  6.409990e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.812000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 8.859304e+03
PMG: contraction number = , 8.859304e+03
PMG: iteration =  3
PMG: relative residual =  1.095148e-03
PMG: contraction number =  1.243898e-01
NEWTON: using errtol_s:  7.973373e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.964000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.349615e+03
PMG: contraction number = , 1.349615e+03
PMG: iteration =  4
PMG: relative residual =  1.668334e-04
PMG: contraction number =  1.523388e-01
NEWTON: using errtol_s:  1.214654e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.117000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 2.415577e+02
PMG: contraction number = , 2.415577e+02
PMG: iteration =  5
PMG: relative residual =  2.986029e-05
PMG: contraction number =  1.789827e-01
NEWTON: using errtol_s:  2.174020e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.270000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.172653e+01
PMG: contraction number = , 6.172653e+01
PMG: iteration =  6
PMG: relative residual =  7.630359e-06
PMG: contraction number =  2.555353e-01
NEWTON: using errtol_s:  5.555388e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.423000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 2.039820e+01
PMG: contraction number = , 2.039820e+01
PMG: iteration =  7
PMG: relative residual =  2.521535e-06
PMG: contraction number =  3.304608e-01
NEWTON: using errtol_s:  1.835838e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.575000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 8.317684e+00
PMG: contraction number = , 8.317684e+00
PMG: iteration =  8
PMG: relative residual =  1.028195e-06
PMG: contraction number =  4.077656e-01
NEWTON: using errtol_s:  7.485915e+00
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.729000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 3.147687e+00
PMG: contraction number = , 3.147687e+00
PMG: iteration =  9
PMG: relative residual =  3.891031e-07
PMG: contraction number =  3.784332e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.555000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.605000e+01
Vpmg_setPart:  lower corner = (-43.683, 35.948, 62.353)
Vpmg_setPart:  upper corner = (30.129, 117.809, 135.134)
Vpmg_setPart:  actual minima = (-43.683, 35.948, 62.353)
Vpmg_setPart:  actual maxima = (30.129, 117.809, 135.134)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.000000e-02
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 3.918000e+01
##############################################################################
# MC-shell I/O capture file.
# Creation Date and Time:  Tue Jul 24 12:46:16 2012
##############################################################################
Hello world from PE 0
Vnm_tstart: starting timer 26 (APBS WALL CLOCK)..
NOsh_parseInput:  Starting file parsing...
NOsh: Parsing READ section
NOsh: Storing molecule 0 path /home/Ubuntu/tk/Projects/BindingPathway/clustering/WT/middle_structure.pqr
NOsh: Done parsing READ section
NOsh: Done parsing READ section (nmol=1, ndiel=0, nkappa=0, ncharge=0)
NOsh: Parsing ELEC section
NOsh_parseMG: Parsing parameters for MG calculation
NOsh_parseMG:  Parsing dime...
PBEparm_parseToken:  trying dime...
MGparm_parseToken:  trying dime...
NOsh_parseMG:  Parsing cglen...
PBEparm_parseToken:  trying cglen...
MGparm_parseToken:  trying cglen...
NOsh_parseMG:  Parsing fglen...
PBEparm_parseToken:  trying fglen...
MGparm_parseToken:  trying fglen...
NOsh_parseMG:  Parsing cgcent...
PBEparm_parseToken:  trying cgcent...
MGparm_parseToken:  trying cgcent...
NOsh_parseMG:  Parsing fgcent...
PBEparm_parseToken:  trying fgcent...
MGparm_parseToken:  trying fgcent...
NOsh_parseMG:  Parsing npbe...
PBEparm_parseToken:  trying npbe...
NOsh: parsed npbe
NOsh_parseMG:  Parsing bcfl...
PBEparm_parseToken:  trying bcfl...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing ion...
PBEparm_parseToken:  trying ion...
NOsh_parseMG:  Parsing pdie...
PBEparm_parseToken:  trying pdie...
NOsh_parseMG:  Parsing sdie...
PBEparm_parseToken:  trying sdie...
NOsh_parseMG:  Parsing chgm...
PBEparm_parseToken:  trying chgm...
MGparm_parseToken:  trying chgm...
NOsh_parseMG:  Parsing mol...
PBEparm_parseToken:  trying mol...
NOsh_parseMG:  Parsing srfm...
PBEparm_parseToken:  trying srfm...
NOsh_parseMG:  Parsing srad...
PBEparm_parseToken:  trying srad...
NOsh_parseMG:  Parsing swin...
PBEparm_parseToken:  trying swin...
NOsh_parseMG:  Parsing temp...
PBEparm_parseToken:  trying temp...
NOsh_parseMG:  Parsing sdens...
PBEparm_parseToken:  trying sdens...
NOsh_parseMG:  Parsing gamma...
PBEparm_parseToken:  trying gamma...
MGparm_parseToken:  trying gamma...
NOsh_parseMG:  Parsing calcenergy...
PBEparm_parseToken:  trying calcenergy...
NOsh_parseMG:  Parsing calcforce...
PBEparm_parseToken:  trying calcforce...
NOsh_parseMG:  Parsing write...
PBEparm_parseToken:  trying write...
NOsh_parseMG:  Parsing end...
MGparm_check:  checking MGparm object of type 1.
NOsh:  nlev = 4, dime = (97, 97, 65)
NOsh: Done parsing ELEC section (nelec = 1)
NOsh: Done parsing file (got QUIT)
Valist_readPQR: Counted 5749 atoms
Valist_getStatistics:  Max atom coordinate:  (20.129, 107.809, 124.682)
Valist_getStatistics:  Min atom coordinate:  (-33.683, 47.724, 72.829)
Valist_getStatistics:  Molecule center:  (-6.777, 77.7665, 98.7555)
NOsh_setupCalcMGAUTO(nosh.c, 1526):  coarse grid center = -6.777 77.7665 98.7555
NOsh_setupCalcMGAUTO(nosh.c, 1531):  fine grid center = -6.777 77.7665 98.7555
NOsh_setupCalcMGAUTO (nosh.c, 1543):  Coarse grid spacing = 0.952921, 1.06401, 1.37735
NOsh_setupCalcMGAUTO (nosh.c, 1545):  Fine grid spacing = 0.768875, 0.834219, 1.1227
NOsh_setupCalcMGAUTO (nosh.c, 1547):  Displacement between fine and coarse grids = 0, 0, 0
NOsh:  2 levels of focusing with 0.806861, 0.784036, 0.815121 reductions
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalcMGAUTO (nosh.c, 1641):  starting mesh repositioning.
NOsh_setupCalcMGAUTO (nosh.c, 1643):  coarse mesh center = -6.777 77.7665 98.7555
NOsh_setupCalcMGAUTO (nosh.c, 1648):  coarse mesh upper corner = 38.9632 128.839 142.831
NOsh_setupCalcMGAUTO (nosh.c, 1653):  coarse mesh lower corner = -52.5172 26.6942 54.6805
NOsh_setupCalcMGAUTO (nosh.c, 1658):  initial fine mesh upper corner = 30.129 117.809 134.682
NOsh_setupCalcMGAUTO (nosh.c, 1663):  initial fine mesh lower corner = -43.683 37.724 62.829
NOsh_setupCalcMGAUTO (nosh.c, 1724):  final fine mesh upper corner = 30.129 117.809 134.682
NOsh_setupCalcMGAUTO (nosh.c, 1729):  final fine mesh lower corner = -43.683 37.724 62.829
NOsh_setupMGAUTO:  Resetting boundary flags
NOsh_setupCalc:  Mapping ELEC statement 0 (1) to calculation 1 (2)
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 39.9413
Vpbe_ctor2:  solute dimensions = 56.539 x 62.406 x 54.016
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (66.592, 72.865, 64.633)
Vclist_setupGrid:  Grid lower corner = (-40.073, 41.334, 66.439)
Vclist_assignAtoms:  Have 5732586 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 65
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 9
Vpmg_ctor2:  PMG chose nf = 611585, nc = 1521
Vpmg_ctor2:  PMG chose narr = 702964, narrc = 91379
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 8822477, niwk = 750
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vpmg_fillco:  filling boundary arrays
Vpmg_fillco:  done filling boundary arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.240000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 9.000000e-02
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 1.900000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 3.640000e+00
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  5.582853e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 4.820000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 5.017516e+05
PMG: contraction number = , 5.017516e+05
NEWTON: attempting damping, relres =  8.088632e-02
NEWTON: attempting damping, relres =  5.362185e-01
NEWTON: damping accepted, relres =  8.088632e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  8.088632e-02
PMG: contraction number =  8.088632e-02
NEWTON: using errtol_s:  4.515764e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 6.260000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.211184e+04
PMG: contraction number = , 6.211184e+04
PMG: iteration =  2
PMG: relative residual =  1.001292e-02
PMG: contraction number =  1.237900e-01
NEWTON: using errtol_s:  5.590066e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 7.270000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.056088e+04
PMG: contraction number = , 1.056088e+04
PMG: iteration =  3
PMG: relative residual =  1.702497e-03
PMG: contraction number =  1.700300e-01
NEWTON: using errtol_s:  9.504787e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 8.280000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 2.071580e+03
PMG: contraction number = , 2.071580e+03
PMG: iteration =  4
PMG: relative residual =  3.339551e-04
PMG: contraction number =  1.961561e-01
NEWTON: using errtol_s:  1.864422e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 9.290000e+00
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 4.407796e+02
PMG: contraction number = , 4.407796e+02
PMG: iteration =  5
PMG: relative residual =  7.105716e-05
PMG: contraction number =  2.127746e-01
NEWTON: using errtol_s:  3.967017e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.030000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.019459e+02
PMG: contraction number = , 1.019459e+02
PMG: iteration =  6
PMG: relative residual =  1.643449e-05
PMG: contraction number =  2.312855e-01
NEWTON: using errtol_s:  9.175133e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.130000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 2.538831e+01
PMG: contraction number = , 2.538831e+01
PMG: iteration =  7
PMG: relative residual =  4.092796e-06
PMG: contraction number =  2.490370e-01
NEWTON: using errtol_s:  2.284948e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.231000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.844416e+00
PMG: contraction number = , 6.844416e+00
PMG: iteration =  8
PMG: relative residual =  1.103374e-06
PMG: contraction number =  2.695893e-01
NEWTON: using errtol_s:  6.159974e+00
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.332000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.938328e+00
PMG: contraction number = , 1.938328e+00
PMG: iteration =  9
PMG: relative residual =  3.124737e-07
PMG: contraction number =  2.831984e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.026000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.058000e+01
Vpmg_setPart:  lower corner = (-52.5172, 26.6942, 54.6805)
Vpmg_setPart:  upper corner = (38.9632, 128.839, 142.831)
Vpmg_setPart:  actual minima = (-52.5172, 26.6942, 54.6805)
Vpmg_setPart:  actual maxima = (38.9632, 128.839, 142.831)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 1.000000e-02
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 27 (Setup timer)..
Setting up PBE object...
Vpbe_ctor2:  solute radius = 39.9413
Vpbe_ctor2:  solute dimensions = 56.539 x 62.406 x 54.016
Vpbe_ctor2:  solute charge = -4
Vpbe_ctor2:  bulk ionic strength = 0
Vpbe_ctor2:  xkappa = 0
Vpbe_ctor2:  Debye length = 0
Vpbe_ctor2:  zkappa2 = 0
Vpbe_ctor2:  zmagic = 6773.76
Vpbe_ctor2:  Constructing Vclist with 75 x 75 x 75 table
Vclist_ctor2:  Using 75 x 75 x 75 hash table
Vclist_ctor2:  automatic domain setup.
Vclist_ctor2:  Using 2.5 max radius
Vclist_setupGrid:  Grid lengths = (66.592, 72.865, 64.633)
Vclist_setupGrid:  Grid lower corner = (-40.073, 41.334, 66.439)
Vclist_assignAtoms:  Have 5732586 atom entries
Vacc_storeParms:  Surf. density = 10
Vacc_storeParms:  Max area = 254.469
Vacc_storeParms:  Using 2584-point reference sphere
Setting up PDE object...
Vpmp_ctor2:  Using meth = 1, mgsolv = 0
Setting PDE center to local center...
Vpmg_ctor2:  PMG chose nx = 97, ny = 97, nz = 65
Vpmg_ctor2:  PMG chose nlev = 4
Vpmg_ctor2:  PMG chose nxc = 13, nyc = 13, nzc = 9
Vpmg_ctor2:  PMG chose nf = 611585, nc = 1521
Vpmg_ctor2:  PMG chose narr = 702964, narrc = 91379
Vpmg_ctor2:  PMG chose n_rpc = 500, n_iz = 250, n_ipc = 500
Vpmg_ctor2:  PMG chose nrwk = 8822477, niwk = 750
Vpmg_ctor2:  Filling boundary with old solution!
VPMG::focusFillBound -- New mesh mins = -43.683, 37.724, 62.829
VPMG::focusFillBound -- New mesh maxs = 30.129, 117.809, 134.682
VPMG::focusFillBound -- Old mesh mins = -52.5172, 26.6942, 54.6805
VPMG::focusFillBound -- Old mesh maxs = 38.9632, 128.839, 142.831
Vpmg_fillco:  filling in source term.
fillcoCharge:  Calling fillcoChargeSpline2...
Vpmg_fillco:  filling in source term.
Vpmg_fillco:  marking ion and solvent accessibility.
fillcoCoef:  Calling fillcoCoefMol...
Vpmg_fillco:  done filling coefficient arrays
Vnm_tstop: stopping timer 27 (Setup timer).  CPU TIME = 3.440000e+00
Vnm_tstart: starting timer 28 (Solver timer)..
Vnm_tstart: starting timer 30 (NEWDRIV2: fine problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: fine problem setup).  CPU TIME = 9.000000e-02
Vnm_tstart: starting timer 30 (NEWDRIV2: coarse problem setup)..
Vnm_tstop: stopping timer 30 (NEWDRIV2: coarse problem setup).  CPU TIME = 1.800000e-01
Vnm_tstart: starting timer 30 (NEWDRIV2: solve)..
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.766000e+01
PMG: iteration =  0
PMG: relative residual =  1.000000e+00
PMG: contraction number =  1.000000e+00
NEWTON: damping enabled...
NEWTON: using errtol_s:  6.678504e+06
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 1.884000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.785990e+05
PMG: contraction number = , 6.785990e+05
NEWTON: attempting damping, relres =  9.144849e-02
NEWTON: attempting damping, relres =  5.414741e-01
NEWTON: damping accepted, relres =  9.144849e-02
NEWTON: damping disabled...
PMG: iteration =  1
PMG: relative residual =  9.144849e-02
PMG: contraction number =  9.144849e-02
NEWTON: using errtol_s:  6.107391e+05
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.029000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 8.573826e+04
PMG: contraction number = , 8.573826e+04
PMG: iteration =  2
PMG: relative residual =  1.155415e-02
PMG: contraction number =  1.263460e-01
NEWTON: using errtol_s:  7.716444e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.129000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.553548e+04
PMG: contraction number = , 1.553548e+04
PMG: iteration =  3
PMG: relative residual =  2.093573e-03
PMG: contraction number =  1.811966e-01
NEWTON: using errtol_s:  1.398193e+04
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.231000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 3.194813e+03
PMG: contraction number = , 3.194813e+03
PMG: iteration =  4
PMG: relative residual =  4.305353e-04
PMG: contraction number =  2.056462e-01
NEWTON: using errtol_s:  2.875332e+03
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.332000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 6.832645e+02
PMG: contraction number = , 6.832645e+02
PMG: iteration =  5
PMG: relative residual =  9.207721e-05
PMG: contraction number =  2.138668e-01
NEWTON: using errtol_s:  6.149380e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.433000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.624746e+02
PMG: contraction number = , 1.624746e+02
PMG: iteration =  6
PMG: relative residual =  2.189519e-05
PMG: contraction number =  2.377916e-01
NEWTON: using errtol_s:  1.462271e+02
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.534000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 4.166186e+01
PMG: contraction number = , 4.166186e+01
PMG: iteration =  7
PMG: relative residual =  5.614382e-06
PMG: contraction number =  2.564208e-01
NEWTON: using errtol_s:  3.749567e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.635000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 1.219450e+01
PMG: contraction number = , 1.219450e+01
PMG: iteration =  8
PMG: relative residual =  1.643340e-06
PMG: contraction number =  2.927019e-01
NEWTON: using errtol_s:  1.097505e+01
Vnm_tstop: stopping timer 40 (MG iteration).  CPU TIME = 2.737000e+01
PMG: iteration =  0
PMG: relative residual = , 1.000000e+00
PMG: contraction number = , 1.000000e+00
PMG: iteration =  1
PMG: relative residual = , 3.946208e+00
PMG: contraction number = , 3.946208e+00
PMG: iteration =  9
PMG: relative residual =  5.317938e-07
PMG: contraction number =  3.236055e-01
Vnm_tstop: stopping timer 30 (NEWDRIV2: solve).  CPU TIME = 1.030000e+01
Vnm_tstop: stopping timer 28 (Solver timer).  CPU TIME = 1.060000e+01
Vpmg_setPart:  lower corner = (-43.683, 37.724, 62.829)
Vpmg_setPart:  upper corner = (30.129, 117.809, 134.682)
Vpmg_setPart:  actual minima = (-43.683, 37.724, 62.829)
Vpmg_setPart:  actual maxima = (30.129, 117.809, 134.682)
Vpmg_setPart:  bflag[FRONT] = 0
Vpmg_setPart:  bflag[BACK] = 0
Vpmg_setPart:  bflag[LEFT] = 0
Vpmg_setPart:  bflag[RIGHT] = 0
Vpmg_setPart:  bflag[UP] = 0
Vpmg_setPart:  bflag[DOWN] = 0
Vnm_tstart: starting timer 29 (Energy timer)..
Vnm_tstop: stopping timer 29 (Energy timer).  CPU TIME = 0.000000e+00
Vnm_tstart: starting timer 30 (Force timer)..
Vnm_tstop: stopping timer 30 (Force timer).  CPU TIME = 0.000000e+00
Vgrid_writeDX:  Opening virtual socket...
Vgrid_writeDX:  Writing to virtual socket...
Vgrid_writeDX:  Writing comments for ASC format.
Vnm_tstop: stopping timer 26 (APBS WALL CLOCK).  CPU TIME = 2.859000e+01

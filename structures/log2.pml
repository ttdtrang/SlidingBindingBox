cmd.edit()
cmd.edit()
origin grid_center
cmd.enable('2HU4A')
cmd.select(None,"2HU4A")
cmd.create(None,"2HU4")
cmd.enable('sel04')
cmd.disable('sel04')
cmd.enable('sel04')
cmd.disable('sel04')
rotate [-1,1,0], -22.5, obj05
_ set_view (\
_     0.707700670,   -0.107751958,    0.698202014,\
_     0.706447005,    0.098594077,   -0.700850070,\
_     0.006684741,    0.989250183,    0.145893544,\
_     0.000000000,    0.000000000, -240.375000000,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   184.790084839,  295.959930420,  -20.000000000 )
cmd.edit()
cmd.disable('rotation_axis')
cmd.disable('M2')
cmd.disable('M1')
cmd.disable('B0_plane')
cmd.disable('B_plane')
cmd.back()
cmd.mstop()
cmd.enable('A_plane',1)
cmd.disable('A_plane')
cmd.disable('obj05')
cmd.enable('obj05',1)
rotate [-1,1,0], -22.5, obj05
_ set_view (\
_     0.708145797,   -0.104786843,    0.698202014,\
_     0.706027865,    0.101552129,   -0.700850070,\
_     0.002541265,    0.989269435,    0.145893544,\
_     0.000000000,    0.000000000, -240.375000000,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   184.790084839,  295.959930420,  -20.000000000 )
cmd.forward()
cmd.forward()
cmd.forward()
cmd.forward()
cmd.forward()
cmd.forward()
cmd.forward()
cmd.forward()
cmd.mplay()
cmd.mstop()
cmd.mplay()
cmd.mstop()
cmd.enable('B0_plane',1)
cmd.disable('B0_plane')
cmd.enable('B_plane',1)
cmd.mplay()
cmd.mstop()
cmd.back()
cmd.back()
cmd.disable('B_plane')
cmd.enable('B_plane',1)
cmd.enable('B0_plane',1)
cmd.disable('obj05')
cmd.enable('obj05',1)
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
rotate [-1,1,0], -22.5, obj05
_ set_view (\
_     0.746144056,   -0.036636420,    0.664727867,\
_     0.665683925,    0.054791734,   -0.744205236,\
_    -0.009151557,    0.997798800,    0.065266602,\
_     0.000000000,    0.000000000, -240.375000000,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   184.790084839,  295.959930420,  -20.000000000 )
cmd.disable('B_plane')
cmd.disable('B0_plane')
cmd.enable('A_plane',1)
cmd.disable('A_plane')
cmd.enable('A0_plane',1)
cmd.disable('A0_plane')
cmd.enable('B_plane',1)
cmd.disable('B_plane')
cmd.delete("obj05")
cmd.enable('2HU4',1)
cmd.enable('sel04')
cmd.disable('sel04')
cmd.enable('B_plane',1)
cmd.enable('B0_plane',1)
cmd.enable('M1',1)
cmd.enable('M2',1)
cmd.mplay()
cmd.mstop()
cmd.back()
cmd.back()
cmd.disable('B0_plane')
cmd.disable('B_plane')
cmd.delete("B_plane")
cmd.delete("B0_plane")
cmd.delete("M1")
cmd.delete("M2")
cmd.enable('rotation_axis',1)
cmd.delete("rotation_axis")
cmd.enable('sel04')
cmd.delete("sel04")
cmd.edit()
cmd.edit()
run /home/Ubuntu/tk/Programs/pymol/scripts/draw_plane_cgo.py
draw_plane B_plane, b1, b2, b3, b4
draw_plane B0_plane, b1, b3, b4, b2
cmd.disable('B_plane')
cmd.disable('B0_plane')
cmd.enable('A_plane',1)
cmd.enable('A0_plane',1)
cmd.edit()
save 3complexes.pse,format=pse
cmd.edit()
cmd.create(None,"2HU4")
rotate [-1,1,0],-22.5, obj06
_ set_view (\
_     0.563692272,   -0.218099177,    0.796622694,\
_     0.821651101,    0.049734220,   -0.567793667,\
_     0.084225170,    0.974636078,    0.207238004,\
_     0.000000000,    0.000000000, -323.920623779,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   289.406799316,  358.434478760,  -20.000000000 )
cmd.disable('A_plane')
cmd.disable('A0_plane')
cmd.enable('B0_plane',1)
cmd.enable('B_plane',1)
cmd.disable('B_plane')
cmd.disable('B0_plane')
cmd.disable('2HU4')
cmd.edit()
cmd.edit()
cmd.edit()
pseudoatom M1, pos=[16.42, 54.8, 100.43]
show spheres, M1
pseudoatom M2, pos=[28.58, 99.88, 100.43]
cmd.delete("M2")
pseudoatom M2, pos=[-28.58, 99.88, 100.43]
show spheres, M2
cmd.color(4,"M1")
cmd.color(4,"M2")
cmd.edit()
wizard measurement
refresh_wizard
cmd.edit("(M1`1)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(M2`1)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.set_wizard()
cmd.hide("labels"    ,"measure01")
cmd.delete("obj06")
cmd.enable('2HU4',1)
cmd.edit()
cmd.edit()
cmd.edit()
cmd.create(None,"2HU4")
origin grid_center
cmd.edit()
cmd.edit()
rotate [-1,1,0], -15, obj07
_ set_view (\
_    -0.431936204,   -0.067955092,    0.899287105,\
_     0.900893152,   -0.079008043,    0.426732659,\
_     0.042061277,    0.994535387,    0.095352940,\
_     0.014453851,    0.022056738, -223.808578491,\
_    -6.079999924,   77.379997253,  100.430000305,\
_   189.287200928,  258.314910889,  -20.000000000 )
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.edit()
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.delete("obj07")
cmd.create(None,"2HU4")
_special 107,801,544,0
rotate [-1,1,0], 15, obj08
_ set_view (\
_     0.745897472,   -0.098870903,    0.658607721,\
_     0.665814042,    0.087347075,   -0.740952075,\
_     0.015735213,    0.991239667,    0.130981624,\
_     0.000000000,    0.000000000, -231.074813843,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   196.560958862,  265.588653564,  -20.000000000 )
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.delete("obj08")
cmd.create(None,"2HU4")
rotate [-1,1,0], -20, obj09
_ set_view (\
_     0.745897472,   -0.098870903,    0.658607721,\
_     0.665814042,    0.087347075,   -0.740952075,\
_     0.015735213,    0.991239667,    0.130981624,\
_     0.000000000,    0.000000000, -236.277236938,\
_    -6.065554619,   77.372543335,  100.407913208,\
_   201.763381958,  270.791137695,  -20.000000000 )
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('2HU4')
cmd.wizard("renaming","measure01")
refresh_wizard
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(8,922,539,0)
cmd.get_wizard().do_key(97,922,539,0)
cmd.get_wizard().do_key(120,922,539,0)
cmd.get_wizard().do_key(105,922,539,0)
cmd.get_wizard().do_key(115,922,539,0)
cmd.get_wizard().do_key(49,922,539,0)
cmd.get_wizard().do_key(13,922,539,0)
pseudoatom M3, pos=[16.42, 99.88, 100.43]
pseudoatom M4, pos=[-28.58, 54.88, 100.43]
show sphere, M3 or M4
cmd.color(4,"M3")
cmd.color(4,"M4")
cmd.edit()
wizard measurement
refresh_wizard
cmd.edit("(M3`1)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(M4`1)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.hide("labels"    ,"measure01")
cmd.wizard("renaming","measure01")
refresh_wizard
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(8,475,176,0)
cmd.get_wizard().do_key(97,475,176,0)
cmd.get_wizard().do_key(120,475,176,0)
cmd.get_wizard().do_key(105,475,176,0)
cmd.get_wizard().do_key(115,475,176,0)
cmd.get_wizard().do_key(50,475,176,0)
cmd.get_wizard().do_key(13,475,176,0)
cmd.create(None,"obj09")
rotate [1,1,0], 30, obj10
_ set_view (\
_    -0.707621276,   -0.044335753,    0.705129385,\
_     0.706529200,   -0.037951905,    0.706624448,\
_    -0.004559524,    0.998267949,    0.058186814,\
_     0.000000000,    0.000000000, -192.528076172,\
_    -6.065543175,   77.372596741,  100.407997131,\
_   155.435287476,  229.620880127,  -20.000000000 )
cmd.disable('obj09')
cmd.edit()
cmd.edit()
cmd.edit()
cmd.enable('obj09',1)
cmd.disable('obj09')
cmd.enable('obj09',1)
cmd.disable('obj09')
cmd.edit()
rotate [1,1,0], 15, obj10
_ set_view (\
_    -0.711480737,   -0.019529611,    0.702361107,\
_     0.702600241,   -0.007139021,    0.711506546,\
_    -0.008873394,    0.999756575,    0.018807657,\
_     0.000000000,    0.000000000, -192.528076172,\
_    -6.065543175,   77.372596741,  100.407997131,\
_   155.435287476,  229.620880127,  -20.000000000 )
cmd.disable('obj10')
cmd.edit()
cmd.edit()
cmd.edit()
cmd.edit()
cmd.edit()
cmd.edit()
cmd.edit()
cmd.enable('obj10',1)
cmd.disable('obj10')
cmd.enable('obj09',1)
cmd.enable('2HU4',1)
cmd.disable('axis1')
cmd.enable('axis1',1)
cmd.disable('obj09')
cmd.edit("(2HU4`2982)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(2HU4`2981)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(2HU4`2982)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(2HU4`2979)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(2HU4`2973)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.edit("(2HU4`2965)",None,None,None,pkresi=0,pkbond=0)
cmd.get_wizard().do_pick(0)
cmd.set_wizard()
cmd.disable('measure02')
cmd.disable('measure03')
cmd.enable('measure03',1)
cmd.disable('measure03')
cmd.disable('measure04')
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.show("surface"   ,"2HU4")
cmd.edit()
cmd.enable('obj09',1)
cmd.show("surface"   ,"obj09")
cmd.disable('2HU4')
cmd.enable('2HU4',1)
cmd.disable('obj09')
cmd.edit()
cmd.enable('grid_center',1)
cmd.edit()
set_name grid_center, grid_center_whole
set_name box, box_whole
cmd.edit()
cmd.edit()
cmd.disable('box_whole')
cmd.enable('box_whole',1)
cmd.edit()
set_name box_whole, box
cmd.edit()

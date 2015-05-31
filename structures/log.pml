cmd.create(None,"2HU4A",zoom=0)
cmd.create(None,"3CL0A",zoom=0)
cmd.create(None,"3CL2A",zoom=0)
delete 2HU4
cmd.disable('obj01')
cmd.enable('obj01',1)
cmd.wizard("renaming","obj01")
refresh_wizard
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(50,700,267,0)
cmd.get_wizard().do_key(72,700,267,1)
cmd.get_wizard().do_key(89,700,267,1)
cmd.get_wizard().do_key(8,700,267,0)
cmd.get_wizard().do_key(85,700,267,1)
cmd.get_wizard().do_key(52,700,267,0)
cmd.get_wizard().do_key(13,700,267,0)
delete 3CL0
set_name obj02,3CL0
delete 3CL2
set_name obj03,3CL2
align 3CL0,2HU4
align 3CL2,2HU4
align 3CL2,3CL0
cmd.show_as("cartoon"   ,"all")
cmd.set('seq_view',1)
_ cmd.select("_seeker","(2HU4`1461|2HU4`1462|2HU4`1463|2HU4`1464|2HU4`1465|2HU4`1466|2HU4`1467|2HU4`1468|2HU4`1469|2HU4`1470)")
cmd.select('sele','none')
_ cmd.select("sele","((byresi(?sele)) or byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
_ cmd.select("_seeker","(3CL0`1461|3CL0`1462|3CL0`1463|3CL0`1464|3CL0`1465|3CL0`1466|3CL0`1467|3CL0`1468|3CL0`1469|3CL0`1470|3CL0`1471|3CL0`1472)")
_ cmd.select("sele","((byresi(?sele)) or byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
cmd.disable('3CL2')
select H274,resn his and resi 274 and 2HU4
select Y274,resn tyr and resi 274 and 3CL0
select N294,resn asn and resi 294 and 2HU4
select S294,resn ser and resi 294 and 3CL2
show stick, H274
show stick, Y274
show stick, N294
show stick, S294
_ cmd.select("_seeker","(2HU4`2963|2HU4`2964|2HU4`2965|2HU4`2966|2HU4`2967|2HU4`2968|2HU4`2969|2HU4`2970|2HU4`2971|2HU4`2972|2HU4`2973|2HU4`2974|2HU4`2975|2HU4`2976|2HU4`2977|2HU4`2978|2HU4`2979|2HU4`2980|2HU4`2981|2HU4`2982)")
_ cmd.select("S294","((byresi(?S294)) or byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
_ cmd.select("_seeker","(2HU4`2963|2HU4`2964|2HU4`2965|2HU4`2966|2HU4`2967|2HU4`2968|2HU4`2969|2HU4`2970|2HU4`2971|2HU4`2972|2HU4`2973|2HU4`2974|2HU4`2975|2HU4`2976|2HU4`2977|2HU4`2978|2HU4`2979|2HU4`2980|2HU4`2981|2HU4`2982)")
_ cmd.select("S294","((byresi(?S294)) and not byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
cmd.disable('S294')
_ cmd.select("_seeker","(2HU4`2963|2HU4`2964|2HU4`2965|2HU4`2966|2HU4`2967|2HU4`2968|2HU4`2969|2HU4`2970|2HU4`2971|2HU4`2972|2HU4`2973|2HU4`2974|2HU4`2975|2HU4`2976|2HU4`2977|2HU4`2978|2HU4`2979|2HU4`2980|2HU4`2981|2HU4`2982)")
cmd.select('sele','none')
_ cmd.select("sele","((byresi(?sele)) or byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
cmd.show("sticks"    ,"sele")
cmd.disable('sele')
_ cmd.select("_seeker","(3CL0`2966|3CL0`2967|3CL0`2968|3CL0`2969|3CL0`2970|3CL0`2971|3CL0`2972|3CL0`2973|3CL0`2974|3CL0`2975|3CL0`2976|3CL0`2977|3CL0`2978|3CL0`2979|3CL0`2980|3CL0`2981|3CL0`2982|3CL0`2983|3CL0`2984|3CL0`2985)")
cmd.select('sele','none')
_ cmd.select("sele","((byresi(?sele)) or byresi(_seeker))",enable=1)
_ cmd.delete("_seeker")
cmd.show("sticks"    ,"sele")
cmd.disable('sele')
cmd.disable('3CL0')
stereo 
cmd.enable('3CL0',1)
save /home/Ubuntu/tk/Projects/BindingPathway/structures/3complexes.pse,format=pse

/p1
H:0 0
T:0 0
touched:enlist T
fn:{do[y;H::H+x;if[1<max abs H-T;touched,:enlist T::H-x]]}
R:fn[1 0;]
L:fn[-1 0;]
U:fn[0 1;]
D:fn[0 -1;]
value each read0`:d09.txt
count distinct touched
/p2
knots:10#enlist 0 0
touched:enlist 0 0
fn:{do[y;knots::(enlist x+first knots),{$[1<max abs y-z;z+signum y-z;z]}[x;]\[x+first knots;1_ knots]; touched,:enlist last knots]}
R:fn[1 0;]
L:fn[-1 0;]
U:fn[0 1;]
D:fn[0 -1;]
value each read0`:d09.txt
count distinct touched

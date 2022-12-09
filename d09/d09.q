rep:{x#enlist y}
knots:rep[10;0 0]
fn:{x:@[x;0;+;y];{$[1<max abs y-z;z+signum y-z;z]}[y;]\[x]}
R:rep[;1 0]
L:rep[;-1 0]
U:rep[;0 1]
D:rep[;0 -1]
f:`:d09.txt
count distinct last each rep[2;0 0] fn\raze value each read0 f /p1
count distinct last each rep[10;0 0] fn\raze value each read0 f /p2

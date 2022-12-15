f:`:d14eg.txt
f:`:d14.txt
paths:{get each " -> "vs x}each read0 f
range2d:{d:signum diff:y-x; res:enlist x; while[not y~last res; res,:d+last res]; res}
rocks:raze {raze range2d ./: -1_ {x{(x;y)}'next x} x}each paths
// paint a picture from rock paths
paint:{o:min x; m:max x; xy:1+m-o; map:xy#prd[xy]#"."; flip map .[;;:;"o"]/(x-\:o)}

// use sparse matrix tracking
// source is 500 0
init:500 0
bounds:(min;max)@\:rocks,enlist init

check:{
    if[not all x within bounds;:0N 0N];
    p:x+/:(0 1;-1 1;1 1);
    r:first where not in[;rocks,sands] p;
    $[null r;x;p r]
    }
sands:(); { while[not 0N 0N~spot:check/[init]; sands,:enlist spot]; count sands }[]

check2:{
    if[x[1]>=1+last max bounds;:x];
    p:x+/:(0 1;-1 1;1 1);
    r:first where not in[;rocks,sands] p;
    $[null r;x;p r]
    }
sands:enlist init; { i:0; while[not init~spot:check2/[init]; i+:1; sands,:enlist spot; if[0=i mod 100;-1 paint sands; -1 ""]]; -1 paint sands; -1 ""; count sands }[]
paint sands
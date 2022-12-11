f:`:d11eg.txt
f:`:d11.txt
`state`op`test`pass set' flip {get each(last": "vs x[1];"{[old]",(last"="vs x[2]),"}";last" "vs x[3];" "sv last each " "vs'x[5 4])} each 7 cut read0 f

fn:{[w;x;y]
    cnt[y]+:count t:0=mod[;test[y]]s:w op[y]x[y];
    x[y]:0#0; d:s group pass[y]t;
    @[x;key d;{x,y};value d]
    }

p1:fn[div[;3];]
cnt:(count state)#0;20{x p1/til count x}/state
prd 2#desc cnt

p2:fn[mod[;prd test];]
cnt:(count state)#0;10000 {x p2/til count x}/state
prd 2#desc cnt

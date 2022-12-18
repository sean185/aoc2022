f:`:d18eg.txt
f:`:d18.txt
points:"J"$"," vs/: read0 f
p1:{(6*count x)-sum raze in[;x] each x+/:\:(1 0 0;-1 0 0;0 1 0;0 -1 0;0 0 1;0 0 -1)}

/ part 2 strategy: flood fill grid to see which points can be touched or reach from outside
empty:([]point:except[;points] (cross/)til each 1+max points; visited:0b)
res:{
    nbs:exec raze point+/:\:(1 0 0;-1 0 0;0 1 0;0 -1 0;0 0 1;0 0 -1) from x where curr;
    if[0=count nbs;:x];
    x:update curr:0b from x where curr;
    x:update visited:1b, curr:1b from x where point in nbs, not visited;
    x
    }/[update visited:1b, curr:1b from empty where i=0]
// add back bubbles to get "solid" object
p1 points,exec point from res where not visited

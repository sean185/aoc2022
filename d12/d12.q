heights:"S",.Q.a,"E"
dulr:(1 0;-1 0;0 1;0 -1)
f:`:d12eg.txt
f:`:d12.txt
topo:heights?read0 f
find:{raze (til count topo),/:'where each (heights?x)=topo}

// do a bfs from goal back
run:{
    start::find "E";
    end::x;
    touched::start;
    allpaths::([]path:enlist start);
    while[0=count select from allpaths where any each end in/: path; // return because found!
        allpaths::ungroup select fn each path from allpaths];
    min exec -1+count each path from select path from allpaths where any each end in/:path
    }

// part 1
run find "S"

// part 2, any path will do!
run find "a"
prse:{get ssr[;"[[]";"enlist("] ssr[;"]";")"] ssr[;",";";"] x}
pairs:2 cut packets:prse each {x where not x~\:""}read0`:d13eg.txt
cmp:{
    while[any count each (x;y);
        if[0=count x;:1b]; 
        if[0=count y;:0b]; 
        a:first x; b:first y; 
        $[any 0<=(type a;type b);
            [
                if[0>type a;a:enlist a];
                if[0>type b;b:enlist b];
                res:.z.s[a;b];
                if[not (::)~res;:res]
            ];
            [
                if[a<b;:1b]; 
                if[a>b;:0b];
            ]
        ];
        x:1_x; y:1_y
    ];
 }
/ p1
sum 1+where cmp ./: pairs
/ p2
prd {1+where in[;0 1] iasc sum each 1b~''x cmp\:/:x}(enlist enlist 2;enlist enlist 6),packets

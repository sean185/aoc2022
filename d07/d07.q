fn:{[ctx;inp]
    $[inp like "$ ls";
        (first ctx;::);
      inp like "$ cd ..";
        (-1_first ctx;::);
      inp like "$ cd *";
        (first[ctx],last `$" " vs inp;::);
      inp like "dir *";
        [v:("SS";" ")0:inp;(first ctx;v 0;v 1;0)]; // `typ`name
        [v:("JS";" ")0:inp;(first ctx;`file;v 1;v 0)] // `size`name
    ]
 }

allfiles:`path`typ`name`size!/:{x where not null x@'1} ()fn\read0`:d07eg.txt

while[count select from allfiles where typ=`dir, size=0;
    map:exec sum size by path from allfiles;
    allfiles:update size:map[path,'name] from allfiles where typ=`dir, size=0, (count each path)=max(count each path)
 ]

/p1
exec sum size from allfiles where typ=`dir, size <= 100000
/p2
free:70000000-exec sum size from allfiles where 1=count each path
exec first size from `size xasc select name, size from allfiles where typ=`dir, size>=30000000-free

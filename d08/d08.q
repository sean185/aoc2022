trees:"J"$''read0`:d08.txt
// look right, left, down, up
search:{[trees]
    (
    fn trees;
    reverse each fn reverse each trees;
    flip fn flip trees;
    flip reverse each fn reverse each flip trees
    )
 }
/p1
fn:{differ each maxs each x}
sum raze (|/) search[trees]
/p2
c:{(-1+count x)^first 1+where (1_x)>=first x}
fn:{flip{c each z _' x}[x]\[();til count x]}
max raze (*/) search[trees]

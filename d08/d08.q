trees:"J"$''read0`:d08eg.txt
trees:"J"$''read0`:d08.txt
/p1
fn:{differ each maxs each x}
// look right, left, down, up
sum raze (|/)(
    fn trees;
    reverse each fn reverse each trees;
    flip fn flip trees;
    flip reverse each fn reverse each flip trees
    )

/p2
c:{(-1+count x)^first 1+where (1_x)>=first x}
fn:{flip{c each z _' x}[x]\[();til count x]}
// look right, left, down, up
max raze (*/)(
    fn trees;
    reverse each fn reverse each trees;
    flip fn flip trees;
    flip reverse each fn reverse each flip trees
    )

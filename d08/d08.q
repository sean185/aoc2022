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
fn:{(-1+count x)^first 1+where (1_x)>=first x}
max raze (*/)(
    // look right
    flip{fn each z _' x}[trees]\[();til count trees];
    // look left
    reverse each flip{fn each z _' x}[reverse each trees]\[();til count trees];
    // look down
    {fn each z _' x}[flip trees]\[();til count trees];
    // look up
    flip reverse each flip {fn each z _' x}[reverse each flip trees]\[();til count trees]
    )

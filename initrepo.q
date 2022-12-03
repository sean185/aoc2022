// while within aoc2022/
dirs:"d",/:"0"^-2$string 1+til 25
files:raze {` sv' (hsym`$x),/:`$x,/:(".txt";"eg.txt")} each dirs
{x 0: enlist""} each files
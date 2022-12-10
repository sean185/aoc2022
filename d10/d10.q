fn:{x,:i:last x;$[y like "addx*";x,:i+last(" J";" ")0:y;x]}
output:(1#1)fn/read0`:d10.txt
/p1
sum {x*output@-1+x}20+40*til 6
/p2
" #"40 cut (240#til 40){x in -1 0 1+y}'240#output
r:{(x 0)+til 1+(-/)x 1 0}
p:{r asc "J"$"-"vs x}''
p1:{any x~\:(inter/)x}
p2:{0<count(inter/)x}

f:`:d04eg.txt
vals:p "," vs'read0 f
sum p1 each vals
sum p2 each vals

f:`:d04.txt
vals:p "," vs'read0 f
sum p1 each vals
sum p2 each vals

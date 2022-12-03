d:({" " sv string raze x} each `A`B`C cross `X`Y`Z)!4 8 3 1 5 9 7 2 6
sum d read0`:d02.txt

/ X is lose, Y is draw, Z is win
d:`X`Y`Z!(`A`B`C!3 1 2;`A`B`C!1 2 3;`A`B`C!2 3 1)
sum {v:`$" " vs x; t:(`X`Y`Z!0 3 6)v[1]; t+sum d[v[1]][v[0]]} each read0`:d02.txt

// alt part 1
`X`Y`Z set' 1 2 3
A:{y+x y}1 2 3!3 6 0
B:{y+x y}1 2 3!0 3 6
C:{y+x y}1 2 3!6 0 3
sum value each read0`:d02.txt

// alt part 2
`X`Y`Z set' 0 3 6
A:{y+x y}0 3 6!3 1 2
B:{y+x y}0 3 6!1 2 3
C:{y+x y}0 3 6!2 3 1
sum value each read0`:d02.txt



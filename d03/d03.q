// part 1
sum 1+(.Q.a,.Q.A)?raze {distinct (inter/) (`long$count[x]%2) cut x} each read0`:d03.txt
// part 2
sum {first 1+(.Q.a,.Q.A)?c:(inter/) x}each 3 cut read0`:d03.txt

// rewrite
scores:{1+(.Q.a,.Q.A)?x}
txt:read0`:d03.txt
// part 1
part1:{first(inter/)2 0N#x}
sum scores part1 each txt
// part 2
part2:{first(inter/)x}
sum scores part2 each 3 cut txt

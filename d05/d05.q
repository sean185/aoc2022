input:"\n" vs/: "\n\n" vs "\n" sv read0 `:d05eg.txt
steps:"J"$(" "vs/: input[1])@\:1 3 5
init:1 2 3!`$''trim flip reverse -1_ input[0]@\:1 5 9
fn:{[n;st;ed] stack:reverse neg[n]#init[st]; init[st]:neg[n]_ init[st]; init[ed],:stack}
fn ./: steps
raze string value last each init

input:"\n" vs/: "\n\n" vs "\n" sv read0 `:d05.txt
init:(1+til 9)!`$''trim flip reverse -1_ input[0]@\:1 5 9 13 17 21 25 29 33
steps:"J"$(" "vs/: input[1])@\:1 3 5
fn:{[n;st;ed] stack:reverse neg[n]#init[st]; init[st]:neg[n]_ init[st]; init[ed],:stack}
fn ./: steps
raze string value last each init


input:"\n" vs/: "\n\n" vs "\n" sv read0 `:d05eg.txt
steps:"J"$(" "vs/: input[1])@\:1 3 5
init:1 2 3!`$''trim flip reverse -1_ input[0]@\:1 5 9
fn:{[n;st;ed] stack:neg[n]#init[st]; init[st]:neg[n]_ init[st]; init[ed],:stack}
fn ./: steps
raze string value last each init

input:"\n" vs/: "\n\n" vs "\n" sv read0 `:d05.txt
init:(1+til 9)!`$''trim flip reverse -1_ input[0]@\:1 5 9 13 17 21 25 29 33
steps:"J"$(" "vs/: input[1])@\:1 3 5
fn:{[n;st;ed] stack:neg[n]#init[st]; init[st]:neg[n]_ init[st]; init[ed],:stack}
fn ./: steps
raze string value last each init

// rewrite
input:"\n" vs/: "\n\n" vs "\n" sv read0 `:d05.txt
init:(!). flip {("J"$last x;-1_ x)} each except[;enlist""] {x@'where each x in .Q.an} flip input[0]
steps:"J"$(" "vs/:input[1])@\:1 3 5
p1:{[x;n;st;ed] x[ed]:(reverse n#x[st]),x[ed]; x[st]:n _x[st]; x}
raze first each {p1[x] . y}/[init;steps]
p2:{[x;n;st;ed] x[ed]:(n#x[st]),x[ed]; x[st]:n _x[st]; x}
raze first each {p2[x] . y}/[init;steps]


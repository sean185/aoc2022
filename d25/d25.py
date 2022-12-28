snafu_chars = '=-012'

def snafu_to_dec(snafu):
    total = 0
    idx = reversed(range(len(snafu)))
    for i, c in zip(idx, snafu):
        p = snafu_chars.index(c)-2
        total += p*5**i
    return total

def baseX(base, num):
    res = list()    
    while num >= base:
        divisor, remainder = divmod(num, base)
        res.insert(0, remainder)
        num = divisor
    res.insert(0, divisor)
    result = ''.join([str(i) for i in res])
    return res

def base_snafu(num):
    i = 0
    offset = 2
    while 2*5**i < num:
        i += 1
        offset += 2*5**i
    return ''.join([snafu_chars[x] for x in baseX(5, num + offset)])

print(base_snafu(2022))
print(base_snafu(12345))
print(base_snafu(314159265))

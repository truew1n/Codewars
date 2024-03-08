def count(num):
    res = 0
    while num:
        b = num.bit_length()-1 
        x = 1<<b
        num -=  x
        res += b*(x>>1)+1 + num
    return res

def countOnes(left, right): 
    return count(right) - count(left-1)

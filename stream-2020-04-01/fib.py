import sys
num = int(sys.argv[1])


def fib(i):
    if i is 0:
        return 0
    
    total = 1
    prev_total = 0
    for i in range(i-1):
        temp = total + prev_total
        prev_total = total
        total = temp

    return(total)

print(fib(num))

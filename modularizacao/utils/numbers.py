def fatorial(num=0):
    f = 1
    for i in range(1,num + 1):
        f *= i
    return f

def soma(*num):
    return sum(num)

def media(*num):
    return sum(num) / len(num) 
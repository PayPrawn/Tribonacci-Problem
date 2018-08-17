def tribonacci(a, b, c, n): 
    total = ('[' + str(a) + ', ' + str(b) + ', ' + str(c) + ', ')
    x = 1
    for f in range(n):
        if x < n: 
            c = a + b + c
            c = str(c)
            total = total + c + ', '
    print(c)
tribonacci(1, 1, 1, 4)
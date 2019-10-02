def numerics(n):
    L = list(map(int,str(n)))
    return L
def kaprekar_step(L):
    return int(''.join(map(str,sorted(L,reverse=True)))) - int(''.join(map(str,sorted(L))))
def kaprekar_check(n):
    s = (str(n))
    kaperkar_false = {100, 1000, 100000}
    return (len(s) in [3, 4, 6]) and (len(set(s)) > 1) and (n not in kaperkar_false)
def kaprekar_loop(n):
    kaperkar_true = {6174, 495, 549945, 631764}
    sixnum = {1}
    while n not in kaperkar_true:
        if kaprekar_check(n) == False:
            print ("Ошибка! На вход подано число ", n,", не удовлетворяющее условиям процесса Капрекара", sep = '')
            break
        elif len(str(n)) == 6 and n in sixnum:
            print ('Следующее число - ', n, ', кажется процесс зациклился...', sep = '')
            break
        elif len(str(n)) == 6 and n not in sixnum:
            sixnum.add(n)
            print (n)
        elif len(str(n)) != 6:
            print (n)
        n = kaprekar_step(numerics(n))
    if n in kaperkar_true:
            print (n)

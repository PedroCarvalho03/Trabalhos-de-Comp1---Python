def resto1(x,y):
    if x>y:
        return resto1(x-y,y)
    elif x<y:
        return x
    else:
        return 0

#print(resto1(2,5))
#print(resto1(10,3))
#print(resto1(10,4))
#print(resto1(10,5))

def montante2(valor,taxa,tempo):
    if tempo>0:
        return montante2(valor,taxa,tempo-1)*(taxa/100) + montante2(valor,taxa,tempo-1)
    else :
        return valor
#print(montante2(1000,1,3))
#print(montante2(1010,1,2))
#print(montante2(1020.1,1,1))
#print(montante2(200,4,4))
#print(montante2(208,4,3))
#print(montante2(216.32,4,2))
#print(montante2(224.9728,4,1))
#print(montante2(400,5,2))
#print(montante2(400,5,3))
#print(montante2(400,5,4))
 
def catalan3(n):
    if n == 0:
        return 1
    else :
        return 2*(((2*n-1)*(catalan3(n-1))/(n+1)))

#print(catalan3(0))
#print(catalan3(1))
#print(catalan3(2))
#print(catalan3(3))
#print(catalan3(9))

        
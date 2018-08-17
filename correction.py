#Autor: Ma. Fernanda Rodriguez 
#Fecha:17/08/18
def isPrimefor(num):
    flag=True
    
    for i in range (2, num/2+1):
        if num%i==0:
            flag=False
            break 
    return flag

p= input('dame un numero')
if isPrimefor(p):
    print "es primo"
else:
    print "no es primo"
  

#imprima todos os números primos de 1 até 1000
# saída: 2,3,5, . . . , 991,997. 



for numero in range (2,1000+1):
  primo = 1
  for divisor in range(2,numero+1):
    if numero % divisor == 0 :
      primo = primo + 1
  if primo == 2:
    print(numero)
  

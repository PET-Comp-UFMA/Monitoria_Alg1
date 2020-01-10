print("digite um numero de 4 digitos")
num = io.read("*n")

n1 = math.floor(num/1)%10
n2 = math.floor(num/10)%10
n3 = math.floor(num/100)%10
n4 = math.floor(num/1000)%10


print(n1..n2..n3..n4)

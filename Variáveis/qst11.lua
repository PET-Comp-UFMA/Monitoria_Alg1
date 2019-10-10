print("informe a idade em anos meses e dias")
anos = io.read("*n")
meses = io.read("*n")
dias = io.read("*n")
total = dias
 
total = total + (anos*365) + (meses*30)
 
print(total .. " dias")

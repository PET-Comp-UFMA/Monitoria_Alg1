cont = 0
print("Quantos numeros voce deseja verificar")
n = io.read("*n")
print("Agora digite os " .. n .. " numeros")
for i=1, n do
 teste = io.read("*n")
 if(teste >= 10 and teste <= 20) then
   cont = cont +1
 end
end
print(cont .. " numeros dentro do intervalo\n" .. n-cont .. " numeros fora do intervalo")

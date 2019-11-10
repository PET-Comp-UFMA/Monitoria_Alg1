cont = 0
print("digite 10 valores")
 
for i=1,10 do
 valor = io.read("*n")
 if(valor < 0) then
   cont = cont + 1
 end
end
 
print(cont .. " números negativos")

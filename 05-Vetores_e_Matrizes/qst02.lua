lista = {}
 
for i=1,100 do
 lista[i] = math.random(100);
end
 
maior = lista[1]
menor = lista[1]
for i=2,100 do
 if(lista[i] > maior) then
   maior = lista[i]
 end
 if(lista[i] < menor) then
   menor = lista[i]
 end
end
 
print(menor, maior)

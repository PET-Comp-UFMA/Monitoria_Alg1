vet = {}
for i=1,30 do
 vet[i] = math.random(30)
end
 
num = io.read ( "*n" )
count=0
for j=1,30 do
 print(vet[j])
 if(vet[j] == num) then
   count = count+1
 end
end
print("O numero ".. num .." aparece "..count.." vezes")

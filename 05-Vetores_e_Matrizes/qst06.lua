vet={}
count = 0
soma = 0
for i=1,10 do
    vet[i] = io.read("*n")
    if vet[i]%2==0 then
        count = count+1
        soma = soma + vet[i]
    end
end

print("Existem "..count.." elementos pares")

if count == 0 then
    print("Não há elementos pares")
else    
    for i=1,10 do
        if vet[i] % 2 == 0 then
            print(vet[i])
        end
    end
    print("Soma de pares = "..soma)
end

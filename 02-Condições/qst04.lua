km = io.read("*n")
l = io.read("*n")

print(km/l.." km/l")

if km/l > 14 then
    print("É econômico")
else
    print("Não é econômico")
    if(km/l<9) then
        print("Sr.Antônio, melhor trocar de carro")
    end
end

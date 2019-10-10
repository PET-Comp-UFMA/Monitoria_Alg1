saldoinit = io.read("*n")
debt = io.read("*n")
cred =io.read("*n")

saldo = (saldoinit-debt)+cred

if saldo > 0 then
    print("Saldo positivo em R$ "..string.format("%.2f",saldo))
elseif saldo < 0 then
    saldo = saldo * -1--[[Eliminando o sinal negativo--]]
    print("Saldo negativo em R$"..string.format("%.2f",saldo)) 
else
    print("Saldo zero")
end

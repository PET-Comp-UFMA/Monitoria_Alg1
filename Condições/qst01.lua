print("Informe Peso e Altura.")
altura, peso = io.read("*n","*n")
imc = peso / (altura*altura)
print(imc)
msg = ""
if imc<=18 then
    msg = "Abaixo do Peso"
elseif imc >18 and imc<25 then
    msg = "Peso Normal"
elseif imc>=25 and imc<30 then
    msg = "Sobrepeso"
else
    msg = "Obeso Mórbido"
end
print(msg)

temp = io.read("*n")
escala = io.read()


if (escala == " \"Celsius\"") then 
  result = (temp - 32) * (5/9) 
  escalResult = " °C"
elseif (escala == " \"Kelvin\"") then
  result = (temp - 32) * (5/9) + 273,15
  escalResult = " K"
end

if result ~= nil then
  print(result..escalResult)
else
  print("Entrada Invalida")
end


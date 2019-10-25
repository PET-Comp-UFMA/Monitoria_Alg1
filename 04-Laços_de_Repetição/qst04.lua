n=0
maior = n
menor = 0
contmenor = 0
contmaior = 0

while n >=0 do
  print("Digite um numero")
  n = io.read("*n")

  if menor == 0 then
    menor = n
  end

  if n > maior then 
    maior = n
    contmaior = 1
  elseif n == maior then
    contmaior = contmaior + 1
  end

  if n > 0 then
    if n < menor then 
      menor = n
      contmenor = 1
    elseif n == menor then
      contmenor = contmenor + 1
    end
  end
  
end 

print("O maior numero é ".. maior .. ", e ocorreu " .. contmaior .. " vez(es).")

print("O menor numero é ".. menor .. ", e ocorreu " .. contmenor .. " vez(es).")

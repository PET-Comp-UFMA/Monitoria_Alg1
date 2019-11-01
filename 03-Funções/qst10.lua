function fibonacci(n)
  if(n == 1) then
    return 0;
  elseif(n == 2) then
    return 1;
  else 
    return fibonacci(n-1) + fibonacci (n-2)
  end
end

print("Digite a quantidade de numeros da sequencia")
n = io.read("*n")

for i=1, n do
  io.write(fibonacci(i) .. " ")
end

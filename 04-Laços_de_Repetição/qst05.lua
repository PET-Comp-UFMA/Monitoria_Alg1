print("Digite um numero")
n = io.read("*n")
somadiv = 0

for i=1, n/2 do
  if n%i == 0 then
    somadiv = somadiv + i
  end 
end
print(somadiv)

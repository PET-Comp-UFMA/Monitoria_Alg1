print("Digite um numero")
n = io.read("*n")

for i=n, n+n-1 do
  io.write(i^2 .. ", ")
end

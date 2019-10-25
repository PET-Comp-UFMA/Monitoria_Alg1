function fatorial(n)
  if(n == 1) then
    return 1;
  else return n*fatorial(n-1)
  end
end

print("Digite um numero")
n = io.read("*n")

print(fatorial(n))

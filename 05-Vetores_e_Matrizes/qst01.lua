print("Digite um numero")
n = io.read("*n")
v = {}

for i =1, n do 
  v[i] = math.random(20)
  io.write(v[i] .. " ")
end

print("")

for i =1, n do 
  if v[i]%2 == 0 then
    v[i] = (v[i] -1) *2
  else 
    v[i] = v[i] * 3
  end
  io.write(v[i] .. " ")
end

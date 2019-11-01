function ordenavetor(v)
  for i = 1, #v do
    for j = i+1, #v do
      if(v[i] > v[j]) then
        v[i],v[j] = v[j],v[i]
      end
    end
  end
  return v
end

v = {}
print("Digite os 10 numeros do vetor")

for i=1, 10 do
  v[i] = io.read("*n")
end

ordenavetor(v)

for i=1, 10 do 
  io.write(v[i] .. " ")
end 

function visiveisFila(fila)
  visiveis = 1
  ultimovisto = fila[1]

  for i = 2, #fila do 
    prox = fila[i]
    if ultimovisto < prox then --proximo da fila visivel
      ultimovisto = prox
      visiveis = visiveis + 1
    end
  end

  return visiveis
end

print("Existem quantas pessoas na fila?")
n = io.read("*n")
fila = {}

for i=1, n do
  fila[i] = io.read("*n")
end

print(visiveisFila(fila) .. " Pessoas visiveis na fila")

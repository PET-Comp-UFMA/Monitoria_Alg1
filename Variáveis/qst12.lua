print("Digite o tempo em segundos")
segs = io.read("*n")
horas = math.floor(segs/3600)
segs = segs%3600
min = math.floor(segs/60)
segs = segs%60
 
print(horas .. ":" .. min .. ":" .. segs)

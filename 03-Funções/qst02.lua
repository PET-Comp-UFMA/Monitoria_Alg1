function mediaAluno(nota1, nota2, nota3, tipoMedia)
	if tipoMedia == "aritmetica" then
		return (nota1 + nota2 + nota3) / 3 
	elseif tipoMedia == "ponderada" then
			return (2*nota1 + 4*nota2 + 2*nota3) / 8
	end
	return -1 -- Erro, caso a string seja diferente
end

print("Insira as médias:")
a,b,c = io.read("*n","*n","*n")
str = io.read("*line")
print(mediaAluno(a,b,c,str))

matrix = {}
linhas = io.read("*n")
colunas = io.read("*n")
for i=1,linhas do
    matrix[i] = {}
    for j=1,colunas do
        matrix[i][j] = math.random(9)
    end
end
print("Matriz gerada:")
for i=1,linhas do
    for j=1,colunas do 
        io.write(matrix[i][j].." ")
    end
    print("")
end

print("Matriz transposta:")

for i=1,colunas do
    for j=1,linhas do 
        io.write(matrix[j][i].." ")
    end
    print("")
end

print("Diagonal principal:")

for i=1,linhas do
    for j=1,colunas do 
        if j==i then
            print(matrix[i][j])
        elseif j<i then
            io.write("  ")
        end
    end
end

print("triângulo superior:")
for i=1,linhas do 
    for j=1,colunas do
        if j>i then
            io.write(matrix[i][j].." ")
        else
            io.write("  ")
        end
    end
    print("")
end

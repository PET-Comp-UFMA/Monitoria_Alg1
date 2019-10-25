function tempAposentadoria(idade, tempoTrabalho)
    if idade >= 65 and tempoTrabalho >= 30 then
        return true
    else
        return false
    end
end
idade = io.read("*n")
tempoTrabalho = io.read("*n")

print(tempAposentadoria(idade,tempoTrabalho))

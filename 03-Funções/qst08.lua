function tempAposentadoria(idade, tempoTrabalho)
    if idade >= 65 and tempoTrabalho >= 30 then
        return true
    else
        return false
    end
end


function aposentadoria2019(trabalhador,nasc,anoIngresso)
    if tempAposentadoria(2019-nasc,2019-anoIngresso) == true then
        print(trabalhador.." tem aposentadoria em 2019")
    else
        print(trabalhador.." não tem  aposentadoria em 2019")
        print("Trabalhe mais "..30-(2019-anoIngresso).." anos.")
        if 2019-nasc<65 then
            print("Muito novo para se aposentar.")
        end
    end
end


trabalhador = io.read()
anoNasc = io.read("*n")
anoIngresso = io.read("*n")

aposentadoria2019( trabalhador, anoNasc, anoIngresso)

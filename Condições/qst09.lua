scorpion = 0
subzero = 0


print("Round 1")
input=io.read()

if input == "true" then
    scorpion = scorpion + 1
    print("Scorpion")
elseif input == "false" then
    subzero = subzero + 1
    print("Subzero")
else
    print("Toasty!!!")
    return -1
end

print("Round 2")
input = io.read()

if input == "true" then 
    scorpion = scorpion + 1
    print("Scorpion")
elseif input == "false" then
    subzero = subzero + 1
    print("Subzero")
else
    print("Toasty!!!")
    return -1
end

print("Round 3")
input = io.read()

if input == "true" then 
    scorpion = scorpion + 1
    print("Scorpion")
elseif input == "false" then
    subzero = subzero + 1
    print("Subzero")
else
    print("Toasty!!!")
    return -1
end

if scorpion ~= 3 and subzero ~= 3 then
    print("Round 4")
    input = io.read()
    
    if input == "true" then
        scorpion = scorpion + 1
        print("Scorpion")
    elseif input == "false" then
        subzero = subzero + 1
        print("Subzero")
    else
        print("Toasty!!!")
        return -1
    end
    
    if scorpion ~= 3 and subzero ~= 3 then
        print("Final Round")
        input = io.read()
        if input == "true" then
            print("O vencedor da luta é Scorpion!")
        elseif input == "false" then
            print("O vencedor da luta é Subzero!")
        else
            print("Toasty!!!")
            return -1
        end
    else
        if scorpion == 3 then
            print("O vencedor da luta é Scorpion!")
        else
            print("O vencedor da luta é Subzero!")
        end
    end

else
    if scorpion == 3 then
        print("O vencedor da luta é Scorpion!")
    else
        print("O vencedor da luta é Subzero!")
    end
end


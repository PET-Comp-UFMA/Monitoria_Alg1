honda = 0
blanka = 0


print("Round 1")
input=io.read()

if input == "true" then
    honda = honda + 1
    print("Honda")
elseif input == "false" then
    blanka = blanka + 1
    print("Blanka")
else
    print("Toasty!!!")
    return -1
end
print("Round 2")
input = io.read()

if input == "true" then 
    honda = honda + 1
    print("Honda")
elseif input == "false" then
    blanka = blanka + 1
    print("Blanka")
else
    print("Toasty!!!")
    return -1
end

print("Round 3")
input = io.read()

if input == "true" then 
    honda = honda + 1
    print("Honda")
elseif input == "false" then
    blanka = blanka + 1
    print("Blanka")
else
    print("Toasty!!!")
    return -1
end

if honda ~= 3 and blanka ~= 3 then
    print("Round 4")
    input = io.read()
    
    if input == "true" then
        honda = honda + 1
        print("Honda")
    elseif input == "false" then
        blanka = blanka + 1
        print("Blanka")
    else
        print("Toasty!!!")
        return -1
    end
    
    if honda ~= 3 and blanka ~= 3 then
        print("Final Round")
        input = io.read()
        if input == "true" then
            print("O vencedor da luta é Honda!")
        elseif input == "false" then
            print("O vencedor da luta é Blanka!")
        else
            print("Toasty!!!")
            return -1
        end
    else
        if honda == 3 then
            print("O vencedor da luta é Honda!")
        else
            print("O vencedor da luta é Blanka!")
        end
    end

else
    if honda == 3 then
        print("O vencedor da luta é Honda!")
    else
        print("O vencedor da luta é Blanka!")
    end
end


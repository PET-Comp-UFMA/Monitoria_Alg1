honda = 0
blanka = 0

print("Round 1")
input=io.read()

if input == "true" then
    honda = honda + 1
    print("Honda")
else
    blanka = blanka + 1
    print("Blanka")
end

print("Round 2")
input = io.read()

if input == "true" then 
    honda = honda + 1
    print("Honda")
else
    blanka = blanka + 1
    print("Blanka")
end

if honda~=2 and blanka~=2 then
    print("Final Round")
    input = io.read()
    if input == "true" then
        print("O vencedor da luta é Honda!")
    else
        print("O vencedor da luta é Blanka!")
    end
else
    if honda == 2 then
        print("O vencedor da luta é Honda!")
    else
        print("O vencedor da luta é Blanka!")
    end
end

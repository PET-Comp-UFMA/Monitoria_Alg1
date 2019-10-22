function primo(n)
    countDiv = 2
    if n%2 == 0 and n~=2 then
        countDiv = countDiv+1
    elseif n%3 == 0 and n~=3 then
        countDiv = countDiv+1
    end
    if countDiv>2 then
        print("false")
    else 
        print("true")
    end
end
n = io.read("*n")

primo(n)

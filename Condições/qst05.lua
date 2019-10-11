a = io.read("*n")
b = math.random(1,10)
if(a<=10 and a>=0)  then  
    if(a%b==0) then
        print(a.." é divisível por "..b)
    else 
        print(a.." não é divisível por "..b)
        print("Resto = "..a%b)
    end
end

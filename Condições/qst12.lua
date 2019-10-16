n1 = io.read("*n")
n2 = io.read("*n")
n3 = io.read("*n")

if n1>n2 and n1>n3 then
    print(n1.." é o maior")
elseif n2>n1 and n2>n3 then
    print(n2.." é o maior")
else
    print(n3.." é o maior")
end

n1 = io.read("*n")
n2 = io.read("*n")
n3 = io.read("*n")

if n1>n2 and n1>n3 then
    print(n1.." eh o maior")
elseif n2>n1 and n2>n3 then
    print(n2.." eh o maior")
else
    print(n3.." eh maior")
end

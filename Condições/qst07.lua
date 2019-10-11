n = io.read("*n")

if n>=0 and n<=10 then
    print(n*n)
elseif n<0 then
    print(-1*n)
else
    print(math.sqrt(n))
end

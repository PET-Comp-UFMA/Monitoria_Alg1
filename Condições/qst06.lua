a = io.read("*n")
math.randomseed(os.time())

b = math.random(2,10)

flag = true

if a%b == 0 then
    print(flag)
else
    flag = false
    print(flag)
end
print(b)

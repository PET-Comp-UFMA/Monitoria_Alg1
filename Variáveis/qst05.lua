a,b = io.read("*n","*n")
-- r = math.floor(a/b) está vetado
print((a - a%b)/b)

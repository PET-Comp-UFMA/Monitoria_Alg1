a,b,c = io.read("*n","*n","*n")
d = 0 -- Variavel auxiliar

--permuta entre a e b
d = a
a = b
b = d
print("A = " .. a .. ", B = " .. b .. ", C = " .. c)
--permuta entre b e c
d = b
b = c
c = d
print("A = " .. a .. ", B = " .. b .. ", C = " .. c)
--permuta entre b e a
d = b
b = a
a = d
print("A = " .. a .. ", B = " .. b .. ", C = " .. c)
--permuta entre a e c
d = a
a = c
c = d
print("A = " .. a .. ", B = " .. b .. ", C = " .. c)
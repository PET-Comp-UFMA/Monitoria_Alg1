l1 = io.read("*n")
l2 = io.read("*n")
l3 = io.read("*n")

if l1<l2+l3 and l2<l1+l3 and l3<l2+l2 then
    if l1 == l2 and l2 == l3 then 
        print("Equilátero")
    elseif l1 == l2 or l1 == l3 or l2 == l3 then
        print("Isóceles")
    else
        print("Escaleno")
    end
else
    print("ERRO!!!")
end

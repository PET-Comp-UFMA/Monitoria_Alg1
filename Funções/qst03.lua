function squareArea(x1,y1,x2,y2,x3,y3,x4,y4)
    maiorX = x1

    if x2>maiorX then
        maiorX = x2
    elseif x3>maiorX then
        maiorX = x3
    elseif x4>maiorX then
        maiorX = x4
    end 
    
    menorX = x1
    if x2<menorX then
        menorX = x2
    elseif x3<menorX then
        menorX = x3
    elseif x4<menorX then
        menorX = x4
    end

    maiorY = y1
    if y2>maiorY then
        maiorY = y2
    elseif y3>maiorY then
        maiorY = y3
    elseif y4>maiorY then
        maiorY = y4
    end 
    
    menorY = y1
    if y2<menorY then
        menorY = y2
    elseif y3<menorY then
        menorY = y3
    elseif y4<menorY then
        menorY = y4
    end

    if maiorX-menorX ~= maiorY-menorY then
        print("Não formou um quadrado.")
    else
        print(math.pow(maiorX-menorX,2))
    end
end

x1 = io.read()
y1 = io.read()
x2 = io.read()
y2 = io.read()
x3 = io.read()
y3 = io.read()
x4 = io.read()
y4 = io.read()

squareArea(x1,y1,x2,y2,x3,y3,x4,y4)

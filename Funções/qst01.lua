function IdealWeight(h,g)
    if g == "m" or g =="M" then
        return (72.3*h)-58.2
    elseif g == "f" or g == "F" then
        return (62.7*h)-45.2
    end
end

h = io.read()
g = io.read()

print( string.format("%.2f",IdealWeight(h,g)).." Kg" )

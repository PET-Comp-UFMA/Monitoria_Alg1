mat = {}
for i=1,3 do
 mat[i] = {}
end
 
for i=1,3 do
 for j=1,3 do
   mat[i][j] = io.read("*n")
 end
end
 
for i=1,3 do
 for j = 4,5 do
   mat[i][j] = mat[i][j-3]
 end
end
 
dprin = 0
dsec = 0
aux = 1
k=0
 
for i=1,3 do
 for j=1,3 do
   aux = aux * mat[j][j+k]
   --print("\n" .. aux .. '\n')
 end
 dprin = dprin + aux
 aux = 1
 k = k+1
end
k=0
 
for i=1,3 do
 l=1
 for j=3,1,-1 do
   aux = aux * mat[l][j+k]
   l = l+1
 end
 dsec = dsec + aux
 aux = 1
 k = k+1
end
 
print("\no determinate eh " .. dprin-dsec)

#part1
input = "91212129"
sum=0
int(input)
length = len(input)
for i in range(length):
   if input[i] == input[(i+1)%length]:
      sum+=int(input[i])
    
print sum


#Part2
input = "1212"
sum=0
length = len(input)
for i in range(length):
   if input[i] == input[(i+length/2)%length]:
      sum+=int(input[i])
    
print sum

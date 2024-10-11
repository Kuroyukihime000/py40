input_data = open('input.txt' , 'r')
data = input_data.read()

a = 2 
b = 1
N = int(data)
while b <N:
    a = a * 2
    b = b +1

output = open('output.txt', 'w')
output.write(str(a))



input_data.close()
output.close()

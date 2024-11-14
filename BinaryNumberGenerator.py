import random 

binary_1= 1
binary_2 = 0

binary_full = [binary_1, binary_2] * 4

sample = (binary_full)
random.shuffle(sample)

binary_number = '     '.join(map(str, sample))

print(binary_number)  


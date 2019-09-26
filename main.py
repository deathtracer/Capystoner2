import add
import multiplication
import div
import sys
import sub

input_1 = int(sys.argv[1])
input_2 = int(sys.argv[2])

print("1: Addtion\n2: Subtration\n3: Multiplication\n4: Division\nEnter the number of operation.")

process = int(sys.argv[3])

if process == 1: 
    add.add(input_1, input_2)
elif process == 2:
    sub.sub(input_1, input_2)
elif process == 3:
    multiplication.mul(input_1, input_2)
elif process == 4:
    div.divide(input_1,input_2) 
else 
    print("Please select between 1 and 4 only")

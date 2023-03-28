num= int(input("Enter any number : "))
for i in range(num):
    print(" * " * num)

for i in range(num):
    print("   "*(num-i)+" * "*(i+1+i))
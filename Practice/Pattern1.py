for i in range(3):
    for j in range(3):
        print(" * ",end="")
    print(" ")

print("**************************************************")

for i in range(3):
    for j in range(i+1):
        print(" * ",end="")
    print(" ")

print("**************************************************")

for i in range(3):
    for j in range(3-i):
        print(" * ",end="")
    print(" ")

print("**************************************************")
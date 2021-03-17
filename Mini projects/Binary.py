InputData=input("Text to Binary and Octal:")

#Binary
print("Binary")
for x in InputData:
    print(x+"->"+format(ord(x), "b"))


#Octal
print("\nOctal")

for x in InputData:
    print(x+"->"+format(ord(x), "0"))

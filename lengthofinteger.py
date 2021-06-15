def functionIntLength(number):
    if number==0:
        return 1
    length=0
    if number<0:
        number*=-1

    while number > 0:
        number %= 10
        length += 1
    return length 


number=int(input("Enter the number:"))
length = functionIntLength(number)
print(f"length of numner = {length}")
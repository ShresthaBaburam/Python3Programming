def functionIntLength(number):
    len=0
    if number<0:
        number*=(-1)

    while number > 0:
        number %= 10
        len += 1
    return len


def functionSumDigit(number):
    
    while functionIntLength(number)>1:
        sum =0
        while number>0:
            rem = number % 10
            sum += rem
            number //= 10
        number=sum
    return number


number=int(input("Enter the number:"))
sum = functionSumDigit(number)
print(f"Sum of digit = {sum}")
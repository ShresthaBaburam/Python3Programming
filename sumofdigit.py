def functionSumDigit(number):
    sum =0
    while number>0:
        rem = number % 10
        sum += rem
        number //= 10
    return sum


number=int(input("Enter the number:"))
sum = functionSumDigit(number)
print(f"Sum of digit = {sum}")
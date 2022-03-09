#this program turns digits into binary
import math

def decimalToBinary(num):
    if num >= 1:
        decimalToBinary(num // 2)
    print(num % 2, end ='')

number = int(input("Enter any number (no decimals allowed): "))

decimalToBinary(number)


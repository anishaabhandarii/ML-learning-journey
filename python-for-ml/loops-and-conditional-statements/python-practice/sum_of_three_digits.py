# three_digit_num = input("Enter a three-digit number: ")
# digit1 = int(three_digit_num[0])
# digit2 = int(three_digit_num[1])
# digit3 = int(three_digit_num[2])
# sum_of_digits = digit1 + digit2 + digit3
# print("The sum of the digits is:", sum_of_digits)

# Easy way to calculate the sum of digits of a three-digit number using a loop:
three_digit_num = input("Enter a three-digit number: ")
sum_of_digits = 0
for digit in three_digit_num:  #loops through each character in the string representation of the number
    sum_of_digits += int(digit)
print("The sum of the digits is:", sum_of_digits)

# Another way to calculate the sum of digits of a three-digit number:
three_digit_num = int(input("Enter a three-digit number: ")) 
hundreds_digit = three_digit_num // 100 #integer division to get the hundreds digit
tens_digit = (three_digit_num // 10) % 10 # integer and then modulo division to get the tens digit  
ones_digit = three_digit_num % 10
sum_of_digits = hundreds_digit + tens_digit + ones_digit
print("The sum of the digits is:", sum_of_digits)

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
temp = first_num
first_num = second_num
second_num = temp
print("After swapping:")
print("First number:", first_num)
print("Second number:", second_num)

# Easy way python allows you to swap two numbers without using a temporary variable. You can do this in a single line of code using tuple unpacking. Here's how you can do it:
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
first_num, second_num = second_num, first_num
print("After swapping:")
print("First number:", first_num)   
print("Second number:", second_num)
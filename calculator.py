
# Name: Nwoye Luke Nnamdi
# Reg: 2017364060
# Dept: ECE 
# Course: ECE 541
# Lecturer: Engr Dozie

print('Select Operation to perform')
print('1. ADD')
print('2. SUBSTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')

operation = input()

if operation == '1':
    #code for add
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The result of ' + str(num1) + ' + ' + str(num2)+ ' = ' + str(num1 + num2))

elif operation == '2':
    #code for substract
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The result of ' + str(num1) + ' - ' + str(num2)+ ' = ' + str(num1 - num2))

elif operation == '3':
    #code for multiply
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The result of ' + str(num1) + ' * ' + str(num2)+ ' = ' + str(num1 * num2))

elif operation == '4':
    #code for division
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The result of ' + str(num1) + ' / ' + str(num2)+ ' = ' + str(num1 / num2))

else:
    print('Invalid entry')
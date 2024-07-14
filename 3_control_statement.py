
# If statements
value = int(input('Enter the value : ')) 
output = ''
if value > 100 :
    output = 'Value : ' + str(value) + ' is greater than 100'
elif value < 100 :
    output = 'Value : ' + str(value) + ' is less than 100'
else:
    output = 'Value : ' + str(value) + ' is equal to 100'
print(output)

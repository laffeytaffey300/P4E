#defines starting values
sum = 0
count = 0
max = None
min = None

#loop
while True:
    input_val= input('Enter a number: ')
    if input_val == 'done': 
        break #allows user to exit loop by entering 'done'
    try:
        float_num = float(input_val) #checks if input value is number
    except:
        print('bad data') #exception handling when input is not a number
        continue #skips updating stats for bad input
    sum = sum + float_num
    if count == 0: #sets max and min to first input value on first iteration
            max = float_num
            min = float_num
    else:
        if float_num > max: max = float_num
        if float_num < min: min = float_num
    count = count + 1

#print output
if count > 0: #checks at least one valid entry has been made
    print(
        '\nTotal:', sum,
        '\nCount:', count,
        '\nAverage:', sum/count,
        '\nMax:', max,
        '\nMin:', min)
else: print("\nOops! You didn't enter any valid data before entering 'done', there's nothing to calculate!" ) #error message if no valid entries
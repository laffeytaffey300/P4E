#defines starting values
sum = 0
count = 0

#loop
while True:
    input_val= input('Enter a number: ')
    try:
        float_num = float(input_val) #checks if input value is number
        sum = sum + float_num
        count = count + 1
    except:
        if input_val == 'done': 
            break #allows user to exit loop by entering 'done'
        print('bad data') #exception handingling when input is not a number

#print output
if count > 0: #checks at least one valid entry has been made
    print('Total:', sum)
    print('Count:', count)
    print('Average:', sum/count)
else: print("Oops! You didn't enter any valid data before entering 'done'" ) #error message if no valid entries
#asks user to enter hours and rate
#prints error if input for hours or rate is not numeric
hours = input('Enter Hours:'))
try:
    hours=float(hours)
    rate = input('Enter Rate:')
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
#calculates pay with 1.5*rate over 40 hours
if hours > 40:
    print('Pay:', 40*rate+((hours-40)*(rate*1.5)))
else: print('Pay:', hours*rate)

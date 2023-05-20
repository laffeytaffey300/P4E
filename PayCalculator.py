#calculates straight pay for up to 40 hours
#calculates 1.5 rate over 40 hours
def computepay(hours,rate):
    if hours > 40:
        pay = 40*rate+((hours-40)*(rate*1.5))
    else: pay = hours*rate
    return pay
#asks user to enters hours and rate
#converts inputs to float, prints error and quits if unable
hours = input('Enter Hours:')
try:
    hours=float(hours)
    rate = input('Enter Rate:')
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
#calculates and prints pay based on given inputs
pay = computepay(hours, rate)
print('Pay: ', pay)

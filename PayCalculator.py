#calculates straight pay for up to 40 hours
#calculates 1.5 rate over 40 hours
def computepay(hours,rate):
    if hours > 40:
        pay = 40*rate+((hours-40)*(rate*1.5))
    else: pay = hours*rate
    return pay
#asks user to enters hours and rate
#converts inputs to float, prints error and quits if unable
input_hours = input('Enter Hours:')
try:
    float_hours=float(input_hours)
    input_rate = input('Enter Rate:')
    float_rate = float(input_rate)
except:
    print('Error, please enter numeric input')
    quit()
#calculates and prints pay based on given inputs
computed_pay = computepay(float_hours, float_rate)
print('Pay: ', computed_pay)

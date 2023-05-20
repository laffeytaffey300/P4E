hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
if hours > 40:
    print('Pay:', 40*rate+((hours-40)*(rate*1.5)))
else: print('Pay:', hours*rate)

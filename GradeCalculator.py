#function: prints error message and quits
def badscore():
    print('Bad Score')
    quit()  
#function: returns grade for a score between 0 and 1
#prints error for scores out of range
def computegrade(score):
    if score >= 1.0 or score <=0.0:
        badscore()
    elif score >= 0.9: grade = 'A'
    elif score >= 0.8: grade = 'B'
    elif score >= 0.7: grade ='C'
    elif score >= 0.6: grade ='D'
    else: grade ='F'
    return grade
#prints grade based on score
#prints error and quits for nonnumeric inputs
score = input('Enter Score: ')
try:
    score = float(score)
except:
    badscore()
print(computegrade(score))

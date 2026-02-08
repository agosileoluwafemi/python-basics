# This program is a grade checker.

print('Welcome to your grade checker.')
print('Kindly enter your score to see your grade.')
score = int(input('Enter your score (0-100): '))
if score >= 70 and score <= 100 :
    print('Grade: A')
elif score >= 60 and score <= 69 :
    print('Grade: B')
elif score >= 50 and score <= 59 :
    print('Grade: C')
elif score >= 45 and score <= 49 :
    print('Grade: D')
elif score >= 40 and score <= 44 :
    print('Grade: E')
elif score >= 0 and score <= 39 :
    print('Grade: F')
else :
    print('Invalid score')

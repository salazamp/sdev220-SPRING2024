
# assign the value 7 to the variable
guess_me =7
# and the value 1 to the variable number.
number =1
#write a while loop
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1
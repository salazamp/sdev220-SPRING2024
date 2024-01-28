import random

#Generate the secret and guess values between 1 and 10...
secret = random.randint(1,10)
guess = random.randint(1,10)

#Print the value of Guess and secret...
print("Guess value is = ", guess)
print("Secret value is = ", secret)

#Now, check if the guess is less than secret then print 'too low!'...
if guess < secret:
    print("too low!")

#Check if the guess is greater than secret then prints 'too high!'...
elif guess > secret:
    print("too high!")

#Otherwise both values are the same so print 'just right!'...
else:
    print("just right!")
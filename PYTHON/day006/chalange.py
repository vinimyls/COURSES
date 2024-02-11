# Write your code below this line 👇
def prime_checker(number):
    prime_found = 1
    if number == 0:
        prime_found = 1
    elif number == 1:
        prime_found = 1
    elif number == 2:
        prime_found = 1
    else:
        for i in range(2, number+1):
            if number % i == 0:
                prime_found = 0
                break

    if prime_found == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Bill value")
bill = float(input())
print("number of people")
people = float(input())
print("percent of tip")
tip = float(input())

total_plus_tip = bill *( 1 + tip/100)
total_per_person = total_plus_tip / people

result = f'{total_per_person:.2f}'

print(result)

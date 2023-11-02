# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
for myNumber in range(32):
  result = str(result) + str(myNumber) + "\n"

print(result)

for myNumber in range(32):
    result = ""
    gameStr = ""
    if (myNumber+1) % 3 == 0:
      gameStr = "Fizz"
    if (myNumber+1) % 5 == 0:
      gameStr = "Buzz"
    if (myNumber+1) % 15 == 0:
      gameStr = "FizzBuzz"
    if gameStr == "":
        result =  str(myNumber+1) + "\n"
    else:
        result =  gameStr + "\n"
    print(result) 

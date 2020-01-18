import random

secret = random.randint(0, 1000) # sets a random number, assigned to variable "secret"

x = 0
y = 10
while x < 10:
  print("=" * 45)
  response = input("Enter a guess, or 'quit': ") # user inputs a guess
  if response.isnumeric(): # input takes this if the input registers as numeric characters
      guess = int(response)
      if guess == secret:
        print("You got it!")
        break
      elif guess < 0:
        x = x
        y = y
        print("Invalid input. Enter a number between 0 and 1000.")
        print("Attempts remaining:", y)
      elif guess > 1000:
        x = x
        y = y
        print("Invalid input. Enter a number between 0 and 1000.")
        print("Attempts remaining:", y)
      elif guess > secret:
        x += 1
        y = y - 1
        print("Too high! Try again.")
        print("Attempts remaining:", y)
        if y == 0:
          print(f"Game over :(\nAnswer: {secret}")
      elif guess < secret:
        x += 1
        y = y - 1
        print("Too low! Try again.")
        print("Attempts remaining:", y)
        if y == 0:
            print(f"Game over :(\nAnswer: {secret}")
      else:
        x += 1
        y = y - 1
        print("Nope, you're wrong.")
        print("Attempts remaining:", y)
        if y == 0:
            print(f"Game over :(\nAnswer: {secret}")
  
  elif response.isalpha(): # input takes this if input registers characters as string
    guess = str(response)
    if guess == "quit":
      break
    elif guess != "quit":
      x = x
      y = y
      print("Invalid input. Enter a number between 0 and 1000.")
      print("Attempts remaining:", y)

  else: # input takes this for anything else, such as negative symbols, floats
    x = x
    y = y
    print("Invalid input. Enter a number between 0 and 1000.")
    print("Attempts remaining:", y)
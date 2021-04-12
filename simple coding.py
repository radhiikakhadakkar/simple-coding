print("Hello People! \n Welcome to Gameiz")

answer= input("Lets play, are you ready (yes/no):")
total_no_of_questions=4
points=0

if answer== "yes":
    answer = input(" 1. What is the capital of India?")
    if answer== "Delhi":
        points += 1
        print("**CORRECT! Well it was an essy one**")
    else:
        print("Oops! Incorrect")


    answer = input("2. What is the output of 3**2")
    if answer == "6":
        points += 1
        print("**CORRECT! Is seems you know basics of Python**")
    else:
        print("INCORRECT")


    answer = input("3. Which city is called the pink city of India")
    if answer == "Jaipur":
        points += 1
        print(" **YEAHH.. It is the correct answer**")
    else:
        print("INCORRECT")

    answer = input("4. Is Python Case Sensitive")
    if answer == "yes":
         points += 1
         print("**You are right!!!**")
    else:
         print("INCORRECT")

print("It was nice playing with you, You scored" , points, "correct questions")
score= (points/total_no_of_questions)*10

print("Score", score)
print("Thank you for playing with us")

         
     
    

# Intro
print("~ Tales of UMBC ~")
print("(A Work of Fiction)")
print()


print("You are a knight in the year 650 CE, and you're trying to become the most famous knight of them all.")
print()
print("You decide to go on an adventure at castle UMBC to earn your glory!")
print()

# Pick a Story
print("You are outside the castle grounds, and see three different people asking for help. You could talk to:")
print("  A. The town's blind man, who needs help getting to the local hospital emergency room")
print("  B. The teacher, who's asking you a question")
print("  C. The king who needs a brave warrior")
  
# Story 1: Multiple Choice Problem  
# # Get input from user
story_choice = input("Who will you talk to? Please select options A through C: ")
print()

if(story_choice.lower() == "a"):
  print("You meet with the town's blind man, who desperately needs to get to the emergency room, some 20 miles away.")
  print("They tell you that the legend is that only one of the town's two forms of mobility works and you have only one choice to make.")
  print("You go with your guts and decide on one of the following:")
  print("  A. HorseCart")
  print("  B. Van")
  print()

  # Get input from user
  choice = input("What do you choose? A. HorseCart or B. Van: ")
  print()
  # Success - Town's Blind man
  if(choice.lower() == "a" and not choice.isdigit()):
    print("Success! You have chosen the right transportation")
    print("The old man is thrilled and rewards you with an ancient sword used by the town's greatest warrior")
    print()
  
# Failure - Town's Blind man 
  elif(choice.lower() == "b"):
    print("Wrong selection! The van's batteries are dead and will therefore not be available for use.")
    print("This will cost the old blind man the needed medical attention to stay alive.")
  elif(choice.isdigit()):
    choice = input("What do you choose? A. HorseCart or B. Van: ")
    print()


# Story 2: Math Problem
elif(story_choice.lower() == "b"):

  # Save correct answer in a variable
  correct_answer = 100
  print()

  print("You meet with the teacher, who is asking you a question.")
  print("'My friend, I have a math problem that no one in this town seems to be able to solve. It is simple, yet thought-provoking and people get it wrong simply for over-thinking it.'")
  print()
  print("The teacher describes the problem as follows:")
  print("'A lady walks into a store and steals $100 from the register without the owner's knowledge. She comes back 5 minutes later and buys $70 worth of goods with the $100 bill. The owner gives her $30 in change. How much did the owner lose in total?")

  # Prompt user for input
  knight_input = input("Please enter the answer to this problem (digits ONLY): ")
  print()  
    
  # Check that they made the correct input
  if(knight_input.isdigit() and int(knight_input) == correct_answer):

    # Success - The teacher
    print("'Correct!' the teacher cries.")
    print("That is impressive. For your help, you will be honored as an outstanding member of our town.")
    print()


  elif(not knight_input.isdigit()):
    # Prompt user for input
    knight_input = input("Please enter the answer to this problem (digits ONLY): ")
    print()
  
  # Failure - The teacher
  else:
    print("That is incorrect!")
    print()

# Story 3: Riddle/Puzzle
elif(story_choice.lower() == "c"):


  print("You meet with the king of UMBC who is looking for a brave warrior.")
  print("He informs you that his kingdom is under a spell by an adversary. And that only a wizard in the woods can save them. There is no time, 'he says. Head south and find her.")
  print()
  print("You head south but find the road to the wizard has vanished. A warrior-like image appears in the sky and tells you to solve a riddle in exchange for him to make a hidden pathway to the wizard")
  print("What two numbers, when added and multiplied, equal four?")
  print("You ponder for a moment. There are multiple answers to this question, aren't there?")
  print("After thinking for a moment, you answer with two numbers...")

  # Create the two numbers
  correctnum1 = 2
  correctnum2 = 2
  
  # Get input from user for both numbers
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))

  # Success - The king
  if(num1 == correctnum1 and num2 == correctnum2):
    print("'Ah yes, 2 and 2 add up and multply to 4! the warrior-like image explained'")
    print("The road to the wizard has once again re-appeared. Go forth my son and save your kingdom.")
  
  # Failure - The king
  else:
    print("That is incorrect my son! You have failed to answer correctly and must be punished as a result. Return to the castle and explain to the king why you could not get the needed help his kingdom desperately needs.")
  print()

print("~ The End ~")

  # elif(num1 != correctnum1 and num2 == correctnum2):
  #   print("Those numbers are incorrect!")
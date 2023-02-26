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
story_choice = input("Who will you talk to? Please select option A through C: ")
print()

if(story_choice == "A"):
  print("You meet with the town's blind man, who desperately needs to get to the emergency room, some 20 miles away.")
  print("They tell you that the legend is that only one of the town's two forms of mobility works and you have only one choice to make.")
  print("You go with your guts and decide on one of the following:")
  print("  A. HorseCart")
  print("  B. Van")
response = input("Please select option A or B: ")
print()

# Success - Town's Blind man
if(response == "A"):
  print("Success! You have chosen the right transportation")
  print("The old man is thrilled and rewards you with an ancient sword used by the town's greatest warrior")

# Failure - Town's Blind man
else:
  print("Wrong selection! The van's batteries are dead and will therefore not be available for use.")
  print("This will cost the old blind man the needed medical attention to stay alive")
print()

if(story_choice == "B"):
  # Story 2: Display Story
  print("You meet with the teacher, who is asking you a question")
  print("'My friend, I have to be honest with you,' he says. Of late, I have been experiencing this lapse in memory and sometimes cannot solve simple math problems.'")
  print("He gestures to a math problem that reads as follows: w = 2 * (3 + 1)")
solution = int(input("Please enter the solution to this problem: "))
print()

# Check if they entered the correct answer
w = 8

# Success - The teacher
if(solution == w):
  print("'Correct!' the teacher cries.")
  print("That is impressive. For your help, you will be honored as an outstanding member of our town.")

# Failure - The teacher
else:
  print("That is incorrect!")
print()

if(story_choice == "C"):
  # Story 3: Display Story
  print("You meet with the king of UMBC,looking for a brave warrior.")
  print("He informs you that his kingdom is under a spell by an adversary. And that only a wizard in the woods can save them. There is no time, 'he says. Head south and find her.")
  print()
  print("You head south but find the way to the wizard has vanished. A warrior-like image appears in the sky and tells you to solve a riddle in exchange for him to make a hidden pathway to the wizard")
print("What two numbers, when added and multiplied, equal four?")
print("You ponder for a moment. There are multiple answers to this question, aren't there?")
print("After thinking for a moment, you answer with two numbers...")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Create the two numbers
correctnum1 = 2
correctnum2 = 2

# Determine if the right numbers were entered
# Success - The king
if(num1 == correctnum1 and num2 == correctnum2):
  print("'Ah yes, 2 and 2 add up and multply to 4! the warrior-like image explained'")

# Failure - The king
elif(num1 != correctnum1 and num2 == correctnum2):
  print("Those numbers are incorrect!")
else:
  print("Wrong! My son, you have failed to answer correctly and must be punished as a result. Return to the castle and explain wto the king why you could not get the needed help his kingdom desperately needs.")
  
def Process():
  if Option == 0:
    print("Exiting...")
    exit()
  elif Option == 1:
    First_Number = input("First number: ")
    Second_Number = input("Second number: ")
    Answer = int(First_Number) + int(Second_Number)
    print("Answer: " + str(Answer))
  elif Option == 2:
    First_Number = input("First number: ")
    Second_Number = input("Second number: ")
    Answer = int(First_Number) - int(Second_Number)
    print("Answer: " + str(Answer))
  elif Option == 3:
    First_Number = input("First number: ")
    Second_Number = input("Second number: ")
    Answer = int(First_Number) * int(Second_Number)
    print("Answer: " + str(Answer))
  elif Option == 4:
    First_Number = input("First number: ")
    Second_Number = input("Second number: ")
    Answer = int(First_Number) / int(Second_Number)
    print("Answer: " + str(Answer))
  Continue = input("Do you want to continue using this program? Yes or No? ")
  if "Yes" in Continue:
    Loop()
  else:
    print("Exiting...")
    exit()
def Loop():
  #Display of options
  print("0: Exit\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
  #Selection of option
  global Option
  Option = input("Pick the arithmetic operator that you wish to use (0,1,2,3,4): ")
  Option = int(Option)
  #Start of process
  Process()
Loop()

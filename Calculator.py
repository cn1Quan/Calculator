def Loop():
  #Display of options
  print("0: Exit\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
  #Selection of option & Rejection of input
  Option = input("Pick the arithmetic operator that you wish to use (0,1,2,3,4): ")
  Option = int(Option)
  #Processing of option
  def Exit():
    if Option == 0:
      exit()
  def Option_Addition():
    if Option == 1:
      First_Number = input("First number: ")
      Second_Number = input("Second number: ")
      Answer = int(First_Number) + int(Second_Number)
      print("Answer: " + str(Answer))
  def Option_Subtraction():
    if Option == 2:
      First_Number = input("First number: ")
      Second_Number = input("Second number: ")
      Answer = int(First_Number) - int(Second_Number)
      print("Answer: " + str(Answer))
  def Option_Multiplication():
    if Option == 3:
      First_Number = input("First number: ")
      Second_Number = input("Second number: ")
      Answer = int(First_Number) * int(Second_Number)
      print("Answer: " + str(Answer))
  def Option_Division():
    if Option == 4:
      First_Number = input("First number: ")
      Second_Number = input("Second number: ")
      Answer = int(First_Number) / int(Second_Number)
      print("Answer: " + str(Answer))
  Option_Addition()
  Option_Subtraction()
  Option_Multiplication()
  Option_Division()
  Continue = input("Do you want to continue using the program (Yes/No)? ")
  if "Yes" in Continue:
    Loop()
  if "No" in Continue:
    print("Exiting...")
Loop()

# Run with python ArnoldDay1.py && java -jar ArnoldC.jar day1_from_python.arnoldc && java day1_from_python

def main():
  # Get puzzle input
  day1Input = open("day1.txt", "r")
  contents = day1Input.readlines()

  # Clear file contents and prepare to append lines
  open("day1_from_python.arnoldc", "w").close()
  arnoldFile = open("day1_from_python.arnoldc", "a")

  # Write: begin main
  arnoldFile.write("IT'S SHOWTIME \n")
  # Write: initialise total
  arnoldFile.write("HEY CHRISTMAS TREE total \n")
  arnoldFile.write("YOU SET US UP 0 \n")
  # Write: load total ready to update it
  arnoldFile.write("GET TO THE CHOPPER total \n")
  arnoldFile.write("HERE IS MY INVITATION 0 \n")

  # Read input
  for line in contents:
    # Write: increment and decrement total,d epending on input
    if line[0] == '+':
      arnoldFile.write("GET UP " + line[1:])
    else:
      arnoldFile.write("GET DOWN " + line[1:])

  # Write: finished modifying total
  arnoldFile.write("\nENOUGH TALK \n")
  # Write: print total
  arnoldFile.write("TALK TO THE HAND total \n")
  # Write: end main
  arnoldFile.write("YOU HAVE BEEN TERMINATED")

if __name__== "__main__":
  main()
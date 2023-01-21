import sys


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



def do_stuff():

  if (len(sys. argv) > 1):
    for x in sys.argv[1:]:
      if  is_number(x) == False:
        print(x + " is not a number")
        print("Please enter a number")
        print("Program terminated")
        exit()

    numbers = [float(x) for x in sys.argv[1:]]
    numbers = [x for x in numbers if x >= 0]
    if len(numbers) == 0:
      print("Division by zero is not possible")
      print("Program terminated")
      exit()
    m = sum(numbers) / len(numbers)
    print(f'{m}')
  else:
    print("no command line argument was passed")
    print("Please pass a command line argument")


do_stuff()


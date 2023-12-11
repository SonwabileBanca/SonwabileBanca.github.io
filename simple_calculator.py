print('===========Welcome to Simple Calculator==============\n\n\n')


# A function to calculate the operation with if statements
def calculate(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 != 0:
      return num1 / num2
    else:
      # Raise error if Divided by zero
      raise ValueError("Error: Division by zero")
  else:
    # Raise an error if the operator is not valid
    raise ValueError("Error: Invalid operator")


# A function that takes the input from the user and passes it to the calculate function
def process_equation_line(line):
  # Extracts numbers and operator from a line in the equation file
  parts = line.split('=')
  if len(parts) == 2:
    equation_part, result_part = parts
    equation_parts = equation_part.split()
    if len(equation_parts) == 3:
      num1, operator, num2 = equation_parts
      result = result_part.strip()
      return float(num1), float(num2), operator, float(result)
  raise ValueError("Error: Invalid equation format")


def read_equations_from_file(file_name):
  try:
    #file_name = 'calculator_history.txt'
    with open(file_name, 'r') as file:
      equations = [process_equation_line(line) for line in file.readlines()]
    return equations
  except FileNotFoundError:
    raise FileNotFoundError(f"Error: File '{file_name}' not found")
  except Exception as e:
    raise RuntimeError(
        f"An unexpected error occurred while reading the file: {e}")


def main():
  equations = None
  while True:
    try:
      option = input(
          "Enter '1' to perform a new calculation or '2' to read equations from a file: "
      )

      if option == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
          raise ValueError("Error: Invalid operator")

        result = calculate(num1, num2, operator)

        print(f"Result: {result}")

        with open('calculator_history.txt', 'a+') as file:
          file.write(f"{num1} {operator} {num2} = {result}\n")

      elif option == '2':
        while True:
          try:
            file_name = input("Enter the name of the file with equations: ")
            equations = read_equations_from_file(file_name)
            break  # Break the loop if file reading is successful
          # If a file is not found then print an error message and continue the loop.
          except FileNotFoundError as fnfe:
            print(fnfe)
          # Keyboard Error occurs and prints the error message
          except KeyboardInterrupt:
            print("\nUser chose to exit. Goodbye!")
            break
          except Exception as e:
            print(f"An unexpected error occurred: {e}")

        if equations:
          print("\nEquations and Results:")
          for eq in equations:
            num1, num2, operator, result = eq
            print(f"{num1} {operator} {num2} = {result}")

      else:
        raise ValueError("Error: Invalid option. Enter '1' or '2'.")
# Value Error rasised as an exception
    except ValueError as ve:
      print(ve)
  # Runtime Error rasised as an exception
    except RuntimeError as re:
      print(re)
    except Exception as e:
      print(f"An unexpected error occurred: {e}")


# A prompt that will ask if you want to continue
    another_attempt = input("Do you want to make another attempt? (yes/no): ")
    if another_attempt.lower() != 'yes':
      break

if __name__ == "__main__":
  main()

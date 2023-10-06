print(
    'Welcome to the Holiday destination\nTell us where you want to go and well calculate the cost.'
)
print('')
print('Destinations and Prices\n==========================')

# Create 3 txt files with the information needed and print out the information
# Open the cities txt file to display the cities

citiesPath = 'cities.txt'
# Initailize the variables
x = 1
price = 0
carPrice = 0
with open(citiesPath, 'r+') as file:
  while True:
    line = file.readline()
    if not line:
      break
    split = line.split("#")
    print(f"{x}. {split[0]} \t {split[1]}")
    x = x + 1

print('\nChoose destination you are travelling to by typing its full name\n\n')

# Use the global function to modify my variables outside my scope.
global dest
dest = input('Enter destination: ')
days = int(
    input(
        '\nHow many days are you going to stay(enter a number e.g. 1,2 12): '))


# Create a function that will find a path of which cities is the user wants
def ReturnHotelByDestination(dest):
  hotelsPath = 'hotels.txt'
  with open(hotelsPath, 'r+') as file:
    while True:
      line = file.readline()
      if not line:
        break

      split = line.split("#")  # remove the Hash in txt files
      # use split variable and index through split[] to take information from txt file

      if (dest == 'Cape Town' and split[0] == 'Cape Town'):
        print(f'\nHere are the available hotels for {dest}')
        print(f"\n{split[1]}\n{split[2]}\n{split[3]}")
        break
      elif (dest == 'East London' and split[0] == 'East London'):
        print(f'\nHere are the available hotels for {dest}')
        print(f"\n{split[1]}\n{split[2]}\n{split[3]}")
      elif (dest == 'Johannesburg' and split[0] == 'Johannesburg'):
        print(f'\nHere are the available hotels for {dest}')
        print(f"\n{split[1]}\n{split[2]}\n{split[3]}")
      elif (dest == 'Gqeberha' and split[0] == 'Gqeberha'):
        print(f'\nHere are the available hotels for {dest}')
        print(f"\n{split[1]}\n{split[2]}\n{split[3]}")
      elif (dest == 'Pretoria' and split[0] == 'Pretoria'):
        print(f'\nHere are the available hotels for {dest}')
        print(f"\n{split[1]}\n{split[2]}\n{split[3]}")

    return dest


ReturnHotelByDestination(dest)
# Prompt the user to enter their choice of Hotels

print(
    'choose one of the above available hotels by writing its full name as written'
)
hotel = input('\nEnter available hotel: ')


def ReturnHotelPriceAndCity(hotel, dest, days):
  #for Cape town:
  #1500 is the travel cost to cape town
  global price
  if (hotel == 'Russel Blue'):
    price = 1500 + (2500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'City Lodge'):
    price = 1500 + (3000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Mojo Hotel'):
    price = 1500 + (5000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")

#for East London the cost is R1700

  if (hotel == 'Garden Court'):
    price = 1700 + (3500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Premier Hotel ICC'):
    price = 1700 + (4000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Premier Regent'):
    price = 1700 + (2500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")

# Johannesburg cost R1800
  if (hotel == 'Four Seasons Hotel'):
    price = 1800 + (2500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Southern Sun Sandton'):
    price = 1800 + (6000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Garden Court'):
    price = 1800 + (4500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")


#Gqeberha cost is R1600
  if (hotel == 'City Lodge'):
    price = 1600 + (3500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Paxton Hotel'):
    price = 1600 + (3000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Road Lodge'):
    price = 1600 + (1500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")

  #Pretoria
  if (hotel == 'Menlyn Hotel'):
    price = 1500 + (4500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Capital Menlyn'):
    price = 1500 + (2000 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")
  elif (hotel == 'Protea Marriot'):
    price = 1500 + (2500 * days)
    print(f'\nTotal due for travel to {dest} and Booking {hotel} is:\nR',
          price, ".00")

  return price
ReturnHotelPriceAndCity(hotel, dest, days)

#Car rental
print('\nWould you like a car rental(Y/N):\nChoose Y or N as your option.')
option = input('\n\nRequire a car hire (Y/N): ')


# The cities and rental prices
# calculate the num of days and company
def ReturnCarCompanyByDestination(dest, days):
  global carPrice

  if (dest == 'Cape Town'):
    carPrice = 240 * days
  elif (dest == 'East London'):
    carPrice = 300 * days
  elif (dest == 'Johannesburg'):
    carPrice = 400 * days
  elif (dest == 'Gqeberha'):
    carPrice = 240 * days
  elif (dest == 'Pretoria'):
    carPrice = 300 * days
  return carPrice


def CalculateTotal(price, carPrice):
  global total
  total = price + carPrice
  return total


if (option == 'y' or option == 'Y'):
  carCompanyPath = 'rentals.txt'
  with open(carCompanyPath, 'r+') as file:
    while True:
      line = file.readline()
      if not line:
        break

      split = line.split("#")
      if (dest == 'Cape Town' and split[0] == 'Cape Town'):
        print(f'\nHere is the available car rental company in {dest}')
        print(f"\n{split[1]}\t{split[2]} per day.")
        carDayPrice = split[2]
        break

      elif (dest == 'East London' and split[0] == 'East London'):
        print(f'\nHere is the available car rental company in {dest}')
        print(f"\n{split[1]}\t{split[2]} per day.")
        carDayPrice = split[2]
        break
      elif (dest == 'Johannesburg' and split[0] == 'Johannesburg'):
        print(f'\nHere is the available car rental company in {dest}')
        print(f"\n{split[1]}\t{split[2]} per day.")
        carDayPrice = split[2]
        break
      elif (dest == 'Gqeberha' and split[0] == 'Gqeberha'):
        print(f'\nHere is the available car rental company in {dest}')
        print(f"\n{split[1]}\t{split[2]} per day.")
        carDayPrice = split[2]
        break
      elif (dest == 'Pretoria' and split[0] == 'Pretoria'):
        print(f'\nHere is the available car rental company in {dest}')
        print(f"\n{split[1]}\t{split[2]} per day.")
        carDayPrice = split[2]
        break

  ReturnCarCompanyByDestination(dest, days)
  CalculateTotal(price, carPrice)
  print(f'\nCar for {days} days is {carPrice}')
  print('Total cost for the Journey:\t ', total)

elif (option == 'n' or option == 'N'):
  print('Total Cost for Traveling: ', price)

else:
  print('Incorrect option selected please try again')

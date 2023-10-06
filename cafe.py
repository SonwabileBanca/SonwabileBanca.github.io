#Menu of the cafe
print('Welcome to the cafe\nHere is the \033[035mMenu\033[0m')
#Menu items
menu = ['Pie','Sandwich','Muffin','Coffie']


#Sock Items
stock = {'Pie': 4,
         'Sanwich': 6,
         'Muffin': 15,
         'Coffie': 7
        }


#Price of one item
price = {'Pie': 17,
          'Sanwich': 14,
          'Muffin': 8,
          'Coffie': 13
          }
#Separate intp lists
print(stock.keys())
print(stock.values())
print(price.keys())
print(price.values())
#iterate the keys
#####
# Total_stock iterate the values
for keys in stock.values():
  total_stock = sum(stock.values())
print('The Total Stock is:\n',total_stock)

#####
#Total price of the items

for keys in price.values():
  total_price = sum(price.values())
print(f'The Total Price is:R{total_price}.')
#####
# Item value and Total costs

item_value = total_stock * total_price
print(f'The Item value is:R',item_value)

    
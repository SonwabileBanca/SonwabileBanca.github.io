print(
  'Freight:\tis R0.36 per km or R0.25 per km\nInsurance:\t Full at R50.00 or Limited at R25.00\nGift:\t Gift cover at R25.00 or No gift cover R0.00\nPriority:\t Priority at R100.00 or R50.00'
)
# Input from user.
parcel_type = input('What is the type of parcel?')

if parcel_type == 'Sleeve' or parcel_type == 'SLEEVE' or parcel_type == 'sleeve':
    parcel_type = 100
  
elif parcel_type == 'Crate' or parcel_type == 'CRATE' or parcel_type == 'crate':
    parcel_type = 400
  
elif parcel_type == 'Box' or parcel_type == 'BOX' or parcel_type == 'box':
    parcel_type = 150


distance = float(input('Enter distance:\t'))
freight_type = input('Enter the mode of travell:\t')
# if freight is air 
if freight_type == 'air' or freight_type == 'AIR':
    freight_cost = 0.36 * distance
    freight_type = freight_cost
    print(f'R{freight_cost}')
# Freight cost if land is chosen  
elif freight_type == 'land' or freight_type == 'LAND':
    freight_cost = 0.25 * distance
    freight_type = freight_cost
    print(f'R{freight_cost}')
# Or else print error  
else:
    print('Error')

# Insurance type
Insurance_type = input('Enter the insurance type')
# if statement 
if Insurance_type == 'full' or Insurance_type == 'FULL':
    Insurance_type = 50
    print(f'R{Insurance_type}')
  
elif Insurance_type == 'limited' or Insurance_type == 'LIMITED':
    Insurance_type = 25
    print(f'R{Insurance_type}')
else:
    print('Error')
# gift cover type chosen
gift_type = input('Do you want a gift cover or not?\t')
if gift_type == 'gift cover' or gift_type == 'GIFT COVER':
    gift_type = 25
    print(f'R{gift_type}')
  
elif gift_type == 'no' or gift_type == 'NO':
    gift_type = 0
    print(f'R{gift_type}')
  
else:
    print('Error!')

# Priority of delivery
priority_type = input('Enter the the importance of your delivery')
if priority_type == 'standard' or priority_type == 'STANDARD':
  priority_type = 100
  print(priority_type)
# Between standard and limited
elif priority_type == 'limited' or priority_type == 'LIMITED':
    priority_type = 50
    print(priority_type)
else:
    print('Error')
#Total cost 
total_cost = parcel_type + freight_cost + Insurance_type + gift_type
print(f'R{total_cost}')












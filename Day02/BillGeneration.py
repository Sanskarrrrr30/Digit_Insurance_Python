#PROG 06 : Bill Generation

# setting global constants

APPLE_GST = 0.12 #12%
ORANGE_GST = 0.05 #5%

# input buyers name
buyer_name = input("Enter buyer's name: ")

#per kg price of apple and orange
apple_price = float(input("Enter price of apple per kg: "))
orange_price = float(input("Enter price of orange per kg: "))

# quantity of apple and orange in kg
apple_qty = float(input("Enter quantity of apple in kg: "))
orange_qty = float(input("Enter quantity of orange in kg: "))

# calculate total price for apple and orange
apple_total = apple_price * apple_qty
orange_total = orange_price * orange_qty

# calculate gst for apple and orange
apple_gst = apple_total * APPLE_GST
orange_gst = orange_total * ORANGE_GST

#total billing amount 
total_apple = apple_total + apple_gst
total_orange = orange_total + orange_gst

# total amount
total_amount = total_apple + total_orange

total_round_amount = round(total_amount)

# print bill
print(f"Buyer Name:  {buyer_name}")
print('-'*74)
print(f"{'Item':<20}{'Price per kg':<20}{'Quantity (kg)':<20}{'Total Price':<20}")
print('-'*74)  
print(f"{'Apple':<20}{apple_price:<20}{apple_qty:<20}{total_apple:<20.2f}")
print(f"{'Orange':<20}{orange_price:<20}{orange_qty:<20}{total_orange:<20.2f}")
print('-'*74)
print(f"{'Total Amount':<60}{total_round_amount:<20.2f}")



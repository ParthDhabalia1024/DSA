# Question 3 Problem Statement – Mayuri buys “N” no of products from a shop. The shop offers a different percentage of discount 
# on each item. She wants to know the item that has the minimum discount offer, so that she can avoid buying that and save money.
# [Input Format: The first input refers to the no of items; the second input is the item name, price and discount percentage 
#  separated by comma(,)]
# Assume the minimum discount offer is in the form of Integer.
# Note: There can be more than one product with a minimum discount.

# Sample Input 1:
# 4
# mobile,10000,20
# shoe,5000,10
# watch,6000,15
# laptop,35000,5
# Sample Output 1:
# shoe

# Explanation: The discount on the mobile is 2000, the discount on the shoe is 500, the discount on the watch 
# is 900 and the discount on the laptop is 1750. So the discount on the shoe is the minimum.



def find_min_discount_item(items):
    min_discount = float('inf')  # Initialize with a very large number
    min_item = ""
    
    # Loop through each item and calculate the discount
    for item in items:
        item_name = item[0]
        price = int(item[1])
        discount_percentage = int(item[2])
        
        # Calculate the discount
        discount = (price * discount_percentage) // 100
        
        # Check if this discount is the minimum
        if discount < min_discount:
            min_discount = discount
            min_item = item_name
        elif discount == min_discount:  # In case of tie, keep the first one encountered
            continue
    
    return min_item

# Input section
n = int(input())  # Number of items

items = []

# Collecting the item details: name, price, and discount percentage
for _ in range(n):
    item_details = input().split(',')
    items.append(item_details)

# Find and print the item with the minimum discount
result = find_min_discount_item(items)
print(result)

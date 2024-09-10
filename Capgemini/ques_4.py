# Problem Statement –

# A function is there which tells how many dealerships there are and the total number of cars in each dealership.

# Your job is to calculate how many tyres would be there in each dealership.

 

# Input

# 3 

# 4 2

# 4 0

# 1 2

# Output

# 20

# 16

# 8

 

# There are total 3 dealerships

# dealerships1 contains 4 cars and 2 bikes

# dealerships2 contains 4 cars and 0 bikes

# dealerships3 contains 1 cars and 2 bikes

# Total number of tyres in dealerships1  is (4 x 4) + (2 x 2) = 20

# Total number of tyres in dealerships2 is (4 x 4) + (0 x 2) = 16

# Total number of tyres in dealerships3 is (1 x 4) + (2 x 2) = 8



# Function to calculate the total tyres for each dealership
def calculate_tyres(n, dealerships):
    # Loop through each dealership and calculate tyres
    for cars, bikes in dealerships:
        total_tyres = (cars * 4) + (bikes * 2)
        print(total_tyres)






# Input: number of dealerships
n = int(input("Enter the number of dealerships: "))

# Input for cars and bikes in each dealership
dealerships = []
for i in range(n):
    # Split the input to get the number of cars and bikes
    cars, bikes = map(int, input().split())
    dealerships.append((cars, bikes))

# Calculate and print the number of tyres for each dealership
calculate_tyres(n, dealerships)


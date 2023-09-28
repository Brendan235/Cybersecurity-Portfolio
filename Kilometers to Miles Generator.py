# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Input from the user
kilometers = float(input("Enter distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers_to_miles(kilometers)

# Display the result
print(f"{kilometers} kilometers is equal to {miles} miles")

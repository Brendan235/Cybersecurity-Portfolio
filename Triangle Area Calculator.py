# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return (base * height) / 2

# Input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = calculate_triangle_area(base, height)

# Print the result
print(f"The area of the triangle with base {base} and height {height} is {area}")


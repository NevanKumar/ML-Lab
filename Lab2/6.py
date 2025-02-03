print("NEVAN KUMAR")
print("22053791")
def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] 
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1) 
        triangle.append(row)
    return triangle

def display_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))  
    for row in triangle:
        print(" ".join(map(str, row)).center(max_width))

def main():
    try:
        rows = int(input("Enter the number of rows for Pascal's Triangle: "))
        if rows <= 0:
            print("Please enter a positive integer.")
        else:
            triangle = generate_pascals_triangle(rows)
            print("\nPascal's Triangle:")
            display_pascals_triangle(triangle)
    except ValueError:
        print("Invalid input! Please enter an integer.")
main()
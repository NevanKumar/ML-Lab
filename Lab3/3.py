import numpy as np

# Create a sample array
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

print("Original Array:\n", array)

# 1. Access a specific element (Indexing)
element = array[1, 2]  # Row 1, Column 2 (0-based indexing)
print("Element at row 1, column 2:", element)

# 2. Access a full row
row = array[1, :]  # All columns in row 1
print("Row 1:", row)

# 3. Access a full column
column = array[:, 2]  # All rows in column 2
print("Column 2:", column)

# 4. Slice a sub-array
sub_array = array[0:2, 1:3]  # Rows 0 to 1, Columns 1 to 2
print("Sub-array (rows 0-1, columns 1-2):\n", sub_array)

# 5. Reverse the array (row-wise and column-wise)
reverse_rows = array[::-1, :]  # Reverse rows
print("Array with reversed rows:\n", reverse_rows)

reverse_columns = array[:, ::-1]  # Reverse columns
print("Array with reversed columns:\n", reverse_columns)


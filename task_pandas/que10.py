# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+
# Write a solution to correct the errors:

# The grade column is stored as floats, convert it to integers.

# The result format is in the following example.

 

# Example 1:
# Input:
# DataFrame students:
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73.0  |
# | 2          | Kate | 15  | 87.0  |
# +------------+------+-----+-------+
# Output:
# +------------+------+-----+-------+
# | student_id | name | age | grade |
# +------------+------+-----+-------+
# | 1          | Ava  | 6   | 73    |
# | 2          | Kate | 15  | 87    |
# +------------+------+-----+-------+
# Explanation: 
# The data types of the column grade is converted to int.
import pandas as pd
data = {
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.0]
}
students = pd.DataFrame(data)
students['grade'] = students['grade'].astype(int)
print(students.to_string(index=False))
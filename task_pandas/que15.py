# DataFrame animals
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | species     | object |
# | age         | int    |
# | weight      | int    |
# +-------------+--------+
# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

# Return the animals sorted by weight in descending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# DataFrame animals:
# +----------+---------+-----+--------+
# | name     | species | age | weight |
# +----------+---------+-----+--------+
# | Tatiana  | Snake   | 98  | 464    |
# | Khaled   | Giraffe | 50  | 41     |
# | Alex     | Leopard | 6   | 328    |
# | Jonathan | Monkey  | 45  | 463    |
# | Stefan   | Bear    | 100 | 50     |
# | Tommy    | Panda   | 26  | 349    |
# +----------+---------+-----+--------+
# Output: 
# +----------+
# | name     |
# +----------+
# | Tatiana  |
# | Jonathan |
# | Tommy    |
# | Alex     |
# +----------+
# Explanation: 
# All animals weighing more than 100 should be included in the results table.
# Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
# The results should be sorted in descending order of weight.
 

# In Pandas, method chaining enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 

# Can you complete this task in just one line of code using method chaining?
import pandas as pd
animal_data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}
animals = pd.DataFrame(animal_data)
filtered_animals = animals[animals['weight'] > 100]
sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)
result = sorted_animals[['name']].reset_index(drop=True)
print(result)
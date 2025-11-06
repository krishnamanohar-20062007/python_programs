#4.1.(II)
import pandas as pd
# Create a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])
# Convert Series to Python list
data_list = data.tolist()
# Display the list and its type
print("Python list:", data_list)
print("Type:", type(data_list))


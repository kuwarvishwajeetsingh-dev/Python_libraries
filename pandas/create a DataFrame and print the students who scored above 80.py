import pandas as pd
df = pd.DataFrame({
    'Name': ['Amit', 'Riya', 'Karan', 'Sneha'],
    'Marks': [85, 92, 78, 88],
    'City': ['Delhi', 'Noida', 'Delhi', 'Pune']
})
print(df[df['Marks'] > 80])
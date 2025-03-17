import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Category': ['Memory Safety', 'Concurrency Safety', 'Absence of nullptr', 'Performance', 'Bug-free Software', 'Strong Performance', 'Enjoyability', 'H'],
    'Value': [90, 84, 81, 87, 87.1, 84.5, 71.2, -10]
}
df = pd.DataFrame(data)

# Sorting categories by value for better visualization
df = df.sort_values('Value', ascending=True)

# Assigning colors based on positive or negative values
colors = ['red' if x < 0 else 'blue' for x in df['Value']]

# Creating the bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(df['Category'], df['Value'], color=colors)

# Adding a vertical line at x=0 for reference
ax.axvline(0, color='black', linewidth=1.3)

# Adding labels and title
ax.set_xlabel('Value')
ax.set_ylabel('Category')
ax.set_title('Diverging Bar Chart')

# Adding values to the bars
for bar in bars:
    width = bar.get_width()
    # Add the value in the middle of the bars (with a slight offset for better positioning)
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.1f}', 
            va='center', ha='left' if width > 0 else 'right', color='black', fontsize=10)

# Show plot
plt.show()

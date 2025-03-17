import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Daily Usage", "Production Code Proficiency", "Developer Usage", "Professional Usage"]
years = ["2022", "2023", "2024"]
values = [
    [47.3, 49.3, 53.4],
    [42.3, 47.0, 53.5],
    [29.8, 33.9, 38.2],
    [35.4, 38.7, 45.5]    
]

# Define colors for bars
colors = ["#444444", "#777777", "#BBBBBB"]  # Dark grey, medium grey, light grey

# X-axis positions
x = np.arange(len(categories))
width = 0.2  # Bar width

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
plt.style.use("seaborn-v0_8-darkgrid")  # Professional theme

# Plot bars with colors and labels
for i, year in enumerate(years):
    bars = ax.bar(x + i * width, [v[i] for v in values], width, label=year, color=colors[i], edgecolor='black')

    # Add percentage labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f"{height}%", ha='center', fontsize=10, fontweight='bold')

# Labels and formatting
ax.set_xlabel("Categories", fontsize=12, fontweight="bold")
ax.set_ylabel("Percentage (%)", fontsize=12, fontweight="bold")
ax.set_title("Rust Trends between 2022 and 2024", fontsize=14, fontweight="bold")
ax.set_xticks(x + width)
ax.set_xticklabels(categories, fontsize=11)
ax.legend(title="Year", fontsize=11)

# Adjust layout for readability
plt.ylim(0, 100)  # Ensure it goes from 0 to 100%
plt.tight_layout()

# Save as PDF (or PNG)
plt.savefig("grouped_bar_chart.pdf", format="pdf", dpi=300)  # High-res output
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for seasonal revenue patterns
np.random.seed(42)
months = list(range(1, 13)) * 3
segments = ['Enterprise'] * 12 + ['SMB'] * 12 + ['Consumer'] * 12
revenue = []

# Enterprise: High value, steady growth
for i in range(12):
    revenue.append(50000 + i * 1000 + np.random.normal(0, 1000))

# SMB: Medium value, seasonal peak in mid-year
for i in range(12):
    revenue.append(25000 + i * 500 + 5000 * np.sin(i/12 * np.pi) + np.random.normal(0, 800))

# Consumer: Lower value, holiday peak
for i in range(12):
    val = 10000 + i * 200 + np.random.normal(0, 500)
    if i >= 10: # Nov/Dec peak
        val += 3000
    revenue.append(val)

df = pd.DataFrame({
    'Month': months,
    'Revenue': revenue,
    'Segment': segments
})

# Create lineplot
# Figure size 8x8 inches at 64 DPI = 512x512 pixels
plt.figure(figsize=(8, 8))

plot = sns.lineplot(
    data=df, 
    x='Month', 
    y='Revenue', 
    hue='Segment', 
    style='Segment', 
    markers=True, 
    dashes=False,
    palette="deep"
)

# Customize styling
plt.title('Monthly Revenue Trend by Customer Segment', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Segment', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save chart
# Using dpi=64 and figsize=(8,8) ensures exactly 512x512 pixels
# Note: bbox_inches='tight' is omitted to preserve exact dimensions
plt.savefig('chart.png', dpi=64)

print("Chart generated successfully: chart.png")

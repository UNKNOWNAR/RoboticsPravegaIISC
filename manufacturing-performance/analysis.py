import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Email: 24f3001857@ds.study.iitm.ac.in

# 1. Data Setup
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Efficiency_Rate': [70.45, 72.38, 75.40, 77.44]
}
df = pd.DataFrame(data)
benchmark = 90.0

# 2. Analysis
average_efficiency = df['Efficiency_Rate'].mean()
print(f"Average Efficiency Rate: {average_efficiency:.2f}")

# 3. Visualization
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plot Trend
plt.plot(df['Quarter'], df['Efficiency_Rate'], marker='o', linewidth=2, label='Actual Efficiency')

# Plot Benchmark
plt.axhline(y=benchmark, color='r', linestyle='--', label=f'Target ({benchmark})')

plt.title('Manufacturing Equipment Efficiency (2024)', fontsize=14)
plt.xlabel('Quarter')
plt.ylabel('Efficiency Rate (%)')
plt.ylim(60, 100)
plt.legend()

# Add value labels
for x, y in zip(df['Quarter'], df['Efficiency_Rate']):
    plt.text(x, y+1, f'{y}%', ha='center')

plt.tight_layout()
plt.savefig('efficiency_trend.png')
print("Visualization saved as efficiency_trend.png")

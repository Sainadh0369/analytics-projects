
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../data/data.csv')

# Plot data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Value'], label='Data Trend', marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Predictive Sales Analytics')
plt.legend()
plt.tight_layout()
plt.savefig('../output/output_plot.png')

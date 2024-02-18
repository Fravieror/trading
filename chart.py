
import pandas as pd
import matplotlib.pyplot as plt

# Read the log file
log_data = pd.read_csv('logfile.log', header=None, names=['Timestamp', 'Price', 'Value'])

# Convert timestamp to datetime
log_data['Timestamp'] = pd.to_datetime(log_data['Timestamp'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(log_data['Timestamp'], log_data['Value'], marker='o', linestyle='-')
plt.title('Page Views Over Time')
plt.xlabel('Time')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

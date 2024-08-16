import matplotlib . pyplot as plt
import numpy as np

# define events with their dates and associated colors
events = [
    {"name": "Hominins Walk", "date": -7000000, "color": "brown"},
    {"name": "Modern Homo sapiens", "date": -300000, "color": "red"},
    {"name": "Homo Floresiensis", "date": -100000, "color": "black"},
    {"name": "Humans in Americas", "date": -15000, "color": "goldenrod"},
    {"name": "Dog first domesticated", "date": -10000, "color": "green"},
    {"name": "Corn domesticated", "date": -9000, "color": "orange"},
    {"name": "First wheel invented", "date": -4000, "color": "darkblue"},
    {"name": "First pyramid", "date": -2630, "color": "blue"},
    {"name": "China's Great Wall started", "date": -700, "color": "darkgray"},
    {"name": "Roman collapse", "date": 80, "color": "purple"},
    {"name": "Cahokia peak", "date": 1050, "color": "teal"},
]

# sort events by their date
events = sorted(events, key=lambda x: x['date'])

# setting up dates for plotting
dates = [-event['date'] if event['date'] < 0 else event['date'] for event in events]
dates = np.array(dates)
dates[dates == 0] = 1
log_dates = np.log10(dates)

scaling_factor = 1
scaled_log_dates = log_dates * scaling_factor

plt.figure(figsize=(20, 7))
plt.plot(scaled_log_dates, [1] * len(scaled_log_dates),
         color='gray', linestyle='-', linewidth=2)

# position offsets for labels
x_offset = 0.05
y_offset = 0.001

# plot the points and position the labels
for i, event in enumerate(events):
    plt.scatter(scaled_log_dates[i], 1, marker='o', color=event['color'], s=100)
    date_label = f"{event['name']} ({'{} BCE'.format(-event['date']) if event['date'] < 0 else event['name']} ({event['date']} CE)"
    plt.text(scaled_log_dates[i] - x_offset, 1 - y_offset,
             date_label, rotation=45, ha='left', va='bottom',
             fontsize=10, fontfamily='serif', color=event['color'])

plt.yticks([])
plt.xlabel("Years From Present Day (August 15th, 2024)",
           fontsize=12, fontfamily='serif')
plt.title("Timeline on a Logarithmic Timescale", fontsize=14)
plt.xticks(np.log10([1, 10, 100, 1000, 10000, 100000, 1000000,
                     10000000]), ['1', '10', '100', '1,000', '10,000', '100,000', '1,000,000', '10,000,000'],
           fontsize=12, fontfamily='serif')

# The x axis ticks represent major time periods
plt.xlim(scaled_log_dates.min() - 1.5, max(scaled_log_dates) + 1)
plt.tick_params(axis='x', which='minor', length=4, color='gray', top=False)
plt.tick_params(axis='x', which='major', length=7, color='lightgray')
plt.grid(True, which="major", ls="--", color="lightgray")
plt.show()























































import matplotlib.pyplot as plt

# Digit frequency data
digit_data = {
    'Digit': ['6', '7', '1', '3', '2', '4', '5', '9', '8'],
    'Percentage': [6.790123456790123, 5.679012345679013, 31.48148148148148, 12.716049382716049,
                   13.82716049382716, 11.049382716049383, 9.012345679012345, 5.185185185185185,
                   4.2592592592592595],
    'Occurrences': [110, 92, 510, 206, 224, 179, 146, 84, 69]
}

# Extract data for plotting
digits = digit_data['Digit']
percentages = digit_data['Percentage']
occurrences = digit_data['Occurrences']

# Create a bar graph
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(digits, percentages)

# Set labels and title
ax.set_xlabel('Digit')
ax.set_ylabel('Percentage')
ax.set_title('Digit Frequency')

# Display the bar graph
plt.show()

# Save the bar graph as an image file
fig.savefig('results.png')

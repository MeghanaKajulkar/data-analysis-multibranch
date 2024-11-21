import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')

# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

# Process each file in the input directory
for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith('.csv'):
        input_path = os.path.join(INPUT_DIR, file_name)
        output_summary = os.path.join(OUTPUT_DIR, f'{os.path.splitext(file_name)[0]}_summary.txt')
        output_plot = os.path.join(PLOTS_DIR, f'{os.path.splitext(file_name)[0]}_pairplot.png')

        # Load the dataset
        print(f"Processing {file_name}...")
        data = pd.read_csv(input_path)

        # Generate and save a summary
        summary = data.describe(include='all').to_string()
        with open(output_summary, 'w') as f:
            f.write(f"Summary for {file_name}:\n")
            f.write(summary)

        # Generate and save a pairplot
        sns.pairplot(data)
        plt.savefig(output_plot)
        plt.close()
        print(f"Generated summary and pairplot for {file_name}.")

print("Processing complete!")

import argparse
import os
import pandas as pd

def calculate_cross_correlations(directory_i,directory_o):
    directory = directory_i
    # Get a list of all CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Read the CSV files into a dataframe
    main_df = pd.DataFrame([])
    for file in csv_files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        main_df[file.split('.')[0]] = df[df.columns[0]]

    # Create a DataFrame with the cross-correlation results
    df_cross_correlations = main_df.corr()
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_o):
        os.makedirs(directory_o)

    # Save the DataFrame to a CSV file
    output_file = os.path.join(directory_o, 'cross_correlations.csv')
    df_cross_correlations.to_csv(output_file)

    print(f'Successfully calculated cross-correlations and saved them to {output_file}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate cross-correlations between CSV files in a directory.')
    parser.add_argument('--directory_i', '-i', help='Directory containing the CSV files', required=True)
    parser.add_argument('--directory_o', '-o', help='Directory where the CSV file will be saved', default='.')
    args = parser.parse_args()

    calculate_cross_correlations(args.directory_i, args.directory_o)


import argparse
import os
import pandas as pd
import random

def generate_numbers_csv(directory, filename, num_numbers, column_name):
    # Generate a list of random numbers
    numbers = [random.randint(1, 1000) for _ in range(num_numbers)]

    # Create a DataFrame with the numbers
    df = pd.DataFrame({column_name: numbers})

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the file path
    file_path = os.path.join(directory, filename)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    print(f'Successfully saved {num_numbers} numbers to {file_path}.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate random numbers and save them to a CSV file.')
    parser.add_argument('--directory', '-d', help='Directory where the CSV file will be saved', default='.')
    parser.add_argument('--filename', '-f', help='Filename for the CSV file', default='numbers.csv')
    parser.add_argument('--column_name', '-c', help='Name of the column', default='Number')
    parser.add_argument('--num_numbers', '-n', type=int, help='Number of random numbers to generate', default=100)
    args = parser.parse_args()

    generate_numbers_csv(args.directory, args.filename, args.num_numbers, args.column_name)


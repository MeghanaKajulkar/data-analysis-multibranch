import pandas as pd
import os

INPUT_DIR = 'input'

def test_dataset(file_path):
    data = pd.read_csv(file_path)
    assert len(data) > 0, f"The dataset {file_path} is empty!"
    assert data.isnull().sum().sum() == 0, f"The dataset {file_path} contains missing values!"

if __name__ == "__main__":
    print("Running tests...")
    for file_name in os.listdir(INPUT_DIR):
        if file_name.endswith('.csv'):
            file_path = os.path.join(INPUT_DIR, file_name)
            print(f"Testing {file_name}...")
            test_dataset(file_path)
            print(f"{file_name} passed all tests.")
    print("All datasets passed tests!")

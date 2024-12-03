import pandas as pd
import random
import numpy as np

def generate_random_dataset(
    num_entries=1000,
    columns=None,
    value_ranges=None,
    save_to_csv=True,
    filename="random_dataset.csv"
):
    """
    Generate a random dataset for practice purposes.
    """

    # Default columns if none are provided
    if columns is None:
        columns = ["ID", "Feature1", "Feature2", "Feature3", "Feature4"]

    # Default value ranges if none are provided
    if value_ranges is None:
        value_ranges = {
            column: (0, 100) for column in columns if column != "ID"
        }

    # Create the dataset
    data = {}
    for column in columns:
        if column == "ID":
            data[column] = list(range(1, num_entries + 1))  # Sequential IDs
        elif column in value_ranges:
            low, high = value_ranges[column]
            data[column] = [round(random.uniform(low, high), 2) for _ in range(num_entries)]
        else:
            # Default to categorical values if no range is specified
            data[column] = [random.choice(["A", "B", "C", "D"]) for _ in range(num_entries)]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV if required
    if save_to_csv:
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}")

    return df

# Example Usage
if __name__ == "__main__":
    # Customize the dataset parameters
    num_entries = random.randint(1000, 5000)  # Random size between 1000 and 5000
    columns = ["ID", "Age", "Score", "Category", "Salary"]
    value_ranges = {
        "Age": (18, 60),
        "Score": (0, 100),
        "Salary": (30000, 100000)
    }
    dataset = generate_random_dataset(
        num_entries=num_entries,
        columns=columns,
        value_ranges=value_ranges,
        filename="practice_dataset.csv"
    )

    print(dataset.head())

import json

import numpy as np
import pandas as pd


def compute_metrics(data: list) -> dict:
    metrics = {}

    all_ages = []
    all_budgets = []

    for input_str in data:
        json_data = json.loads(input_str)
        all_ages.append(json_data["Age"])
        all_budgets.append(json_data["Budget"])

    # Convert to numpy arrays for easier statistical computations
    ages_array = np.array(all_ages)
    budgets_array = np.array(all_budgets)

    # Compute metrics for ages
    metrics['ages'] = {
        'mean': np.mean(ages_array),
        'std_dev': np.std(ages_array),
        'median': np.median(ages_array),
        'min': np.min(ages_array),
        'max': np.max(ages_array),
        '25th_percentile': np.percentile(ages_array, 25),
        '75th_percentile': np.percentile(ages_array, 75)
    }

    # Compute metrics for budgets
    metrics['budgets'] = {
        'mean': np.mean(budgets_array),
        'std_dev': np.std(budgets_array),
        'median': np.median(budgets_array),
        'min': np.min(budgets_array),
        'max': np.max(budgets_array),
        '25th_percentile': np.percentile(budgets_array, 25),
        '75th_percentile': np.percentile(budgets_array, 75)
    }

    return metrics


if __name__ == "__main__":
    data = ['{"Name": "Jill", "Gender": "F", "Age": 48, "Budget": 5332}', '{"Name": "Jack", "Gender": "M", "Age": 19, "Budget": 3650}', '{"Name": "Jill", "Gender": "F", "Age": 34, "Budget": 5041}', '{"Name": "John", "Gender": "F", "Age": 63, "Budget": 5576}', '{"Name": "Jill", "Gender": "M", "Age": 75, "Budget": 5903}',
            '{"Name": "Jill", "Gender": "F", "Age": 40, "Budget": 5673}', '{"Name": "Jim", "Gender": "F", "Age": 46, "Budget": 4677}', '{"Name": "Jane", "Gender": "F", "Age": 31, "Budget": 3382}', '{"Name": "Jack", "Gender": "F", "Age": 26, "Budget": 4070}', '{"Name": "John", "Gender": "F", "Age": 69, "Budget": 6699}']

    metrics = compute_metrics(data)

    print(metrics)

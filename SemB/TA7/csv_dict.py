import csv


def read_csv_as_dictionary(file_path):
    data = {}

    with open(file_path, 'r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            for key, value in row.items():
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]

    return data


# Example usage
file_path = 'results.csv'  # Replace with the path to your CSV file
data = read_csv_as_dictionary(file_path)
print(data["home_team"])

import csv

input_file = "berkeley_data.txt"
output_file = "berkeley_data.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)

    for line in infile:
        # Remove extra spaces and split
        row = line.strip().split()
        writer.writerow(row)

print(f"✅ Converted successfully: {output_file}")

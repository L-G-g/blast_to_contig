import sys

def parse_blast_results(blast_file, target_species):
    # Open the blast result file for reading
    with open(blast_file, 'r') as file:
        # Initialize a list to store matching first columns
        matching_columns = []

        # Iterate through each line in the file
        for line in file:
            # Split the line into columns
            columns = line.strip().split('\t')
            
            # Check if the last column matches the target species
            if columns[-1] == target_species:
                # If it matches, save the first column
                matching_columns.append(columns[0])
    
    return matching_columns

if __name__ == "__main__":
    # Check if the user provided the blast result file path and the target species
    if len(sys.argv) != 3:
        print("Usage: python script.py <blast_results_file> <target_species>")
        sys.exit(1)
    
    blast_file = sys.argv[1]
    target_species = sys.argv[2]

    # Call the parse function
    matching_columns = parse_blast_results(blast_file, target_species)

    # Save the matching first columns to a file
    with open("matching_nodes", "w") as output_file:
        for col in matching_columns:
            output_file.write(col + "\n")
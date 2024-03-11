import sys
import os

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

def read_matching_nodes(filename):
    with open(filename, 'r') as file:
        nodes = [line.strip() for line in file]
    return nodes

def filter_scaffolds(matching_nodes, scaffold_file, output_file):
    nodes_set = set(matching_nodes)
    keep = False
    with open(scaffold_file, 'r') as input_file, open(output_file, 'w') as output:
        for line in input_file:
            if line.startswith('>'):
                node_name = line.split()[0][1:]
                if node_name in nodes_set:
                    keep = True
                    output.write(line)
                else:
                    keep = False
            elif keep:
                output.write(line)


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
    existing_columns = set()
    with open("matching_nodes", "a") as output_file:
        for col in matching_columns:
            if col not in existing_columns:
                output_file.write(col + "\n")
                existing_columns.add(col)
    
    matching_nodes = read_matching_nodes('matching_nodes')
    filter_scaffolds(matching_nodes, 'scaffolds.fasta', 'scaffolds_final.fasta')
    os.remove('matching_nodes')
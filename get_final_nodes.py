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

matching_nodes = read_matching_nodes('matching_nodes')
filter_scaffolds(matching_nodes, 'scaffolds_sucio.fasta', 'scaffolds_final.fasta')
os.remove('matching_nodes')
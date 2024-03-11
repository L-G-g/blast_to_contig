def read_node_names(file_path):
    """Read node names from a file."""
    nodes = []
    with open(file_path, 'r') as file:
        for line in file:
            node = line.split('\n')[0]
            nodes.append(node)
        return nodes

def filter_contigs(contig_file, node_names, output_file):
    """Filter contigs based on node names."""
    with open(contig_file, 'r') as contig_handle, open(output_file, 'w') as output_handle:
        keep = False
        for line in contig_handle: 
            if line.startswith('>'):
                line_clean= line[1:]

                if line_clean in node_names:
                    print(line_clean)
                    keep = True
                    
                    output_handle.write(line)
                else:
                    keep = False
            elif keep:
                output_handle.write(line)

if __name__ == "__main__":
    node_names = read_node_names("matching_nodes")
    
    filter_contigs("scaffolds_sucio.fasta", node_names, "final_contigs.fasta")
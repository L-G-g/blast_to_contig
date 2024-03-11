# Scaffold Filter

## Overview
This Python script, `get_sta_nodes.py`, filters a scaffold file in FASTA format based on a BLAST result and a specified species name. It retrieves scaffolds containing sequences matching the specified species from the BLAST results.

## Requirements
- Python 3.x

## Usage
```
python get_sta_nodes.py <blast_result_file> "<species_name>"
```

- `<blast_result_file>`: Path to the BLAST result file.
- `"<species_name>"`: Species name in quotes.

The script assumes the existence of a `scaffolds.fasta` file in the working directory to operate.

## Example
Suppose you have a BLAST result file named `blast_AF_proka.txt` and you want to filter scaffolds for the species "Staphylococcus aureus subsp. aureus NCTC 8325". You can use the following command:

```
python get_sta_nodes.py blast_AF_proka.txt "Staphylococcus aureus subsp. aureus NCTC 8325"
```

This will filter the scaffold file based on the specified species and output the filtered version.

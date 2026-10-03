def parse_ncbi_fasta(file_path):
    # 1. Read lines from the NCBI FASTA file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 2. Extract header metadata (starts with '>)
    header = lines[0].strip()

    # 3. Clean and concatenate into one uppercase string the sequence lines until the next sequence header ('>')
    sequence_lines = []
    for line in lines[1:]:
        if line.startswith('>'):
            break  # Stop processing at the start of transcript #2
        sequence_lines.append(line.strip())
    dna_sequence = ''.join(sequence_lines).upper()

    # 4. Perform base counting analysis
    length = len(dna_sequence)
    base_counts = {
        "A": dna_sequence.count('A'),
        "T": dna_sequence.count('T'),
        "G": dna_sequence.count('G'),
        "C": dna_sequence.count('C')
    }

    gc_percent = ((base_counts["G"] + base_counts["C"])/len(dna_sequence)) * 100

    # 5. Output scientific analysis
    print(
f"""
=== NCBI FASTA METADATA ===
{header}

Total Sequence Length: {length} base pairs
Base Counts:-
A: {base_counts["A"]}
T: {base_counts["T"]}
G: {base_counts["G"]}
C: {base_counts["C"]}
Calculated GC Content: {gc_percent:.2f}%
"""
    )

    return {
        "length": length,
        "base_counts": base_counts,
        "gc_percent": gc_percent
    }

if __name__ == "__main__":
    parse_ncbi_fasta("data/real_brca1.fasta")
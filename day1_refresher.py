def analyze_dna(dna_sequence):
    """Calculates nucleotide frequency and GC content from a DNA sequence string."""
    print("Length of DNA sequence:", len(dna_sequence))

    # Dictionaries for counting nucleotides
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for letter in dna_sequence:
        if letter in nucleotide_counts:
            nucleotide_counts[letter] += 1

    print("\nNucleotide Frequency Breakdown:")
    for letter, count in nucleotide_counts.items():
        print(f"Base {letter}: {count}")

    # Simple GC-Content Calculation
    gc_count = nucleotide_counts['G'] + nucleotide_counts['C']
    gc_percentage = (gc_count / len(dna_sequence)) * 100
    print(f"\nGC-Content: {gc_percentage:.2f}%")

def display_target_genes(gene_list):
    """Iterates through and prints target BME gene identifiers."""
    print("\nTarget BME Genes:")
    for gene in gene_list:
        print("- Gene Identifier:", gene)


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    sample_dna = "ATGCGATCGATCGATCGATCGATCGATC"
    bme_genes = ["BRCA1", "TP53", "EGFR", "MYC"]

    # Call the functions
    display_target_genes(bme_genes)
    analyze_dna(sample_dna)
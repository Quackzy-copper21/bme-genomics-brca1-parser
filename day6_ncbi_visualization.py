import matplotlib.pyplot as plt
from day5_fasta_parser import parse_ncbi_fasta

results = parse_ncbi_fasta("data/real_brca1.fasta")

def generate_base_counts_chart(base_counts):
    # Create a clean Bar Chart using Matplotlib
    plt.figure(figsize=(6, 4))
    plt.bar(
        base_counts.keys(), base_counts.values(), 
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        edgecolor='black', alpha=0.8, linewidth=0.8
        )

    # Customize titles and labels for a scientific look
    plt.title("NCBI BRCA1 mRNA Nucleotide Base Breakdown", fontsize=14)
    plt.xlabel("Nucleotide Base", fontsize=10)
    plt.ylabel("Base Count (Frequency)", fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Save the plot as an image file in your folder
    plt.tight_layout() # Tight layout prevents text truncation when saving
    plt.savefig("plots/brca1_base_distribution.png", dpi=300)
    print("Plot saved successfully as 'plots/brca1_base_distribution.png'!")

    # Display the plot window
    plt.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    generate_base_counts_chart(results["base_counts"])
import pandas as pd
import matplotlib.pyplot as plt

def generate_expression_chart(csv_file):
    # 1. Load the biological dataset
    df = pd.read_csv(csv_file)

    # 2. Filter target genes with high expression level (> 50)
    high_exp = df[df['expression_level'] > 50]

    # 3. Create a clean Bar Chart using Matplotlib
    plt.figure(figsize=(8, 5))
    plt.bar(high_exp["gene_name"], high_exp["expression_level"], color='teal')

    # Customize titles and labels for a scientific look
    plt.title("Target BME Genes: High Expression Levels (> 50)", fontsize=14)
    plt.xlabel("Gene Identifier", fontsize=12)
    plt.ylabel("Expression Level (Units)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Save the plot as an image file in your folder
    plt.savefig("high_expression_genes.png", dpi=300)
    print("Plot saved successfully as 'high_expression_genes.png'!")

    # 5. Display the plot window
    plt.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    generate_expression_chart("bme_genes.csv")
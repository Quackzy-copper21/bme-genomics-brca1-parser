import pandas as pd

def process_genomic_dataset(file_path):
    # 1. Load the real genomic CSV file
    df = pd.read_csv(file_path)

    print("=== Raw Genomic Dataset Overview ===")
    print(df[["gene_symbol", "chromosome", "expression_score", "clinical_significance"]])


    # 2. Advanced Filtering: High expression (>70) AND high GC content (>50%)
    target_candidates = df[(df["expression_score"] > 70) & (df["gc_percent"] > 50.0)]

    print("\n=== High-Priority Target BME Candidates ===")
    print(target_candidates[["gene_symbol", "mutation_type", "expression_score", "clinical_significance"]])

    # 3. Export filtered results to a new clean CSV file
    target_candidates.to_csv("filtered_target_genes.csv", index=False)
    print("\nFiltered results automatically saved to 'filtered_target_genes.csv'.")

if __name__ == "__main__":
    process_genomic_dataset("real_genome_data.csv")
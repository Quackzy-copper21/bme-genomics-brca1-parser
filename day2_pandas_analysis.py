import pandas as pd

# 1. Load the biological dataset into a pandas DataFrame
df = pd.read_csv("bme_genes.csv")

def full_ds_overview(df):
    """Prints the full dataset overview."""
    print("--- Full Dataset Overview ---")
    print(df)

# 2. Basic Filtering: Find genes with specific conditions (e.g., high expression levels)
def filter_genes(df, col, col_name, operator, threshold):
    """Filters and returns genes with given condition."""    
    match operator:
        case ">":
            filtered_df = df[df[col] > threshold]
        case "<":
            filtered_df = df[df[col] < threshold]
        case "==":
            filtered_df = df[df[col] == threshold]
        case "!=":
            filtered_df = df[df[col] != threshold]
        case ">=":
            filtered_df = df[df[col] >= threshold]
        case "<=":
            filtered_df = df[df[col] <= threshold]
        case _:
            raise ValueError("Invalid operator. Please use '>', '<', '==', '!=', '>=' or '<='.")

    print(f"\n--- High {col_name} Target Genes ({operator}{threshold}) ---")
    print(filtered_df[["gene_id", col, "associated_disease"]])

# 3. Calculate Summary Statistics (A key skill for BME R&D)
def avg_stat(df, col, col_name):
    """Calculates and prints average of given statistic."""
    mean_value = df[col].mean()
    print(f"\nAverage {col_name}: {mean_value:.2f}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Display the full dataset overview
    full_ds_overview(df)

    # Filter for high-expression genes (expression_level > 50)
    filter_genes(df, "expression_level", "Expression Level", ">", 50)

    # Calculate and display average expression level
    avg_stat(df, "expression_level", "Expression Level")

    # Calculate and display average GC content
    avg_stat(df, "gc_content", "GC Content")
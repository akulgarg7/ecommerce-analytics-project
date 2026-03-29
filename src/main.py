# Import the main functions from the modules you just built!
from extract import extract_all
from transform import build_master_dataset
from load import save_master_data

def run_pipeline():
    print("Starting Olist ETL Pipeline...\n")
    
    # Step 1: Extract
    orders, customers, products, items, payments, sellers, reviews, geo, eng = extract_all()
    print("-" * 30)
    
    # Step 2: Transform
    master_df = build_master_dataset(orders, customers, products, items, payments, sellers, reviews, geo, eng)
    print("-" * 30)
    
    # Step 3: Load
    save_master_data(master_df)
    print("\nPipeline executed successfully!")

# This tells Python to run the pipeline ONLY if we execute this specific file
if __name__ == "__main__":
    run_pipeline()
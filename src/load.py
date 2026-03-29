import pandas as pd
import os

def save_master_data(master_df, file_name="master_dataset.csv"):
    """
    Saves the fully transformed master dataset to the processed data folder.
    """
    print(f"Starting Load Phase: Saving {len(master_df)} rows...")
    
    output_path = os.path.join('..', 'data', 'processed', file_name) 
    
    # 2. Save the dataframe to a CSV
    try:
        master_df.to_csv(output_path, index=False)
        print(f"SUCCESS: Master dataset saved to {output_path}")
    except Exception as e:
        print(f"ERROR: Could not save file. Details: {e}")
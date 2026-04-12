import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import urllib.parse

def load_data_to_mysql():
    print("Connecting to MySQL Database...")
    
    # 1. Load hidden credentials
    load_dotenv()
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    host = os.getenv('MYSQL_HOST')
    db = os.getenv('MYSQL_DATABASE')

    safe_password = urllib.parse.quote_plus(password)
    
    # 2. Create the SQLAlchemy Engine
    engine = create_engine(f"mysql+pymysql://{user}:{safe_password}@{host}/{db}")
    
    # 3. Read the fully processed Master Dataset
    print("Reading master dataset...")
    master_df = pd.read_csv('../data/processed/master_dataset.csv')
    
    # ---STAR SCHEMA SLICING ---
    
    # 4. Extract and Push: dim_costumers
    print("Pushing dim_customers...")
    dim_customers = master_df[[
        'customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 
        'customer_city', 'customer_state', 'customer_lat', 'customer_lng'
    ]].drop_duplicates(subset=['customer_id'])
    
    dim_customers.to_sql('dim_customers', con=engine, if_exists='append', index=False)
    
    # 5. Extract and Push: dim_sellers
    print("Pushing dim_sellers...")
    dim_sellers = master_df[[
        'seller_id', 'seller_zip_code_prefix', 'seller_city', 
        'seller_state', 'seller_lat', 'seller_lng'
    ]].dropna(subset=['seller_id']).drop_duplicates(subset=['seller_id'])
    
    dim_sellers.to_sql('dim_sellers', con=engine, if_exists='append', index=False)
    
    # 6. Extract and Push: dim_products
    print("Pushing dim_products...")
    dim_products = master_df[[
        'product_id', 'product_category_name_english', 'product_weight_g', 
        'product_length_cm', 'product_height_cm', 'product_width_cm'
    ]].dropna(subset=['product_id']).drop_duplicates(subset=['product_id'])
    
    dim_products.to_sql('dim_products', con=engine, if_exists='append', index=False)
    
    # 7. Extract and Push: fact_order_items
    print("Pushing fact_order_items...")
    
    fact_order_items = master_df[[
        'order_id', 'order_item_id', 'customer_id', 'product_id', 'seller_id',
        'price', 'freight_value', 'total_item_cost', 'total_payment_value',
        'review_score', 'delivery_delay_days', 'total_shipping_duration',
        'survey_response_time', 'order_status', 'order_purchase_timestamp',
        'order_delivered_customer_date'
    ]]
    
    fact_order_items = fact_order_items.dropna(subset=['order_id', 'order_item_id'])
    
    fact_order_items = fact_order_items.drop_duplicates(subset=['order_id', 'order_item_id'])
    
    fact_order_items.to_sql('fact_order_items', con=engine, if_exists='append', index=False)
    
    print("Star Schema successfully loaded into MySQL!")

if __name__ == "__main__":
    load_data_to_mysql()
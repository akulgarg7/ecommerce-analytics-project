import pandas as pd
import os

def load_raw(file_name):
    file_path=os.path.join('..', 'data', 'raw', file_name)
    try:
        df=pd.read_csv(file_path)
        print(f"Successfully extracted : {file_name} ({len(df)} rows)")
        return df
    
    except FileNotFoundError:
        print(f"Error! Could not find the file named {file_name}. Check your data folder.")
        return None
    
def extract_all():
    print("Starting Extraction: ")
    
    orders = load_raw('olist_orders_dataset.csv')
    customers = load_raw('olist_customers_dataset.csv')
    products = load_raw('olist_products_dataset.csv')
    items = load_raw('olist_order_items_dataset.csv')
    payments = load_raw('olist_order_payments_dataset.csv')
    sellers = load_raw('olist_sellers_dataset.csv')
    reviews = load_raw('olist_order_reviews_dataset.csv')
    geo = load_raw('olist_geolocation_dataset.csv')
    eng = load_raw('product_category_name_translation.csv')

    return orders, customers, products, items, payments, sellers, reviews, geo, eng
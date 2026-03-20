import pandas as pd

def date_conversions(orders_df):
    """Formats datatypes and cleans the raw orders dataset."""
    print("Cleaning orders: converting datatypes...")
    
    
    date_columns = [
        'order_purchase_timestamp', 
        'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    
    # 2. Loop through the list and safely convert them
    for col in date_columns:
        orders_df[col] = pd.to_datetime(orders_df[col])
        
    return orders_df


def clean_payments(payments_df):
    payments_grouped = payments_df.groupby('order_id').agg(
    total_payment_value=('payment_value', 'sum'),      # Add up all the money they paid
    payment_method_count=('payment_sequential', 'max'), # Find out how many different methods they used
    max_installments=('payment_installments', 'max')   # Find the longest installment plan they chose
).reset_index()
    return payments_grouped
    
def clean_reviews(reviews_df):
    """Handles nulls, fixes datetimes, and deduplicates reviews."""
    print("Cleaning reviews: formatting dates and deduplicating...")
    
    # 1. Fill null text values with 'No Comment' / 'No Title'
    reviews_df['review_comment_title'] = reviews_df['review_comment_title'].fillna('No Title')
    reviews_df['review_comment_message'] = reviews_df['review_comment_message'].fillna('No Comment')
    
    # 2. Convert timestamps before sorting
    reviews_df['review_answer_timestamp'] = pd.to_datetime(reviews_df['review_answer_timestamp'])
    reviews_df['review_creation_date'] = pd.to_datetime(reviews_df['review_creation_date'])
    
    # 3. Sort chronologically and drop duplicate order_ids keeping the 'last'
    reviews_clean = reviews_df.sort_values('review_answer_timestamp')
    reviews_clean = reviews_clean.drop_duplicates(subset=['order_id'], keep='last')
    
    return reviews_clean

def clean_items(items_df):
    """Cleans the order items dataset and formats dates."""
    print("Cleaning items: formatting dates...")
    
   
    items_df['shipping_limit_date'] = pd.to_datetime(items_df['shipping_limit_date'])
    
    return items_df

def clean_geolocation(geo_df):
    """Deduplicates zip code coordinates to prevent Cartesian Explosions."""
    print("Cleaning geolocation: dropping duplicate coordinates...")
    
    geo_clean = geo_df.drop_duplicates(subset=['geolocation_zip_code_prefix']) 
    
    return geo_clean

def add_kpi_columns(master_df):
    """Creates new high-value business metrics for the dashboard."""
    print("Engineering final business features (KPIs)...")
    
    # 1. Financial KPI: Total Item Cost (price + freight)
    master_df['total_item_cost'] = master_df['price'] + master_df['freight_value']
    
    # 2. Logistics KPI: Delivery Delay
    master_df['delivery_delay_days'] = (master_df['order_delivered_customer_date'] - master_df['order_estimated_delivery_date']).dt.days

    #3. Total shipping duration: How many days does the entire process take, end-to-end?
    master_df['total_shipping_duration'] = (master_df['order_delivered_customer_date'] - master_df['order_purchase_timestamp']).dt.days

    #4. Survey Response Time
    master_df['survey_response_time'] = (master_df['review_answer_timestamp'] - master_df['review_creation_date']).dt.days

    return master_df


def build_master_dataset(orders, customers, products, items, payments, sellers, reviews, geo, eng_translations):
    """
    The main transformation engine. 
    Takes raw dataframes, cleans them, and merges them into the final table.
    """
    print("Starting Transformation Phase...")
    
    # 1. Clean the raw tables that have formatting issues
    orders_clean = date_conversions(orders)
    payments_clean = clean_payments(payments)
    reviews_clean = clean_reviews(reviews)
    items_clean = clean_items(items)
    geo_clean = clean_geolocation(geo)
    
    # 2. The Great Merge (Follow your Jupyter Notebook order!)
    master_df = pd.merge(orders_clean, customers, on='customer_id', how='left')
    master_df = pd.merge(master_df, items_clean, on='order_id', how='left')
    master_df = pd.merge(master_df, products, on='product_id', how='left')
    master_df = pd.merge(master_df, eng_translations, on='product_category_name', how='left')
    master_df = pd.merge(master_df, payments_clean, on='order_id', how='left')    
    master_df = pd.merge(master_df, sellers, on='seller_id', how='left')
    master_df = pd.merge(master_df, reviews_clean, on='order_id', how='left')
    
    # 3. The Double Map Merge (Customers then Sellers)
    # Customers
    master_df = pd.merge(
        master_df, 
        geo_clean[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']], 
        left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left'
    )
    master_df = master_df.rename(columns={'geolocation_lat': 'customer_lat', 'geolocation_lng': 'customer_lng'})
    master_df = master_df.drop(columns=['geolocation_zip_code_prefix'])

    # Sellers
    master_df = pd.merge(
        master_df, 
        geo_clean[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']], 
        left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left'
    )
    master_df = master_df.rename(columns={'geolocation_lat': 'seller_lat', 'geolocation_lng': 'seller_lng'})
    master_df = master_df.drop(columns=['geolocation_zip_code_prefix'])

    # 4. KPIs
    master_df = add_kpi_columns(master_df)
    
    print(f"Master dataset built successfully! Total rows: {len(master_df)}")
    return master_df
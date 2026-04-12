USE olist_db;

-- 1. Create Dimension Tables (No Foreign Keys)
CREATE TABLE dim_customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state VARCHAR(10),
    customer_lat DECIMAL(10,8),
    customer_lng DECIMAL(11,8)
);

CREATE TABLE dim_sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state VARCHAR(10),
    seller_lat DECIMAL(10,8),
    seller_lng DECIMAL(11,8)
);

CREATE TABLE dim_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name_english VARCHAR(100),
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- 2. Create the Fact Table (With Foreign Keys connecting to Dimensions)
CREATE TABLE fact_order_items (
    order_id VARCHAR(50),
    order_item_id INT,
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    total_item_cost DECIMAL(10,2),
    total_payment_value DECIMAL(10,2),
    review_score INT,
    delivery_delay_days INT,
    total_shipping_duration INT,
    survey_response_time INT,
    order_status VARCHAR(20),
    order_purchase_timestamp DATETIME,
    order_delivered_customer_date DATETIME,
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (seller_id) REFERENCES dim_sellers(seller_id)
);
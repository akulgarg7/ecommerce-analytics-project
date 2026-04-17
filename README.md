# 🛒 E-Commerce: Supply Chain & Strategy Analytics 
## 📌 Project Overview 
This project is an end-to-end data analytics and business intelligence solution designed for a major Brazilian e-commerce platform. Analyzing over 100,000 orders, this project identifies critical supply chain bottlenecks, measures the financial impact of delivery delays on brand reputation, and provides interactive simulators for executive decision-making. 
### 🎯 The Business Problem 
E-commerce platforms often struggle to balance freight costs with customer satisfaction. The executive team needed visibility into:
1. Which geographic regions are experiencing the highest logistics failures?
2.  How do shipping delays quantitatively impact customer review scores?
3. What is the projected financial return if we improve customer retention or negotiate better freight contracts?

--- 

## 🛠️ The Tech Stack & Architecture 
This project demonstrates a complete data pipeline, from raw data ingestion to executive reporting. 
* **Backend & Data Engineering:** Python, Pandas
     * *Impact:* Engineered an Automated Data Ingestion and Integrity Pipeline. Built CLI logic to validate raw CSV datasets, enforce data types, and quarantine corrupted records before analysis.
* **Database & Querying:** SQL (MySQL)
     * *Impact:* Structured and queried relational tables for exploratory data analysis (EDA).
* **Analytics & Visualization:** Power BI, DAX
    * *Impact:* Developed a 5-page interactive dashboard utilizing complex DAX measures, What-If parameters, and dynamic cross-filtering.

--- 

## 📸 Executive Dashboard Preview 
<img width="1372" height="763" alt="image" src="https://github.com/user-attachments/assets/5ed82dfc-91cd-41c9-b0a5-66e17b4462aa" />


## 🚀 How to Run the Project
1. Clone the repository: `git clone (https://github.com/akulgarg7/ecommerce-analytics-project)`
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Setup the database using the schema in `/sql/schema.sql`
5. Run the ETL pipeline: `python src/extract.py`

## 📊 Business Questions Answered
* Which products generate the highest revenue?
* What is the monthly sales trend?

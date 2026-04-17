# E-Commerce: Supply Chain & Strategy Analytics 
## Project Overview 
This project is an end-to-end data analytics and business intelligence solution designed for a major Brazilian e-commerce platform. Analyzing over 100,000 orders, this project identifies critical supply chain bottlenecks, measures the financial impact of delivery delays on brand reputation, and provides interactive simulators for executive decision-making. 
### The Business Problem 
E-commerce platforms often struggle to balance freight costs with customer satisfaction. The executive team needed visibility into:
1. Which geographic regions are experiencing the highest logistics failures?
2.  How do shipping delays quantitatively impact customer review scores?
3. What is the projected financial return if we improve customer retention or negotiate better freight contracts?

--- 

## The Tech Stack & Architecture 
This project demonstrates a complete data pipeline, from raw data ingestion to executive reporting. 
* **Backend & Data Engineering:** Python, Pandas
     * *Impact:* Engineered an Automated Data Ingestion and Integrity Pipeline. Built CLI logic to validate raw CSV datasets, enforce data types, and quarantine corrupted records before analysis.
* **Database & Querying:** SQL (MySQL)
     * *Impact:* Structured and queried relational tables for exploratory data analysis (EDA).
* **Analytics & Visualization:** Power BI, DAX
    * *Impact:* Developed a 5-page interactive dashboard utilizing complex DAX measures, What-If parameters, and dynamic cross-filtering.

--- 

## Executive Dashboard Preview 
<img width="1372" height="763" alt="image" src="https://github.com/user-attachments/assets/5ed82dfc-91cd-41c9-b0a5-66e17b4462aa" />

## Key Business Insights

### 1. The Geographic Supply Chain Failure
While absolute revenue is dominated by major hubs like São Paulo(SP), looking at the **Delivery Failure Rate (% of Revenue at Risk)** reveals a critical geographic bottleneck. States in the North/Northeast regions are suffering massive logistical failures, with states like **Alagoas (AL) experiencing a nearly 22% late-delivery rate**. 
* *Recommendation:* Renegotiate carrier contracts or establish localized micro-fulfillment centers for the Northern regions to stem revenue bleed.
<img width="877" height="307" alt="image" src="https://github.com/user-attachments/assets/6c8b5311-b196-4c94-83c8-9490e24e868a" />


### 2. The "Cost of Being Late" (Brand Reputation)
The data mathematically proves that shipping logistics are directly tied to brand sentiment. An on-time delivery yields a healthy average review score of **4.2 / 5.0**. However, when an order is delayed, the score plummets to a toxic **2.3 / 5.0**. 
* *Recommendation:* Treat logistics as a customer acquisition cost (CAC). Spending more on expedited freight is cheaper than acquiring a new customer to replace an angry one.
<img width="738" height="359" alt="image" src="https://github.com/user-attachments/assets/0890a628-bdf9-43e8-839e-de69c7fa6fd6" />


### 3. The One-Time Buyer Crisis
A comparison of total unique customers to total orders reveals a near 1:1 ratio, indicating a massive churn rate where over 95% of users purchase once and never return. 
* *Strategic Action:* Built a **Customer Retention Simulator** allowing executives to project revenue lifts based on target retention improvements. A mere 5% increase in retention translates to ~$790K in recovered revenue.
<img width="601" height="407" alt="image" src="https://github.com/user-attachments/assets/6c023a0a-677b-4141-b630-365a144a1bc1" />


### 4. Marketing Ad-Spend Optimization
A heatmap analysis of purchasing timestamps reveals that consumers are highly active on **Tuesdays and Wednesdays**, peaking during the mid-year months of **July and August**. 
* *Strategic Action:* Reallocate top-of-funnel marketing budgets (Instagram/Google Ads) to target these specific temporal windows, aggressively promoting the "Hero Category" (Health & Beauty), which boasts highest revenue ($1.44M) and strong customer satisfaction (4.14 rating).
<img width="758" height="407" alt="image" src="https://github.com/user-attachments/assets/aa5a2e71-9d1c-4420-8485-48d44b1cd104" />


### 5. Payment Preferences & Cash Flow
An analysis of transaction types reveals that **Credit Cards dominate the revenue stream ($12.54M)**, dwarfing alternative methods like Boleto ($2.87M) and Vouchers. 
* *Strategic Action:* With credit cards being the overwhelming preference, the business should optimize checkout flows for installment payments (highly popular in the Brazilian market) to further increase the Average Order Value (AOV).
<img width="405" height="298" alt="image" src="https://github.com/user-attachments/assets/4829275e-3954-4d5c-96ff-9c8f10dc7af3" />


### 6. The Polarization of Customer Sentiment
The Review Score Distribution is highly bimodal—customers either leave a 5-star review (57K) or a 1-star review (11K), with very little middle ground. Furthermore, bulky categories like `office_furniture` hold the lowest average rating (3.49). 
* *Strategic Action:* Heavy, difficult-to-ship items are disproportionately damaging the brand. Olist must either increase the strictness of quality control for large-item sellers or partner with specialized freight carriers for the furniture category.
<img width="1375" height="322" alt="image" src="https://github.com/user-attachments/assets/c92be57a-cbde-4429-b9b2-d651e385a226" />


---

## Interactive Executive Tools (Simulators)
To transition this project from *descriptive* analytics (what happened) to *prescriptive* analytics (what we should do), this dashboard includes an **Executive Control Panel** powered by dynamic DAX What-If parameters.

* **Retention Revenue Simulator:** Allows stakeholders to adjust a slider representing a target increase in customer retention. The DAX engine instantly calculates the projected "recovered revenue" in real-time.
* **Freight Savings Simulator:** Allows supply chain managers to simulate the financial impact of renegotiating carrier contracts. Sliding the target reduction percentage instantly projects the total cash saved on the bottom line.

---

## How to Use This Repository

1. **The Executive Summary (Quick View):**
   * If you are a recruiter or simply want to view the final dashboard without installing any software, download and open the [`Olist_Executive_Summary.pdf`](./Olist_Executive_Summary.pdf). 
2. **The Interactive Dashboard (Deep Dive):**
   * If you have Power BI Desktop installed, download the [`Olist_Analytics_Dashboard.pbix`](./Olist_Analytics_Dashboard.pbix) file. 
   * Open the file to interact with the slicers, view the dynamic DAX measures, and test the ROI Simulators on Page 5.
3. **The Data Engineering Pipeline (Codebase):**
   * Review the Python scripts and SQL files included in this repository to see the automated data ingestion, validation, and integrity enforcement logic that powers the dashboard.

## How to Run the Project
1. Clone the repository: `git clone (https://github.com/akulgarg7/ecommerce-analytics-project)`
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Setup the database using the schema in `/sql/schema.sql`
5. Run the ETL pipeline: `python src/extract.py`


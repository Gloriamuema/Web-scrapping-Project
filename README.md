# Web-scrapping-Project
 Project Overview

# The goal of this project is to:
# Scrape or simulate job listings from Kenyan-based companies (e.g. Safaricom, Equity Bank, KCB, Nation Media Group).
# Store the job data — including title, company, location, and category.
# Train a machine learning classifier to predict job categories (Tech, Finance, or Other).
# Export the data to a CSV file for reporting and visualization.

Technologies Used

# Python 3.x
# Pandas – data cleaning and manipulation
# Requests & BeautifulSoup – web scraping
# Scikit-learn – text classification using machine learning
# CSV – exporting and storing structured data

# Installation & Setup
# Clone the Repository
# Use CMD and VS Code 
git clone https://github.com/Gloriamuema/Web-scrapping-Project.git
cd Web-scrapping-Project

# Create a Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

# Install Dependencies
pip install -r requirements.txt

# How to Run the Project

# Run the main script:

# python jobs_scrap_project.py

This will:
# Generate or scrape 50 Kenyan job listings.
# Classify them into Tech, Finance, or Other.
# Save results into kenya_jobs.csv.
# Print a few sample predictions.

# Sample output in kenya_jobs.csv
job_title,company,location,category
Cybersecurity Analyst,Equity Bank,"Nakuru, Kenya",Tech
HR Assistant,Kenya Airways,"Eldoret, Kenya",Other
Data Analyst,EABL,"Mombasa, Kenya",Tech
Systems Administrator,EABL,"Kisumu, Kenya",Tech
Network Administrator,Twiga Foods,"Nakuru, Kenya",Tech
Business Analyst,Kenya Airways,"Eldoret, Kenya",Other
Network Administrator,Kenya Airways,"Eldoret, Kenya",Tech
Sales Manager,KCB Bank,"Nakuru, Kenya",Other
Software Engineer,Nation Media Group,"Kisumu, Kenya",Tech
Systems Administrator,Safaricom,"Kisumu, Kenya",Tech
Data Analyst,Bamburi Cement,"Eldoret, Kenya",Tech
Software Engineer,Twiga Foods,"Eldoret, Kenya",Tech
IT Support Technician,Nation Media Group,"Thika, Kenya",Other
HR Assistant,MP Shah Hospital,"Eldoret, Kenya",Other
Software Engineer,EABL,"Eldoret, Kenya",Tech
Finance Officer,Safaricom,"Kisumu, Kenya",Finance
Software Engineer,Safaricom,"Mombasa, Kenya",Tech
Network Administrator,KCB Bank,"Nairobi, Kenya",Tech
Systems Administrator,Bamburi Cement,"Eldoret, Kenya",Tech
Data Analyst,Equity Bank,"Eldoret, Kenya",Tech
Business Analyst,Equity Bank,"Thika, Kenya",Other
DevOps Engineer,Nation Media Group,"Mombasa, Kenya",Tech
Software Engineer,Microsoft Kenya,"Mombasa, Kenya",Tech
HR Assistant,KenGen,"Nairobi, Kenya",Other
Software Engineer,KCB Bank,"Nakuru, Kenya",Tech
Marketing Executive,KenGen,"Thika, Kenya",Other
Data Analyst,EABL,"Thika, Kenya",Tech

# Future improvements
This tool will have links to the various jobs  for candidate to apply them.

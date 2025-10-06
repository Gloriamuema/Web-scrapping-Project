# Kenyan Job Listings Generator and Classifier 

# Import necessary libraries
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# List of well-known companies in Kenya
companies = [
    "Safaricom", "Equity Bank", "KCB Bank", "Cooperative Bank", 
    "Kenya Airways", "Nation Media Group", "Bamburi Cement", 
    "KenGen", "EABL", "Twiga Foods", "MP Shah Hospital", "Microsoft Kenya"
]

# Common job titles in the Kenyan market
titles = [
    "Software Engineer", "Data Analyst", "Network Administrator",
    "IT Support Technician", "Finance Officer", "Marketing Executive",
    "HR Assistant", "Systems Administrator", "Sales Manager", 
    "Cybersecurity Analyst", "DevOps Engineer", "Business Analyst"
]

# Major towns and cities in Kenya
locations = [
    "Nairobi, Kenya", "Mombasa, Kenya", "Kisumu, Kenya", 
    "Nakuru, Kenya", "Eldoret, Kenya", "Thika, Kenya"
]

# Create an empty list to store job data
data = []

# Generate 50 sample job listings
for _ in range(50):
    # Randomly choose job details
    title = random.choice(titles)
    company = random.choice(companies)
    location = random.choice(locations)

    # Automatically categorize job type based on keywords
    if any(word in title.lower() for word in ["software", "data", "network", "cybersecurity", "devops", "systems"]):
        category = "Tech"
    elif any(word in title.lower() for word in ["finance", "bank", "account"]):
        category = "Finance"
    else:
        category = "Other"

    # Add each job listing as a dictionary
    data.append({
        "job_title": title,
        "company": company,
        "location": location,
        "category": category
    })


#Convert to DataFrame and save to CSV
df = pd.DataFrame(data)

#Save data to a CSV file 

df.to_csv("kenya_jobs.csv", index=False)
print(" kenya_jobs.csv file has been created successfully!")


# Train a simple ML model
# We use a text vectorizer (TF-IDF) + Naive Bayes classifier
# to train the model on job titles and their categories
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df["job_title"], df["category"])

#Test the model with new job titles

test_jobs = ["Software Developer", "Financial Analyst", "Marketing Officer"]

#Get predictions for the test jobs
predictions = model.predict(test_jobs)
#Display results
print("\n Sample Job Data:")
print(df.head())  # Show first 5 sample jobs

print("\n Job Category Predictions:")
for job, pred in zip(test_jobs, predictions):
    print(f"{job} → {pred}")

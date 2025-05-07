import pandas as pd
import numpy as np
import re

df = pd.read_csv("fake_job_postings.csv")

print(df.head())

# eve

# df.fillna(" ", inplace=True)
df = df.replace(np.nan, '', regex=True)
print(df.isnull().sum())

edited_location = df['location'].str.split(',').str[0]
df['location'] = edited_location.values

df["text"] = df["title"] + " " + df["description"] + " " + df["location"] + " " + df["department"] + " " + df["company_profile"] + " " + df[
    "requirements"] + " " + df["benefits"] + " " + df["employment_type"] + " " + df["required_experience"] + " " + df[
        "required_education"] + " " + df["industry"] + " " + df["function"]

df["text"] = df["text"].str.lower()
df["text"] = df["text"].str.replace(r'[^\w\s]', '', regex=True)

df = df.drop(columns=["title", "description", "location", "department", "company_profile", "requirements", "benefits",
                 "employment_type", "required_experience", "required_education", "industry", "function"])

print(df)


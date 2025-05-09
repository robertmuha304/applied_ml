import pandas as pd
import numpy as np
import re

df = pd.read_csv("fake_job_postings.csv")

print(df.head())


df = df.replace(np.nan, '', regex=True)


edited_location = df['location'].str.split(',').str[0]
df['location'] = edited_location.values

print(df.isnull().sum())

df["text"] = df["title"] + " " + df["description"] + " " + df["location"] + " " + df["department"] + " " + df["company_profile"] + " " + df[
    "requirements"] + " " + df["benefits"] + " " + df["employment_type"] + " " + df["required_experience"] + " " + df[
        "required_education"] + " " + df["industry"] + " " + df["function"]

df["text"] = df["text"].str.lower()
df["text"] = df["text"].str.replace(r'[^\w\s]', '', regex=True)

df = df.drop(columns=["title", "description", "location", "department", "company_profile", "requirements", "benefits",
                 "employment_type", "required_experience", "required_education", "industry", "function"])

split = df["salary_range"].str.split("-", expand=True)
salary_min = pd.to_numeric(split[0], errors="coerce")
salary_max = pd.to_numeric(split[1], errors="coerce")

df["salary_range"] = (salary_min + salary_max) // 2
df["salary_range"] = df["salary_range"].fillna("missing")
print(df[:20])
print(df.info())



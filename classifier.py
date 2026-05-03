def categorize(text):
    text = text.lower()
    if any(x in text for x in ["swiggy","zomato"]):
        return "Food"
    elif "uber" in text:
        return "Travel"
    elif "amazon" in text:
        return "Shopping"
    elif "rent" in text:
        return "Rent"
    elif "salary" in text:
        return "Income"
    return "Other"

def apply_categories(df):
    df['category'] = df['description'].apply(categorize)
    return df

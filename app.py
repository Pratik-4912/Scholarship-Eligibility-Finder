
import pandas as pd
from datetime import datetime

def load_data():
    return pd.read_csv("scholarships.csv")

def get_user_input():
    print("\n--- Enter Student Details ---")
    income = int(input("Family Income (in INR): "))
    category = input("Category (General/OBC/SC/ST): ").strip()
    marks = float(input("Marks Percentage: "))
    state = input("State: ").strip()
    return income, category, marks, state

def check_eligibility(df, income, category, marks, state):
    eligible = df[
        (df["Max Income"] >= income) &
        (df["Min Marks"] <= marks) &
        ((df["Category"] == category) | (df["Category"] == "All")) &
        ((df["State"] == state) | (df["State"] == "All India"))
    ]
    return eligible

def show_results(eligible):
    if eligible.empty:
        print("\nNo scholarships found based on your criteria.")
    else:
        print("\nEligible Scholarships:\n")
        today = datetime.today()
        for index, row in eligible.iterrows():
            last_date = datetime.strptime(row["Last Date"], "%Y-%m-%d")
            days_left = (last_date - today).days
            urgency = "🔴 Urgent" if days_left < 7 else ("🟡 Apply Soon" if days_left < 30 else "🟢 Open")
            
            print(f"Name: {row['Scholarship Name']}")
            print(f"Amount: ₹{row['Amount']}")
            print(f"Last Date: {row['Last Date']} ({urgency})")
            print("-" * 40)

def main():
    df = load_data()
    income, category, marks, state = get_user_input()
    eligible = check_eligibility(df, income, category, marks, state)
    show_results(eligible)

if __name__ == "__main__":
    main()

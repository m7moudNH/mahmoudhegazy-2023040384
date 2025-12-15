import pandas as pd

# Load the Excel file
df = pd.read_excel("names.xlsx")

values = ["السبع", "شنوان", "جنزور", "الدبايب", "بو مشهور", "ام صالح", "كفر الشيخ طعيم", "الشهيد فكري", "طنبشا", "كفر هلال", "كفر هورين", "الروض", "كفر الحمادي", "شنتنا"]

pattern = "|".join(values)

filtered = df[df["address"].str.contains(pattern, case=False, na=False)]


# Filter by specific column value
# filtered = df[df["العنوان"] == "Value"]

filtered.to_excel("filtered_output.xlsx", index=False)
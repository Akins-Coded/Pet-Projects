import pandas as pd
#CODED-SOMETHING
# ==========================
# Load data
# ==========================
bank_df = pd.read_csv("bank.csv")
inv_df = pd.read_csv("invoices.csv")

# ==========================
# Standardize formatting
# ==========================
# Lowercase column names
bank_df.columns = bank_df.columns.str.lower()
inv_df.columns = inv_df.columns.str.lower()

# Ensure date format
bank_df["date"] = pd.to_datetime(bank_df["date"])
inv_df["date"] = pd.to_datetime(inv_df["date"])

# Standardize amount to numeric
bank_df["amount"] = pd.to_numeric(bank_df["amount"])
inv_df["amount"] = pd.to_numeric(inv_df["amount"])

# ==========================
# Reconciliation
# ==========================
# Merge bank and invoice entries by amount + date
matched = pd.merge(
    bank_df,
    inv_df,
    how="inner",
    on=["amount", "date"],
    suffixes=("_bank", "_invoice")
)

# Get unmatched bank entries
unmatched_bank = bank_df[
    ~bank_df.set_index(["amount", "date"]).index.isin(
        inv_df.set_index(["amount", "date"]).index
    )
]

# Get unmatched invoice entries
unmatched_invoices = inv_df[
    ~inv_df.set_index(["amount", "date"]).index.isin(
        bank_df.set_index(["amount", "date"]).index
    )
]

# ==========================
# Export results
# ==========================
matched.to_csv("matched.csv", index=False)
unmatched_bank.to_csv("unmatched_bank.csv", index=False)
unmatched_invoices.to_csv("unmatched_invoices.csv", index=False)

print("✅ Reconciliation completed!")
print(f"✅ Matched: {len(matched)} records")
print(f"⚠️ Unmatched bank entries: {len(unmatched_bank)} records")
print(f"⚠️ Unmatched invoices: {len(unmatched_invoices)} records")

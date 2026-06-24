import pandas as pd

# Load dataset
df = pd.read_csv("loan.csv")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Identify categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns

print("\nCategorical Columns:")
print(list(categorical_cols))

# Encode categorical columns using Pandas only
for col in categorical_cols:

    unique_values = df[col].nunique()

    # Binary categories -> Label Encoding
    if unique_values == 2:
        df[col] = df[col].astype("category").cat.codes

    # Multi-category -> One-Hot Encoding
    else:
        dummies = pd.get_dummies(
            df[col],
            prefix=col,
            dtype=int
        )

        df = pd.concat([df, dummies], axis=1)
        df.drop(col, axis=1, inplace=True)

# Save encoded dataset
df.to_csv("encoded_loan.csv", index=False)

print("\nEncoding completed successfully!")
print("Encoded dataset saved as encoded_loan.csv")

print("\nFinal Shape:", df.shape)

print("\nFirst 5 Rows of Encoded Dataset:")
print(df.head())
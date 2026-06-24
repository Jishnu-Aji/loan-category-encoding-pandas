# Category Encoding using Pandas

## Overview

This project demonstrates how to convert categorical variables into numerical values using only Pandas. The loan dataset is preprocessed using Label Encoding and One-Hot Encoding techniques, making it suitable for machine learning models.

## Dataset

**Dataset Used:** `loan.csv`

The dataset contains loan applicant information, including demographic details, loan attributes, and loan status.

## Objective

- Load the dataset using Pandas
- Identify categorical columns
- Convert categorical values into numerical values
- Use only Pandas for all preprocessing operations
- Save the transformed dataset for further analysis

## Technologies Used

- Python
- Pandas

## Project Structure

```text
loan-category-encoding/
│
├── loan.csv
├── encoded_loan.csv
├── category_encoding.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── terminal_output.png
    └── encoded_dataset.png
```

## Categorical Columns Identified

The following categorical columns were detected and encoded:

- loan_intent
- person_education
- person_gender
- person_home_ownership

## Encoding Techniques Used

### Label Encoding

Binary categorical columns are converted into numeric values using Pandas category codes.

Example:

| Gender | Encoded |
|---------|---------|
| Male | 1 |
| Female | 0 |

### One-Hot Encoding

Columns with multiple categories are converted into separate binary columns.

Example:

| loan_intent |
|-------------|
| EDUCATION |
| PERSONAL |
| MEDICAL |

Becomes:

| loan_intent_EDUCATION | loan_intent_PERSONAL | loan_intent_MEDICAL |
|-----------------------|----------------------|---------------------|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

## Python Script

The preprocessing script:

- Loads the dataset
- Detects categorical columns automatically
- Applies Label Encoding for binary categories
- Applies One-Hot Encoding for multi-category features
- Saves the encoded dataset

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute the Script

```bash
python category_encoding.py
```

## Output

After execution:

```text
Dataset Shape: (45015, 12)

Categorical Columns:
['loan_intent',
 'person_education',
 'person_gender',
 'person_home_ownership']

Encoding completed successfully!

Encoded dataset saved as encoded_loan.csv

Final Shape: (45015, 24)
```

## Generated File

```text
encoded_loan.csv
```

The final dataset contains only numerical values and is ready for machine learning workflows.

## Screenshots

### Terminal Output

![Terminal Output](screenshots/terminal_output.png)

### Encoded Dataset

![Encoded Dataset](screenshots/encoded_dataset.png)

## Learning Outcomes

- Data preprocessing using Pandas
- Identifying categorical variables
- Label Encoding
- One-Hot Encoding
- Preparing datasets for machine learning
- Saving transformed datasets for future use


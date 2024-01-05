# Semantic-based-Indicators-of-compromise-Evaluator: User Guide

## Installation

### Pre-requisites

#### Software

- [Python](https://www.python.org/downloads/) (required)
- [Homomorphic Encryption](https://github.com/OpenMined/TenSEAL)
  ```bash
  pip install tenseal
- [OTXv2] (https://pypi.org/project/OTXv2/)
  OTXv2 is an API client library for accessing the Open Threat Exchange, a collaborative platform that allows cybersecurity professionals to share and access threat intelligence data.
  ```bash
  pip install OTXv2


pip install tensorflow
TensorFlow is an open-source machine learning library developed by the Google Brain team. It is widely used for building and training machine learning models, particularly deep learning models.

pip install tensorflow_hub
ensorFlow Hub is a library and platform for reusable machine learning modules. It allows the sharing and reuse of pre-trained models and model components.

pip install sentence-transformers

- SQLite Library
  ```bash
  sudo apt-get update
  sudo apt-get install sqlite3
  sqlite3 --version
  sqlite3 Secureloan.db #not required

#### Procedure for Installation and Run
- Step 1: Clone the Project
Get the resource file from GitHub by cloning the project:

  ```bash
  git clone https://github.com/mahend72/Secure-Loan-Verififaction-and-Approval-system.git


- Step 2: Generate Keys
Run Key_generation.py to obtain public and private keys for each entity in the system.

- Step 3: Customer Registration
Run Registration.py for customer registration and obtaining a unique identification (UID).

- Step 4: Open Bank Account
Run Account_open.py to open an account in a Bank.

- Step 5: Apply for a Loan
Run Apply_loan.py to apply for a loan.

- Step 6: Sign In
For a new customer, run Signin.py to apply for a loan.
For an existing user, run login.py to apply for a loan.

#### Additional Steps
- Run Display.py to display existing customers in the database.
- Run Remove.py to remove any customer from the database.
- Run Enter_details.py to enter information related to customers relevant for a loan application.
- Run Loan_approval.py to check a customer's eligibility.
- Run Approval_decision.py to verify and make a decision for loan approval.
- Run Loan_details_generation.py to consolidate and generate the loan details.

# Tandematcher Version 1.0
## Installation guide
### Step 1: Install python3
### Step 2: Follow the first two steps of the Google Sheets v4 quickstart document
### Step 3: Download MySQL, create an account, a database, and save it to a file titled 'config.py'.
```
connection_id = {
              'user': enter your username between two single quotes,
              'password': enter your password between two single quotes,
              'host': 'localhost',
              'database': enter the name of your database here
}

```
### Step 4: In MySQL, run create_tables_tdmatcher.sql 
### Step 5: Download the Python/MySQL database connector
### Step 6: Run main.py to start the program 
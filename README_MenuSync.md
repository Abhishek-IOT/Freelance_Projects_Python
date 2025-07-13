# MenuSync Automation – A Real-World Python Project for Extract, Clean & Upload via API

## 📌 Overview

**MenuSync Automation** is a Python-based project that automates the workflow of:
1. Extracting menu/product data from a real-world public API .
2. Cleaning and normalizing the data (truncate, round, fill nulls).
3. Uploading cleaned data to a simulated API endpoint.
4. Logging success and failures to timestamped log files.

This project mimics a real-world Upwork use case and is built using clean, modular Python scripts.

---

## 🚀 Project Workflow

```plaintext
phase1_fetch_menu.py       -->  Fetches product data (JSON) from FakeStore API → saves as menu_data.csv
clean_menu_data.py         -->  Cleans data (truncate description, round price, fill nulls) → saves menu_data_cleaned.csv
phase2_push_menu.py        -->  Reads cleaned CSV and uploads each item to httpbin.org/post (simulated API)
                              --> Logs results in upload_log_YYYY-MM-DD.txt
```

---

## 🧩 Technologies Used

- Python 3.x
- `requests` – for API interaction
- `pandas` – for data cleaning and transformation
- `datetime` – for dynamic log naming
- `cron` or Task Scheduler – for automation (6-hour intervals)

---


## ⏱️ Cron Setup (Linux/macOS)

To run every 6 hours, add this to `crontab -e`:

```
0 */6 * * * /usr/bin/python3 /path/to/phase2_push_menu.py >> /path/to/log.txt 2>&1
```


---

## 🧑‍💻 Created By

**Abhishek Srivastava**  
Snowflake & Python Developer | Data Engineer  
July 2025

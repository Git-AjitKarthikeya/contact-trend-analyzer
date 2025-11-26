<h1 align="center">📊 Contact Trend Analyzer</h1>

<p align="center">
  <strong>A lightweight analytics project demonstrating issue trend analysis, escalation patterns, and automated reporting using Python + SQL.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Analysis-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQL-Queries-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Data%20Visualization-Matplotlib-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Role-Operations%20%26%20Analysis-critical?style=for-the-badge">
</p>

---

## 🔍 Overview

This project demonstrates **how to analyze operational contact data** similar to Seller Support or SPS workflows.  
It includes:

- Issue frequency analysis  
- Escalation rate calculation  
- Region-wise resolution time metrics  
- Automated CSV exports  
- A generated bar chart for visual reporting  
- SQL queries for structured analysis  
- Clean, modular Python code  

This project is designed for **portfolio visibility**, **internal mobility**, and **showcasing analytics capability**.

---

## 🗂 Project Structure

---

## 📸 Visuals (ready to upload into your repo)

### **1️⃣ Issue Frequency Chart**
*(Upload the generated PNG later — placeholder below)*

<img src="https://via.placeholder.com/700x350.png?text=Issue+Frequency+Chart" />

---

### **2️⃣ Project Workflow Diagram**
*(Shows how data flows through the project)*

<img src="https://via.placeholder.com/700x300.png?text=Project+Workflow:+CSV+→+Python+→+Outputs" />

---

### **3️⃣ SQL + Python Hybrid Analysis**
*(Nice-looking banner placeholder)*

<img src="https://via.placeholder.com/700x200.png?text=Python+%2B+SQL+Analytics" />

---

## 🚀 How to Run

### **Install dependencies**

### **Execute analysis**

### **Outputs will be generated in**

---

## 📊 Features

### ✔ Issue Frequency Analysis  
Groups contacts by issue_type and summarizes high-volume categories.

### ✔ Escalation Rate Tracking  
Calculates escalation % for each issue type.

### ✔ Regional Resolution Time  
Computes average handling/resolution duration across NA/EU/FE or any defined region.

### ✔ Automated Reporting  
Outputs CSV and PNG files for sharing or dashboard ingestion.

### ✔ SQL Query Set  
Included for a structured alternative to Python processing.

---

## 🧩 Sample Results (Auto-generated)


---

## 🏗 Tech Stack

| Area | Tools |
|------|-------|
| Programming | Python (pandas, matplotlib) |
| Data Storage | CSV |
| Querying | SQL |
| Visualization | Charts (matplotlib) |
| Automation | Azure DevOps-ready YAML |
| Portfolio | GitHub |

---

## 📘 SQL Queries Included

```sql
SELECT issue_type, COUNT(*) AS issue_count
FROM contacts
GROUP BY issue_type;

SELECT issue_type, AVG(escalated) AS escalation_rate
FROM contacts
GROUP BY issue_type;

SELECT region, AVG(resolution_time_min) AS avg_resolution_time_min
FROM contacts
GROUP BY region;
**

👤 Author

Ajit Karthikeya Balla
Selling Partner Support | Amazon
Operations & Analysis | Python | SQL | DevOps**

⭐ If this project helped or you want to connect, feel free to star the repo!
outputs/issue_counts.png

# Expense and Approval Automation Suite

## 🎯 Scenario Overview

AdventureWorks’ Finance team experiences delays in approvals, missed failures, and inconsistent notifications for expense requests and purchase orders.

## 🧩 Your Task

Design a modular automation system to:
- Manage approval workflows
- Handle errors robustly
- Integrate Teams notifications and external APIs

---

## 🧱 Components to Build

1. **Flow 1 – Expense Submission Processor**
    - **Trigger:** New item in SharePoint Expenses list
    - **Action:** Initiate approval using “Start and wait for an approval”

2. **Flow 2 – Approval Result Handler**
    - **If approved:**  
        - Set Status to Approved  
        - Notify via Teams and email
    - **If rejected:**  
        - Set Status to Rejected  
        - Notify requester

3. **Flow 3 – Error Scope Wrapper**
    - Use Try/Catch/Finally scopes
    - **On failure:**  
        - Email admin  
        - Terminate flow

4. **Flow 4 – API Integration Flow**
    - **Trigger:** Manual or scheduled
    - **Action:** HTTP GET (e.g., OpenWeather or Currency API)
    - **Process:** Parse JSON and send summary via Child Flow

5. **Flow 5 – Approval Summary and Audit Logger**
    - **Schedule:** Daily
    - **Action:** Retrieve Expenses, log Approved/Rejected counts to SharePoint FinanceAudit list

---

## ✅ Deliverables

- **Single Solution:** `FinanceAutomationSuite` with all flows
- **Logging:** Decisions and logs in SharePoint lists

---

## 🔍 Validation Criteria

| Check                      | Description                          |
|----------------------------|--------------------------------------|
| Approvals trigger correctly| Managers receive requests            |
| Error handled gracefully   | Admin alert received on failure      |
| API response parsed        | JSON fields mapped correctly         |
| Audit log                  | Daily approval count recorded        |
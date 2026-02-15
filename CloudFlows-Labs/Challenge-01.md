# HR Onboarding and Operations Automation

## 🎯 Scenario Overview

Contoso’s HR department seeks to automate new-hire onboarding and daily HR operations. Manual onboarding emails, document uploads, and expense summaries currently cause delays.

---

## 🧩 Your Task

**Design an end-to-end automation suite using Power Automate to:**
- Streamline onboarding
- Automate HR notifications

---

## 🧱 Components to Build

### **Flow 1 – Onboarding Notification**
- **Trigger:** New record in SharePoint list `Employee_Onboarding`
- **Action:** Send personalized Outlook email  
    _Subject:_ “Welcome to Contoso @{EmployeeName}!”
- **Dynamic Content:** Name, Role, Start Date

---

### **Flow 2 – Document Transfer Flow**
- **Trigger:** File created in OneDrive `/Training/EmployeeDocs`
- **Actions:**
    1. Create corresponding file in SharePoint “Employee Docs” library
    2. Delete source file after successful transfer

---

### **Flow 3 – Invoice Collector**
- **Trigger:** New email with “Invoice” in subject
- **Actions:**
    1. Save attachments to OneDrive
    2. Notify “Finance Ops” channel in Teams

---

### **Flow 4 – Pending Expense Reminder**
- **Trigger:** Recurrence (daily 8 AM)
- **Actions:**
    - Read Excel table of pending expenses
    - Send department-wise Teams reminders (If/Switch conditions)

---

### **Flow 5 – Approved Expense Summary**
- **Trigger:** Recurrence (daily 5 PM)
- **Actions:**
    - Count “Approved” items (variables/expressions)
    - Email daily summary to Finance Manager

---

### **Flow 6 – Daily Health Check (Day 1 Master Flow)**
- **Trigger:** Scheduled 7 PM
- **Actions:**
    - Use Power Automate Management: List my flows & Get flow actions
    - Compile digest of each key flow’s last run status
    - Post summary in Teams

---

## ✅ Deliverables

- Six running flows named **HR_01** → **HR_06**
- Verified run history for each
- Teams and email notifications visible to participants

---

## 🔍 Validation Criteria

| Check                       | Description                              |
|-----------------------------|------------------------------------------|
| Email sent to new hire      | Correct dynamic fields (name, role)      |
| File moved & deleted        | OneDrive → SharePoint success            |
| Invoice handled             | File saved & Teams alert posted          |
| Reminder accuracy           | Only “Pending” expenses notified         |
| Summary email               | Correct approved count                   |
| Health digest               | Reports all flows’ status                |
# 📘 Complete Step-by-Step Guide: HR Onboarding & Operations Automation

## Prerequisites Setup

Before starting, ensure you have:
- ✅ Power Automate license (included with Microsoft 365)
- ✅ Access to SharePoint Online
- ✅ OneDrive for Business
- ✅ Microsoft Teams
- ✅ Outlook (Microsoft 365)
- ✅ Excel Online

---

## 🎯 Flow 1: Onboarding Notification

### **Objective:** Automatically send welcome emails when new employees are added to SharePoint

### **Step-by-Step Instructions:**

#### **Phase 1: Create SharePoint List**

1. **Navigate to SharePoint:**
   - Go to your SharePoint site
   - Click **+ New** → **List**
   - Name it: `Employee_Onboarding`

2. **Add Columns:**
   - Click **+ Add column** and create:
     - `EmployeeName` (Single line of text)
     - `Role` (Single line of text)
     - `StartDate` (Date)
     - `Email` (Single line of text)

3. **Add Test Data:**
   - Click **+ New** and add a sample employee record

#### **Phase 2: Build the Flow**

4. **Open Power Automate:**
   - Go to https://make.powerautomate.com
   - Click **+ Create** → **Automated cloud flow**

5. **Configure Trigger:**
   - Name your flow: `HR_01_Onboarding_Notification`
   - Search for: **"When an item is created"**
   - Select the SharePoint trigger
   - Click **Create**

6. **Set Trigger Parameters:**
   - **Site Address:** Select your SharePoint site
   - **List Name:** Select `Employee_Onboarding`

7. **Add Email Action:**
   - Click **+ New step**
   - Search for: **"Send an email (V2)"**
   - Select the Outlook action

8. **Configure Email:**
   - **To:** Click in the field → Select dynamic content → `Email`
   - **Subject:** Type: `Welcome to Contoso ` then click dynamic content → `EmployeeName` → add `!`
   - **Body:** Create this template:
   ```
   Dear [EmployeeName],

   Welcome to Contoso! We're excited to have you join our team.

   Here are your onboarding details:
   • Role: [Role]
   • Start Date: [StartDate]

   Your manager will reach out shortly with next steps.

   Best regards,
   Contoso HR Team
   ```
   - Replace bracketed items with dynamic content from the SharePoint trigger

9. **Save and Test:**
   - Click **Save**
   - Click **Test** → **Manually** → **Test**
   - Add a new item to your SharePoint list
   - Check the email inbox

---

## 📂 Flow 2: Document Transfer Flow

### **Objective:** Auto-transfer training documents from OneDrive to SharePoint

### **Step-by-Step Instructions:**

#### **Phase 1: Setup Folders**

1. **Create OneDrive Folder:**
   - Open OneDrive for Business
   - Create folder path: `/Training/EmployeeDocs`

2. **Create SharePoint Library:**
   - Go to your SharePoint site
   - Click **+ New** → **Document library**
   - Name it: `Employee Docs`

#### **Phase 2: Build the Flow**

3. **Create New Flow:**
   - Go to Power Automate
   - Click **+ Create** → **Automated cloud flow**
   - Name: `HR_02_Document_Transfer`

4. **Configure Trigger:**
   - Search: **"When a file is created (properties only)"** - OneDrive
   - Click **Create**
   - **Folder:** Browse and select `/Training/EmployeeDocs`

5. **Get File Content:**
   - Click **+ New step**
   - Search: **"Get file content"** - OneDrive for Business
   - **File:** Select dynamic content → `Identifier`

6. **Create File in SharePoint:**
   - Click **+ New step**
   - Search: **"Create file"** - SharePoint
   - Configure:
     - **Site Address:** Your SharePoint site
     - **Folder Path:** `/Employee Docs`
     - **File Name:** Dynamic content → `Name`
     - **File Content:** Dynamic content → `File content`

7. **Delete Original File:**
   - Click **+ New step**
   - Search: **"Delete file"** - OneDrive for Business
   - **File:** Dynamic content → `Identifier`

8. **Save and Test:**
   - Click **Save**
   - Upload a test file to `/Training/EmployeeDocs` in OneDrive
   - Verify it appears in SharePoint and disappears from OneDrive

---

## 💰 Flow 3: Invoice Collector

### **Objective:** Automatically process invoice emails and notify finance team

### **Step-by-Step Instructions:**

#### **Phase 1: Setup**

1. **Create OneDrive Folder:**
   - Create folder: `/Finance/Invoices`

2. **Create Teams Channel:**
   - Open Microsoft Teams
   - Create or use existing channel: `Finance Ops`

#### **Phase 2: Build the Flow**

3. **Create Flow:**
   - Power Automate → **+ Create** → **Automated cloud flow**
   - Name: `HR_03_Invoice_Collector`

4. **Configure Trigger:**
   - Search: **"When a new email arrives (V3)"** - Outlook
   - Click **Create**
   - Click **Show advanced options**
   - **Subject Filter:** Type `Invoice`
   - **Include Attachments:** Yes
   - **Only with Attachments:** Yes

5. **Add Condition to Check Attachments:**
   - Click **+ New step**
   - Search: **"Condition"**
   - Configure:
     - **Left:** Dynamic content → `Attachments` → Click expression tab, type: `length(triggerOutputs()?['body/attachments'])`
     - **Condition:** is greater than
     - **Right:** `0`

6. **In "If yes" Branch - Apply to Each:**
   - Click **Add an action**
   - Search: **"Apply to each"**
   - **Select output:** Dynamic content → `Attachments`

7. **Save Attachments:**
   - Inside Apply to each, click **Add an action**
   - Search: **"Create file"** - OneDrive for Business
   - Configure:
     - **Folder Path:** `/Finance/Invoices`
     - **File Name:** Dynamic content → `Attachments Name`
     - **File Content:** Dynamic content → `Attachments Content`

8. **Notify Teams (Outside Apply to Each):**
   - After the Apply to each action completes
   - Click **+ New step**
   - Search: **"Post message in a chat or channel"** - Teams
   - Configure:
     - **Post as:** Flow bot
     - **Post in:** Channel
     - **Team:** Select your team
     - **Channel:** Select `Finance Ops`
     - **Message:**
     ```
     📧 New Invoice Received!
     
     From: [From]
     Subject: [Subject]
     Attachments saved to OneDrive/Finance/Invoices
     
     Please review and process.
     ```
     - Use dynamic content for From and Subject

9. **Save and Test:**
   - Send yourself an email with "Invoice" in subject and a PDF attachment
   - Check OneDrive and Teams

---

## ⏰ Flow 4: Pending Expense Reminder

### **Objective:** Daily reminders for pending expense approvals

### **Step-by-Step Instructions:**

#### **Phase 1: Create Excel File**

1. **Create Excel File in OneDrive:**
   - Open Excel Online
   - Create new workbook: `Expense_Tracker.xlsx`
   - Save to OneDrive: `/Finance/` folder

2. **Setup Table:**
   - Create headers: `ExpenseID`, `Department`, `Amount`, `Status`, `SubmittedBy`
   - Select the data range (including headers)
   - Click **Insert** → **Table**
   - Name the table: `ExpenseTable` (Table Design → Table Name)
   - Add sample data:
     ```
     ExpenseID | Department | Amount | Status  | SubmittedBy
     EXP001   | Sales      | 500    | Pending | John Doe
     EXP002   | Marketing  | 750    | Approved| Jane Smith
     EXP003   | IT         | 300    | Pending | Bob Wilson
     ```

#### **Phase 2: Build the Flow**

3. **Create Scheduled Flow:**
   - Power Automate → **+ Create** → **Scheduled cloud flow**
   - Name: `HR_04_Pending_Expense_Reminder`
   - **Starting:** Tomorrow at 8:00 AM
   - **Repeat every:** 1 Day

4. **List Rows from Excel:**
   - Click **+ New step**
   - Search: **"List rows present in a table"** - Excel Online
   - Configure:
     - **Location:** OneDrive for Business
     - **Document Library:** OneDrive
     - **File:** Browse to `/Finance/Expense_Tracker.xlsx`
     - **Table:** Select `ExpenseTable`

5. **Filter Pending Items:**
   - Click **+ New step**
   - Search: **"Filter array"**
   - Configure:
     - **From:** Dynamic content → `value` (from List rows)
     - Click **Edit in advanced mode**
     - Paste: `@equals(item()?['Status'], 'Pending')`

6. **Apply to Each Pending Expense:**
   - Click **+ New step**
   - Search: **"Apply to each"**
   - **Select output:** Body from Filter array

7. **Add Switch for Departments:**
   - Inside Apply to each, click **Add an action**
   - Search: **"Switch"**
   - **On:** Dynamic content → `Department` (click "See more" if needed)

8. **Configure Cases:**
   - **Case 1:**
     - **Equals:** `Sales`
     - **Add an action:** Post message in Teams
     - Select Sales channel
     - Message:
     ```
     ⏰ Expense Reminder
     
     Expense ID: [ExpenseID]
     Amount: $[Amount]
     Submitted by: [SubmittedBy]
     Status: Pending
     
     Please review and approve.
     ```
   
   - Click **Add a case** for Marketing, IT, etc.
   - Repeat for each department

9. **Default Case:**
   - In default section, post to general Finance Ops channel

10. **Save and Test:**
    - Click **Save**
    - Click **Test** → **Manually**
    - Or wait until 8 AM tomorrow

---

## 📊 Flow 5: Approved Expense Summary

### **Objective:** Daily email summary of approved expenses

### **Step-by-Step Instructions:**

#### **Phase 1: Build the Flow**

1. **Create Scheduled Flow:**
   - Power Automate → **+ Create** → **Scheduled cloud flow**
   - Name: `HR_05_Approved_Expense_Summary`
   - **Starting:** Tomorrow at 5:00 PM
   - **Repeat every:** 1 Day

2. **Initialize Variable for Count:**
   - Click **+ New step**
   - Search: **"Initialize variable"**
   - Configure:
     - **Name:** `ApprovedCount`
     - **Type:** Integer
     - **Value:** `0`

3. **Initialize Variable for Total Amount:**
   - Click **+ New step**
   - Search: **"Initialize variable"**
   - Configure:
     - **Name:** `TotalAmount`
     - **Type:** Float
     - **Value:** `0`

4. **List Excel Rows:**
   - Click **+ New step**
   - Search: **"List rows present in a table"** - Excel Online
   - Configure same as Flow 4 (same Excel file)

5. **Filter Approved Items:**
   - Click **+ New step**
   - Search: **"Filter array"**
   - **From:** Dynamic content → `value`
   - Click **Edit in advanced mode**
   - Paste: `@equals(item()?['Status'], 'Approved')`

6. **Apply to Each Approved:**
   - Click **+ New step**
   - Search: **"Apply to each"**
   - **Select output:** Body from Filter array

7. **Increment Count:**
   - Inside Apply to each, click **Add an action**
   - Search: **"Increment variable"**
   - **Name:** Select `ApprovedCount`
   - **Value:** `1`

8. **Add to Total:**
   - Click **Add an action**
   - Search: **"Increment variable"**
   - **Name:** Select `TotalAmount`
   - **Value:** Dynamic content → `Amount`

9. **Send Summary Email:**
   - Outside Apply to each, click **+ New step**
   - Search: **"Send an email (V2)"** - Outlook
   - Configure:
     - **To:** `finance.manager@contoso.com` (or your email for testing)
     - **Subject:** `Daily Approved Expense Summary - ` then add expression: `formatDateTime(utcNow(), 'yyyy-MM-dd')`
     - **Body:**
     ```
     📊 Daily Expense Summary
     
     Date: [Today's Date - use expression]
     
     Total Approved Expenses: [ApprovedCount]
     Total Amount: $[TotalAmount]
     
     Please review the full details in the Expense Tracker.
     
     Best regards,
     Automated Finance System
     ```

10. **Save and Test:**
    - Click **Save**
    - Click **Test** → **Manually**

---

## 🏥 Flow 6: Daily Health Check (Master Flow)

### **Objective:** Monitor all flows and report their status

### **Step-by-Step Instructions:**

#### **Phase 1: Build the Flow**

1. **Create Scheduled Flow:**
   - Power Automate → **+ Create** → **Scheduled cloud flow**
   - Name: `HR_06_Daily_Health_Check`
   - **Starting:** Tomorrow at 7:00 PM
   - **Repeat every:** 1 Day

2. **Get Current Environment:**
   - Click **+ New step**
   - Search: **"List my flows"** - Power Automate Management
   - This action will list all your flows

3. **Initialize Variable for Report:**
   - Click **+ New step** (before List my flows)
   - Search: **"Initialize variable"**
   - Configure:
     - **Name:** `HealthReport`
     - **Type:** String
     - **Value:** `Daily Flow Health Check Report\n\n`

4. **Filter for HR Flows:**
   - Click **+ New step**
   - Search: **"Filter array"**
   - **From:** Dynamic content → `value` (from List my flows)
   - Click **Edit in advanced mode**
   - Expression: `@contains(item()?['properties/displayName'], 'HR_')`

5. **Apply to Each Flow:**
   - Click **+ New step**
   - Search: **"Apply to each"**
   - **Select output:** Body from Filter array

6. **Get Flow Run History:**
   - Inside Apply to each, click **Add an action**
   - Search: **"Get flow"** - Power Automate Management
   - **Flow:** Dynamic content → `name` (the GUID of the flow)

7. **Compose Status:**
   - Click **Add an action**
   - Search: **"Compose"**
   - **Inputs:** Use this expression:
   ```
   Flow Name: @{items('Apply_to_each')?['properties/displayName']}
   Status: @{items('Apply_to_each')?['properties/state']}
   Last Modified: @{items('Apply_to_each')?['properties/lastModifiedTime']}
   
   ---
   
   ```

8. **Append to Variable:**
   - Click **Add an action**
   - Search: **"Append to string variable"**
   - **Name:** Select `HealthReport`
   - **Value:** Dynamic content → Select outputs from Compose

9. **Post to Teams:**
   - Outside Apply to each, click **+ New step**
   - Search: **"Post message in a chat or channel"** - Teams
   - Configure:
     - **Post as:** Flow bot
     - **Post in:** Channel
     - **Team:** Your team
     - **Channel:** Select `Finance Ops` or create `IT Ops`
     - **Message:**
     ```
     🏥 Daily Flow Health Check
     
     [HealthReport variable]
     
     All HR automation flows have been checked.
     ```

10. **Optional: Send Email Backup:**
    - Click **+ New step**
    - Search: **"Send an email (V2)"**
    - Send the health report to IT admin

11. **Save and Test:**
    - Click **Save**
    - Click **Test** → **Manually**

---

## 📋 Testing & Validation Checklist

### **Flow 1 - Onboarding Notification**
- [ ] Add new employee to SharePoint list
- [ ] Verify email received with correct name, role, and date
- [ ] Check dynamic content displays properly

### **Flow 2 - Document Transfer**
- [ ] Upload test file to OneDrive `/Training/EmployeeDocs`
- [ ] Confirm file appears in SharePoint `Employee Docs`
- [ ] Verify original file deleted from OneDrive

### **Flow 3 - Invoice Collector**
- [ ] Send email with "Invoice" in subject + attachment
- [ ] Check OneDrive `/Finance/Invoices` for saved file
- [ ] Verify Teams notification in Finance Ops channel

### **Flow 4 - Pending Expense Reminder**
- [ ] Ensure Excel has "Pending" status items
- [ ] Run flow manually (don't wait for 8 AM)
- [ ] Check Teams channels for department reminders
- [ ] Verify only pending items triggered notifications

### **Flow 5 - Approved Expense Summary**
- [ ] Ensure Excel has "Approved" status items
- [ ] Run flow manually
- [ ] Check email for correct count and total
- [ ] Verify calculation accuracy

### **Flow 6 - Daily Health Check**
- [ ] Run flow manually
- [ ] Verify all HR_ flows listed in Teams message
- [ ] Check each flow status is reported
- [ ] Confirm timestamp is accurate

---

## 🎓 Pro Tips & Best Practices

### **Error Handling:**
1. Add **Scope** actions to group steps
2. Add **Configure run after** for error branches
3. Use **Terminate** action for critical failures

### **Performance:**
1. Use **Delay** between API calls to avoid throttling
2. Set **Pagination** on list operations
3. Use **Filter Query** in SharePoint triggers

### **Naming Conventions:**
- Flows: `HR_01_Description`
- Variables: `camelCase` (e.g., `approvedCount`)
- Actions: Descriptive names (rename default action names)

### **Documentation:**
- Add **Notes** in flow designer
- Use **Comments** for complex expressions
- Keep a changelog for flow modifications

### **Security:**
- Use **Service Accounts** for production
- Implement **Approvals** for sensitive operations
- Set appropriate **DLP policies**

---

## 🆘 Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| Dynamic content not showing | Save trigger first, then refresh |
| Excel table not found | Ensure table is formatted as Table, not range |
| Flow fails silently | Check action's **Configure run after** settings |
| Teams connector fails | Re-authenticate Teams connection |
| OneDrive trigger doesn't fire | Check folder path permissions and spelling |
| Email not sending | Verify email address format and Outlook connection |

---

## 📚 Additional Resources

- **Microsoft Learn:** https://learn.microsoft.com/power-automate
- **Power Automate Community:** https://powerusers.microsoft.com
- **Expression Reference:** https://learn.microsoft.com/power-automate/use-expressions-in-conditions
- **Connector Reference:** https://learn.microsoft.com/connectors/

---

## 🎉 Congratulations!

You've now built a complete HR automation suite with 6 interconnected flows. These flows demonstrate:
- ✅ Event-driven automation
- ✅ Scheduled automation
- ✅ Data manipulation
- ✅ Cross-platform integration
- ✅ Monitoring and reporting

**Next Steps:**
1. Monitor flows for 1 week
2. Gather user feedback
3. Optimize based on usage patterns
4. Explore advanced features (approvals, AI Builder)

---

**Need Help?** Feel free to ask questions about any specific flow or concept! 🚀
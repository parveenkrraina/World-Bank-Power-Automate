# Lab 2: Creating Your First Flow — Auto-save Invoice Attachments

## Scenario
Automatically save invoice attachments from email into OneDrive and notify a Teams channel.

**Flow Type:** Automated cloud flow

---

## Steps

### 1. Create the Flow
- Go to **Power Automate**.
- Select **Create** → **Automated cloud flow**.
- **Name:** `M2_Save_Invoice_Attachments`.

### 2. Add Trigger: Outlook – When a new email arrives (V3)
- **Folder:** Inbox
- **Include Attachments:** Yes
- **Additional filter (optional):** Subject filter = `Invoice`

### 3. Add Condition
- **Condition:** Subject contains `Invoice`

### 4. Apply to Each Attachment
- **Action:** OneDrive – Create file
    - **Folder:** `/Training/Invoices_Inbox`
    - **File Name:** `@{concat(triggerOutputs()?['body/subject'],'_',items('Apply_to_each')?['name'])}`
    - **File Content:** Attachment content

### 5. Notify Teams
- **Action:** Teams – Post a message in a chat or channel
    - **Team & Channel:** Automation Training / ops-alerts
    - **Message:** `Saved invoice(s) from "@{triggerOutputs()?['body/from']}" to OneDrive.`

### 6. Save and Test
- Save the flow.
- Test by sending an email with "Invoice" in the subject and a PDF attachment.

---

## Success Criteria
- The file appears in OneDrive under `/Training/Invoices_Inbox`.
- A Teams message posts to the `ops-alerts` channel.

---

**Tip:** You can further customize filters and notifications as needed.
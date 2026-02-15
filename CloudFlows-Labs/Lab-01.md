
## Lab 1: Automated Welcome Email Flow

**Scenario:** Send a personalized welcome email when a new hire is added to the Employee_Onboarding SharePoint list.

### Steps

1. **Create an Automated Cloud Flow**
    - Navigate to [Power Automate](https://make.powerautomate.com).
    - Select **Create** > **Automated cloud flow**.
    - Name the flow: `M1_NewHire_Welcome`.
    - Choose the trigger: **When an item is created** (SharePoint).
    - Configure the trigger:
        - **Site Address:** Your SharePoint site
        - **List Name:** `Employee_Onboarding`

2. **Add an Action: Send Email**
    - Add the **Send an email (V2)** action (Outlook).
    - **To:** Enter a test mailbox or use the dynamic value for "Created By Email".
    - **Subject:**  
      ```
      Welcome to Contoso, @{triggerOutputs()?['body/EmployeeName']}
      ```
    - **Body:**  
      Include dynamic content for EmployeeName, Role, and StartDate.

3. **Save and Test**
    - Save the flow.
    - Add a test item to the `Employee_Onboarding` list.
    - Confirm the flow runs and an email is received with the correct details.

### Success Criteria

- A welcome email is sent with the new hire’s name, role, and start date.

### Troubleshooting

- Verify SharePoint connections and that list/column names match exactly.
- Check permissions for Power Automate and Outlook connections.
- Review run history for error details if the flow fails.
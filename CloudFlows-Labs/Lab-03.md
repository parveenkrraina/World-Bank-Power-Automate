# Lab 03: Move Files from OneDrive to SharePoint Using Power Automate

## Scenario
Automate the process of moving files from a OneDrive folder to a SharePoint document library, then remove the original file from OneDrive.

---

## Flow Type
**Automated cloud flow**

---

## Solution Steps

### 1. Create the Flow
- Go to Power Automate and create a new **Automated cloud flow**.
- **Name:** `M3_OD_To_SP_Mover`

### 2. Add Trigger
- **Trigger:** OneDrive for Business – *When a file is created (Properties only)*
    - **Folder:** `/Training/EmployeeDocs`

### 3. Get File Content
- **Action:** OneDrive for Business – *Get file content*
    - **File Identifier:** Use the Identifier from the trigger.

### 4. Create File in SharePoint
- **Action:** SharePoint – *Create file*
    - **Site Address:** training site
    - **Library Name:** Documents
    - **Folder Path:** EmployeeDocs
    - **File Name:**  
        ```
        @{triggerOutputs()?['body/{FilenameWithExtension}']}
        ```
    - **File Content:** Use the output from *Get file content*.

### 5. Delete File from OneDrive (Optional)
- **Action:** OneDrive for Business – *Delete file*
    - **File Identifier:** Use the Identifier from the trigger.

---

## Testing

1. Save the flow.
2. Drop a file into `/Training/EmployeeDocs` in OneDrive.
3. Confirm the file appears in the SharePoint `EmployeeDocs` folder and is removed from OneDrive.

---

## Success Criteria

- The file is present in SharePoint and no longer exists in the OneDrive source folder.

---
lab:
    Title: 'Lab 1: Create cloud flows'
    Module: 'Module 1: Get started with Power Automate'
---

# Practice Lab 1 – Create cloud flows

In this lab you will create cloud flows.

## What you will learn

- How to create Power Automate cloud flows from a template and with Copilot
- How to create a Power Automate cloud flow from blank and add actions

## High-level lab steps

- Create a cloud flow from a template
- Create a cloud flow with Copilot
- Create a cloud flow
- Monitor cloud flow activity

## Prerequisites

- Must have completed **Lab 0: Validate lab environment**

## Detailed steps

## Exercise 1 – Create a cloud flow from a template

### Task 1.1 - Select a template

1. Navigate to the Power Automate portal `https://make.powerautomate.com`
1. If the **Welcome to Power Automate** pop-up dialog is displayed, select **Get started**.
1. Select the **Dev One** environment.

   ![Environment selector in Power Automate.](../media/select-dev-one-environment-power-automate.png)

1. Select the **Templates** tab from the left-side menu.
1. Select the **Button** tab.
1. Enter `location` in the **Search templates** field.

   ![Screenshot of flow templates.](../media/flow-templates.png)

1. Select **Get today's weather forecast for my current location**.

   ![Screenshot of create connections.](../media/create-connections.png)

1. Select **Create** for **MSN Weather**.
1. Select **Create** for **Notifications**.
1. Select **Create Flow**.
1. If the **Your flow is ready to go** pop-up dialog is displayed, select **Don't show me this again** and select **Got it**.

   ![Screenshot of flow details.](../media/flow-details.png)

### Task 1.2 - Run the flow

1. Select **Run**.
1. If prompted, select **Allow** for **Know your location**

   ![Screenshot of location popup.](../media/allow-location.png)

1. Select **Continue**.
1. Select **Run flow**.
1. Select **Done**.
1. Wait for the flow to complete.

   ![Screenshot of flow run history.](../media/flow-run-history.png)

### Task 1.3 - Review the flow

1. Select the date and time in the flow run history.
1. Expand the **Condition**.
1. Expand the **False** path.

   ![Screenshot of flow run detail.](../media/flow-run-collapsed.png)

1. Select the **Get forecast for today** step with the green tick.

   ![Screenshot of flow run step output.](../media/flow-run-step.png)

1. Select **Edit** and expand the flow steps.
1. Select one of the **Send a push notification** steps.
1. Select **Flow checker**. There should be no errors or warnings.
1. Close the **Flow checker** pane.

### Task 1.4 - Test the flow

1. Select **Test**, select **Automatically**, select **With a recently used trigger**, and then select the flow run.

   ![Screenshot of test flow with recently used trigger.](../media/test-flow.png)

1. Select **Test**.
1. Select the **<-** Back button from the top left-+-+-+-+-+
---
lab:
    Title: 'Lab 1: Create cloud flows'
    Module: 'Module 1: Get started with Power Automate'
---

# Practice Lab 1 – Create cloud flows

In this lab you will create cloud flows.

## What you will learn

- How to create Power Automate cloud flows from a template and with Copilot
- How to create a Power Automate cloud flow from blank and add actions

## High-level lab steps

- Create a cloud flow from a template
- Create a cloud flow with Copilot
- Create a cloud flow
- Monitor cloud flow activity

## Prerequisites

- Must have completed **Lab 0: Validate lab environment**

## Detailed steps

## Exercise 1 – Create a cloud flow from a template

### Task 1.1 - Select a template

1. Navigate to the Power Automate portal `https://make.powerautomate.com`
2. If the **Welcome to Power Automate** pop-up dialog appears, select **Get started**.
3. Select the **Dev One** environment.

   ![Environment selector in Power Automate.](../media/select-dev-one-environment-power-automate.png)

4. Select the **Templates** tab from the left menu.
5. Select the **Button** tab.
6. Enter `location` in the **Search templates** field.

   ![Screenshot of flow templates.](../media/flow-templates.png)

7. Select **Get today's weather forecast for my current location**.

   ![Screenshot of create connections.](../media/create-connections.png)

8. Select **Create** for **MSN Weather**.
9. Select **Create** for **Notifications**.
10. Select **Create Flow**.
11. If the **Your flow is ready to go** dialog appears, select **Don't show me this again** and **Got it**.

    ![Screenshot of flow details.](../media/flow-details.png)

### Task 1.2 - Run the flow

1. Select **Run**.
2. If prompted, select **Allow** for location access.

   ![Screenshot of location popup.](../media/allow-location.png)

3. Select **Continue**.
4. Select **Run flow**.
5. Select **Done**.
6. Wait for completion.

   ![Screenshot of flow run history.](../media/flow-run-history.png)

### Task 1.3 - Review the flow

1. Select the date and time in the run history.
2. Expand the **Condition**.
3. Expand the **False** path.

   ![Screenshot of flow run detail.](../media/flow-run-collapsed.png)

4. Select the **Get forecast for today** step.

   ![Screenshot of flow run step output.](../media/flow-run-step.png)

5. Select **Edit** and expand steps.
6. Select one of the notification steps.
7. Select **Flow checker** to validate.
8. Close the **Flow checker** pane.

### Task 1.4 - Test the flow

1. Select **Test**, then **Automatically**, then **With a recently used trigger**.

   ![Screenshot of test flow with recently used trigger.](../media/test-flow.png)

2. Select **Test**.
3. Select the back button.


# Module 9 — HTTP, APIs, External Integration

## Scenario
Fetch JSON from a public API and post a digest to Microsoft Teams.

---

## Flow Overview

**Name:** `M9_HTTP_Weather_Summary`  
**Type:** Scheduled or Instant (Manual trigger)

---

## Steps

1. **Trigger the Flow**
    - Choose a trigger:
        - **Manual (button) trigger:** Allows users to start the flow on demand.
        - **Recurrence trigger:** Runs the flow on a schedule (e.g., every hour or day).
    - Configure the trigger as needed for your use case.

2. **Add a Scope Action Named `Try`**
    - Insert a **Scope** action and name it `Try`.
    - All main actions will be placed inside this scope.

    a. **HTTP (GET) Action**
        - Inside the `Try` scope, add an **HTTP** action.
        - Set the method to `GET`.
        - Set the URI to:  
          `https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&hourly=temperature_2m`
        - Save and test the action to ensure it returns data.

    b. **Parse JSON Action**
        - Add a **Parse JSON** action after the HTTP action.
        - In the **Content** field, select the `Body` output from the HTTP action.
        - Click **Use sample payload to generate schema**.
        - Paste a sample successful response from the API to generate the schema automatically.

    c. **Compose Summary Message**
        - Add a **Compose** action.
        - Build a summary message using dynamic content from the parsed JSON.
        - Example:  
          ```
          The current temperature is concat(string(first(body('Parse_JSON')?['hourly']?['temperature_2m'])), '°C').
          ```
        - Include at least two fields, such as current temperature and a brief forecast summary.

    d. **Post Message to Teams**
        - Add a **Microsoft Teams – Post a message** action.
        - Set the **Team** and **Channel** to `ops-alerts`.
        - In the **Message** field, use the output from the Compose action.

3. **Add a Scope Action Named `Catch`**
    - Add another **Scope** action and name it `Catch`.
    - Configure this scope to run **only if the `Try` scope fails** (set the run after condition to "has failed").
    - Inside the `Catch` scope:
        - **Compose Error Message:** Add a **Compose** action to create an error message. Use the `outputs('Compose')?['body']` or error details from the failed action.
        - **Post Error to Teams:** Add a **Microsoft Teams – Post a message** action to send the error message to the `ops-alerts` channel.

4. **Add a Scope Action Named `Finally`**
    - Add a third **Scope** action and name it `Finally`.
    - Configure this scope to run **always after** the `Try` and `Catch` scopes (set the run after condition to "is successful, has failed, has timed out, or is skipped").
    - Use this scope for any optional cleanup actions or logging as needed.

---

## Success Criteria

- Teams channel `ops-alerts` receives a structured summary message with weather data from the HTTP API.
- If an error occurs, the channel receives an error notification.

---

> **Tip:** Use clear variable names and comments for maintainability.
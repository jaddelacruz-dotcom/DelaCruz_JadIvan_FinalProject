# Asset Maintenance Tracker (CLI)

**Submitted by:** Jad Ivan Dela Cruz         
**Course:** Intermediate Programming      
**Video Demonstration:** (https://www.youtube.com/watch?v=DN4AhdaC3ug)

## Project Description
The **Asset Maintenance Tracker** is a Python-based Command Line Interface (CLI) application designed to help users log, manage, and track maintenance activities for various equipment or assets. This project solves the real-world problem of disorganized service records by providing a structured, persistent storage system.

*   **Persistent Storage:** Uses JSON file handling to ensure data is saved even after the program closes.
*   **Search Functionality:** Quickly filter through logs using asset names via an optimized search algorithm.
*   **Input Validation:** Handles menu selections and data entry to prevent program crashes.
*   **Object-Oriented Design:** Uses classes to represent tasks and managers for clean, modular code.

1.  **List Comprehensions:** Used for efficient data filtering in the search feature.
2.  **Context Managers:** Utilized `with open()` for safe and leak-proof file handling.
3.  **Data Serialization:** Converting complex Python objects into JSON format for storage.

## Navigate to the directory
cd [Maintenance Tracker]

## Run the application
python src/main.py

---

## Sample Usage
### Adding a New Task
When you run the app, select option **1**. Enter the asset name (e.g., "Laptop"), the service (e.g., "Battery Replacement"), and the date.

### Viewing Logs
Select option **2** to display a numbered list of all maintenance entries currently stored in `data/maintenance_log.json`.

> **Note to Instructor:** Screenshots of the CLI in action are located in the `/screenshots` folder (or attached below).

--- 

##  Installation & Setup
**Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[YourUsername]/[YourRepoName].git

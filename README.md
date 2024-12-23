# 🛡️ URLScanner-VT-ETL-SQLite
This repository is designed for data management and URL scanning using the VirusTotal API. <br>
It integrates SQLite database operations with URL analysis to filter potentially malicious links.

## 📑 Table of Contents
- [✨ Features](#features)
- [⚙️ Installation](#installation)
- [▶️ Usage](#usage)
- [📂 Project Structure](#project-structure)
- [📜 License](#license)

## ✨ Features
- **SQLite Database Management**:
  - 🗂️ Insert data in bulk.
  - 🔍 Execute dynamic SQL queries.
  
- **VirusTotal Integration**:
  - 🛡️ Scan URLs for malicious or suspicious activity.
  - 📊 Retrieve URL reports using VirusTotal API.
  
- **ETL Pipeline**:
  - 📤 Extract data from the SQLite database.
  - ✅ Validate URLs using VirusTotal.
  - 📥 Load filtered results back into the database.

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/virus-total-sql-etl.git
   cd virus-total-sql-etl
   ```
   
2. Install the required Python libraries:
```bash
   pip install -r requirements.txt
```

3. Prepare the following:<br>

  🔑 A VirusTotal API key (Sign up at [VirusTotal](https://www.virustotal.com)).<br>
  🗂️ A SQLite database file with the required schema.



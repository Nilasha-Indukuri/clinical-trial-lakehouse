<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Clinical Trial Data Lakehouse with Blockchain Consent Tracking</title>
</head>
<body style="font-family:sans-serif; line-height:1.6; max-width:800px; margin:auto;">

  <h1>🧪 Clinical Trial Data Lakehouse with Blockchain Consent Tracking</h1>

  <p>This project aims to demonstrate how modern data lakehouse architecture can be combined with blockchain technology to enhance data integrity, consent tracking, and transparency in clinical trials. It is designed to be completed in 1 week with a simplified, end-to-end implementation.</p>

  <h2>🚀 Project Objectives</h2>
  <ul>
    <li>Simulate a data lakehouse to manage clinical trial data.</li>
    <li>Track patient consent using blockchain (Ethereum + Web3.py).</li>
    <li>Build simple ETL pipelines and analytics using Pandas.</li>
    <li>Deploy a Streamlit dashboard to visualize trial progress and consent status.</li>
  </ul>

  <h2>🧱 Architecture Overview</h2>
  <pre>
[Clinical Data CSVs]
       ↓
[Bronze] → [Silver] → [Gold]
       ↓
[Blockchain (Ganache)] ↔ [Web3.py]
       ↓
[Streamlit Dashboard]
  </pre>

  <ul>
    <li><strong>Bronze:</strong> Raw trial data</li>
    <li><strong>Silver:</strong> Cleaned/preprocessed data</li>
    <li><strong>Gold:</strong> Aggregated analytics</li>
    <li><strong>Blockchain:</strong> Records patient consent with timestamps</li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <table border="1" cellpadding="8">
    <tr><th>Layer</th><th>Tools</th></tr>
    <tr><td>Programming</td><td>Python, Pandas, Streamlit</td></tr>
    <tr><td>Blockchain</td><td>Ganache (local Ethereum), Solidity, Web3.py</td></tr>
    <tr><td>Data Storage</td><td>Local folders (Lakehouse style)</td></tr>
    <tr><td>Visualization</td><td>Streamlit</td></tr>
    <tr><td>Version Control</td><td>Git, GitHub</td></tr>
  </table>

  <h2>📁 Project Structure</h2>
  <pre>
clinical-trial-lakehouse/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── contracts/
│   └── Consent.sol
├── notebooks/
│   └── etl.ipynb
├── app.py             # Streamlit Dashboard
├── blockchain.py      # Web3 + Consent functions
├── README.md
├── requirements.txt
└── .gitignore
  </pre>

  <h2>⚙️ Setup Instructions</h2>
  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/YOUR_USERNAME/clinical-trial-lakehouse.git
cd clinical-trial-lakehouse</code></pre>

  <h3>2. Create and Activate Virtual Environment</h3>
  <pre><code>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt</code></pre>

  <h3>3. Install & Launch Ganache</h3>
  <p>Download Ganache from: <a href="https://trufflesuite.com/ganache" target="_blank">https://trufflesuite.com/ganache</a></p>
  <p>Start a workspace and note the RPC URL (usually http://127.0.0.1:8545)</p>

  <h2>📊 Upcoming Features</h2>
  <ul>
    <li>Patient-level consent logging via smart contracts</li>
    <li>Real-time dashboard showing consent and trial stats</li>
    <li>Blockchain-backed audit log of trial data snapshots</li>
  </ul>

  <h2>📄 License</h2>
  <p>This project is for educational and demonstration purposes only.</p>

</body>
</html>

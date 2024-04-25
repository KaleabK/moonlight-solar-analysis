# MoonLight Energy: Solar Investment Strategy Analysis

This repository houses the data analysis and strategy recommendations for MoonLight Energy Solutions' solar investment project. The goal is to leverage data-driven insights to identify high-potential regions for solar panel installation, ultimately enhancing operational efficiency and achieving long-term sustainability goals.

## Project Structure

```plaintext
├── .vscode/
├── .github/
├── .gitignore
├── requirements.txt
├── README.md
├── app
│   └── __init__.py 
│   └── main.py
│   └── util.py
├── data/ (stores solar radiation measurement data)
│   └── <benin-malanville.csv>
│   └── <sierraleone-bumbuna.csv>
│   └── <togo-dapaong_qc.csv>
├── src/ 
├── notebooks/ 
│   └── __init__.py 
│   └── Bennin_Malanville_EDA.ipynb
│   └── Bierraleone_Bumbuna_EDA.ipynb
│   └── Togo-Dapaong_qc_EDA.ipynb
│   └── README.md 
├── tests/ (for unit tests, explained later)
│   └── __init__.py 
│   └── test_scripts.py
└── scripts/
    └── __init__.py 
    └── data_analysis_utils.py
    └── README.md 
    
```

## Project Goals

- Analyze environmental measurements.
- Explore the data using Exploratory Data Analysis (EDA) techniques.
- Identify key trends and valuable insights from the data to inform decision-making.
- Develop a data-driven strategy with recommendations.

## Installation

1. **Create a virtual environment (recommended) and activate it.**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

2. **Install required dependencies listed in requirements.txt:**

    ```bash
    pip install -r requirements.txt
    ```

3. **(Optional) Place your sample data in the data/ directory.**

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app/main.py
    ```

2. A web interface will open in your default browser, displaying the dashboard.

3. Interact with the dashboard elements as needed:

   - Upload your data.
   - Choose an analysis type and customize parameters.
   - Explore the visualizations and statistics.

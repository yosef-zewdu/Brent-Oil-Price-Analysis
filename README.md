# Brent Oil Price Analysis

This repository contains a project for analyzing how significant political and economic events impact Brent oil prices. The analysis aims to provide actionable insights for investors, policymakers, and energy companies to navigate the volatile oil market.

## Project Overview

As a data scientist at Birhan Energies, a consultancy specializing in energy sector insights, the main objective is to study the relationship between key events and Brent oil prices. This includes understanding how factors like political decisions, conflicts, sanctions, and OPEC policies correlate with price changes. The results of this analysis will support strategic decision-making for various stakeholders.

## Data Description

The dataset consists of historical daily Brent oil prices from May 20, 1987, to September 30, 2022.

- **Date**: Date of the recorded oil price.
- **Price**: Brent oil price in USD per barrel on the respective date.

## Objectives

1. **Detect Key Events**: Identify events that have significantly impacted oil prices.
2. **Quantify Impact**: Measure the extent of the impact of these events on price fluctuations.
3. **Provide Insights**: Generate insights to guide investment strategies, policy development, and planning.

## Key Tasks

### Task 1: Define Analysis Workflow
- Plan the steps required for analyzing Brent oil prices.
- Understand data generation, sampling, and model inputs.
- Identify assumptions and limitations of the analysis.

### Task 2: Time Series Analysis and Model Building
- Explore time series models like ARIMA, GARCH, and Bayesian approaches (using PyMC3).
- Implement advanced models such as LSTM or regime-switching ARIMA for different market conditions.
- Integrate economic indicators (GDP, inflation, exchange rates) and regulatory factors.

### Task 3: Dashboard Development
- Develop an interactive dashboard using Flask (backend) and React (frontend).
- Enable data visualization and exploration of how events affect Brent oil prices.

## Model Details

### Change Point Detection and Statistical Modeling
- Utilize PyMC3 for Bayesian inference and Monte Carlo Markov Chain (MCMC) modeling.
- Apply change point detection techniques to analyze structural changes in the time series data.

### Advanced Models
- **ARIMA/GARCH**: For traditional time series forecasting.
- **LSTM**: To capture complex patterns in the data.
- **Vector Autoregression (VAR)**: For multivariate time series analysis.
- **Markov-Switching Models**: For identifying regime changes.

## Dashboard Features

The dashboard application, built with Flask and React, includes:
- **Historical Trends**: View past Brent oil price data.
- **Event Highlighting**: Visualize the impact of specific events.
- **Filters and Comparisons**: Filter data, select date ranges, and compare different periods.



## Project Structure

```plaintext

Brent-Oil-Price-Analysis/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml               # GitHub Actions
├── src/
│   └── __init__.py
├── notebooks/
|   ├── eda.ipynb                       # Jupyter notebook for data cleaning and processing 
│   └── README.md                       # Description of notebooks directory 
├── tests/
|    ├── __init__.py
│    └── test_data.py
├── scripts/
|    ├── __init__.py
│    ├── eda.py                          # Script data processing, cleaning 
│    └── README.md                       # Description of scripts directory
│
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
├── LICENSE                              # License information
└── .gitignore                           # Files and directories to ignore in Git  
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yosef-zewdu/Brent-Oil-Price-Analysis.git
   cd Brent-Oil-Price-Analysis


2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv\Scripts\activate  # On Linux, use `venv/bin/activate`
   

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
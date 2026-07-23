# RetailPulse AI Copilot

An enterprise-style AI-powered Retail Analytics & Decision Intelligence Platform.

## Features

- CSV Upload
- Automatic Data Cleaning
- Feature Engineering
- Business KPIs
- Sales Forecasting
- Customer Churn Prediction
- SHAP Explainability
- AI Copilot

## Architecture we'll actually build
                User Upload
                     │
                     ▼
           Dataset Validation
                     │
                     ▼
         Schema Detection Engine
                     │
                     ▼
          Column Mapping Engine
                     │
                     ▼
          Data Cleaning Engine
                     │
                     ▼
      Feature Engineering Engine
                     │
                     ▼
          Analytics Engine
          │              │
          ▼              ▼
 Sales Forecast      Churn Model
          │              │
          └──────┬───────┘
                 ▼
          SHAP Explainability
                 ▼
         AI Copilot Context
                 ▼
         Streamlit Dashboard
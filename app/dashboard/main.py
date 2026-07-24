from pathlib import Path
import sys

# ----------------------------------------------------
# Add project root to Python path
# ----------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ----------------------------------------------------
# Imports
# ----------------------------------------------------
import streamlit as st

from app.auth.database import AuthDatabase
from app.auth.session import SessionManager

from app.dashboard.auth.auth_page import AuthPage
from app.dashboard.components.sidebar import Sidebar

from app.dashboard.pages.overview import OverviewPage
from app.dashboard.pages.sales import SalesPage
from app.dashboard.pages.customers import CustomerPage
from app.dashboard.pages.forecasting import ForecastPage
from app.dashboard.pages.ai_insights import AIInsightsPage
from app.dashboard.pages.settings import SettingsPage
from app.dashboard.pages.dataset import DatasetPage


# ----------------------------------------------------
# Initialize Database
# ----------------------------------------------------
AuthDatabase.initialize()


# ----------------------------------------------------
# Streamlit Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="RetailPulse AI",
    page_icon="📊",
    layout="wide",
)


# ----------------------------------------------------
# Dashboard Page Router
# ----------------------------------------------------
PAGE_ROUTES = {
    "📂 Dataset": DatasetPage,
    "🏠 Overview": OverviewPage,
    "📈 Sales Analytics": SalesPage,
    "👥 Customer Analytics": CustomerPage,
    "📊 Forecasting": ForecastPage,
    "🤖 AI Insights": AIInsightsPage,
    "⚙ Settings": SettingsPage,
}


# ----------------------------------------------------
# Main Application
# ----------------------------------------------------
if not SessionManager.is_authenticated():

    AuthPage.render()

else:

    page = Sidebar.render()

    PAGE_ROUTES[page].render()
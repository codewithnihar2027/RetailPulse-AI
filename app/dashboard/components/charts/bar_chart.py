import pandas as pd
import plotly.express as px
import streamlit as st


class BarChart:

    @staticmethod
    def render(data, title):

        df = pd.DataFrame(
            {
                "Category": list(data.keys()),
                "Value": list(data.values())
            }
        )

        fig = px.bar(
            df,
            x="Category",
            y="Value",
            title=title
        )

        fig.update_layout(
            height=450,
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
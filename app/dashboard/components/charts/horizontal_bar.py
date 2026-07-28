import pandas as pd
import plotly.express as px
import streamlit as st


class HorizontalBarChart:

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
            x="Value",
            y="Category",
            orientation="h",
            title=title
        )

        fig.update_layout(
            height=500,
            template="plotly_white",
            yaxis=dict(categoryorder="total ascending")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
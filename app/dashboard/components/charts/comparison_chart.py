import streamlit as st
import plotly.graph_objects as go


class ComparisonChart:

    @staticmethod
    def render(actual, predicted, title):

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=actual,
                mode="lines",
                name="Actual"
            )
        )

        fig.add_trace(
            go.Scatter(
                y=predicted,
                mode="lines",
                name="Predicted"
            )
        )

        fig.update_layout(
            title=title,
            template="plotly_dark",
            xaxis_title="Days",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
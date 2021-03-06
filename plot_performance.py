# -*- coding: utf-8 -*-
"""plot_performance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LxYj2qAktf4DXBvigU-HQbP23vHnfdnZ
"""

import plotly.express as px
# storing plot data
lst = []


def plot_line(df, y, name, color_):
    fig = px.line(df, x="epoch", y=y)
    lst.append(fig.update_traces(
        name=name, showlegend=True, line=dict(color=color_)).data)
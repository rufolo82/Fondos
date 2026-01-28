import streamlit as st
import pandas as pd
from data_sources.aggregator import get_fund_data

FUND_ISINS = [
    "ES0119199000",
]

st.set_page_config(page_title="Fondos de Inversión", layout="wide")
st.title("📊 Dashboard de Fondos de Inversión")

rows = []
for isin in FUND_ISINS:
    data = get_fund_data(isin)
    if data:
        data["ISIN"] = isin
        rows.append(data)

if not rows:
    st.error("❌ No se han podido cargar datos de los fondos. Intenta actualizar más tarde.")
    st.stop()

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

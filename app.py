import streamlit as st
import pandas as pd
from data_sources.aggregator import get_fund_data

FUND_ISINS = [
    "ES0119199000",
]

st.set_page_config(page_title="Fondos de Inversión", layout="wide")
st.title("📊 Dashboard de Fondos de Inversión")

st.info("Pulsa el botón para cargar los datos de los fondos.")

@st.cache_data(ttl=3600)
def load_funds(isins):
    rows = []
    for isin in isins:
        data = get_fund_data(isin)
        if data:
            data["ISIN"] = isin
            rows.append(data)
    return pd.DataFrame(rows)

if st.button("🔄 Cargar fondos"):
    with st.spinner("Cargando datos..."):
        df = load_funds(FUND_ISINS)

    if df.empty:
        st.error("❌ No se han podido cargar datos de los fondos.")
    else:
        st.dataframe(df, use_container_width=True)


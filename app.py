import streamlit as st
import pandas as pd
from data_sources.aggregator import get_fund_data

# LISTA COMPLETA DE ISIN
FUND_ISINS = [
    "ES0113728002",
    "ES0159202011",
    "ES0124037005",
    "ES0112611001",
    "ES0146309002",
    "ES0112602000",
    "ES0180782007",
    "ES0173311079",
    "ES0156673008",
    "LU1931536152",
    "ES0168797050",
    "ES0107696066",
    "ES0119199000",
    "ES0173311103",
    "ES0124037021",
    "ES0113728028",
    "ES0119199026",
    "ES0113728036",
    "ES0124037039",
    "ES0119199034",
    "FR0000989626",
    "ES0156572002",
    "IE00BD0NCM55",
    "IE00B42W3S00",
    "ES0141116006",
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
    with st.spinner("Cargando datos de los fondos..."):
        df = load_funds(FUND_ISINS)

    if df.empty:
        st.error("❌ No se han podido cargar datos de los fondos.")
    else:
        st.success(f"Fondos cargados: {len(df)}")
        st.dataframe(df, use_container_width=True)

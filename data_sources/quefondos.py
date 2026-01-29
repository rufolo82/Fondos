import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_from_quefondos(isin):
    url = f"https://www1.quefondos.com/es/fondos/ficha/index.html?isin={isin}"
    r = requests.get(url, headers=HEADERS, timeout=3)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # 🔍 DEBUG: devolver SOLO el nombre y el texto visible
    try:
        nombre = soup.find("h1").get_text(strip=True)
        texto = soup.get_text(" ", strip=True)

        return {
            "Nombre": nombre,
            "YTD (%)": texto[:200],   # 👈 SOLO para ver qué llega
            "1Y (%)": None,
            "3Y (%)": None,
            "5Y (%)": None,
            "TER": None,
            "País": None,
            "Fuente": "quefondos.com (debug)",
        }

    except Exception:
        return None

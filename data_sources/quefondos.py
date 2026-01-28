import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_from_quefondos(isin):
    url = f"https://www1.quefondos.com/es/fondos/ficha/index.html?isin={isin}"
    r = requests.get(url, headers=HEADERS, timeout=3)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        nombre = soup.find("h1").get_text(strip=True)
        return {
            "Nombre": nombre,
            "YTD (%)": None,
            "1Y (%)": None,
            "3Y (%)": None,
            "5Y (%)": None,
            "TER": None,
            "País": "España",
            "Fuente": "quefondos.com",
        }
    except Exception:
        return None

import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
}

def clean(value):
    if not value:
        return None
    return (
        value.replace("%", "")
        .replace(",", ".")
        .strip()
    )

def get_from_investing(isin):
    try:
        # 1️⃣ Buscar el fondo por ISIN
        search_url = f"https://www.investing.com/search/?q={isin}"
        r = requests.get(search_url, headers=HEADERS, timeout=3)
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.select_one("a.js-inner-all-results-quote-item")
        if not result:
            return None

        fund_url = "https://www.investing.com" + result["href"]

        # 2️⃣ Página del fondo
        r = requests.get(fund_url, headers=HEADERS, timeout=3)
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.text, "html.parser")

        nombre = soup.find("h1").get_text(strip=True)

        data = {
            "Nombre": nombre,
            "YTD (%)": None,
            "1Y (%)": None,
            "3Y (%)": None,
            "5Y (%)": None,
            "TER": None,
            "País": None,
            "Fuente": "investing.com",
        }

        text = soup.get_text(" ", strip=True)

        patterns = {
            "YTD (%)": r"YTD\s*([\d.,]+%)",
            "1Y (%)": r"1\s*Año\s*([\d.,]+%)",
            "3Y (%)": r"3\s*Años\s*([\d.,]+%)",
            "5Y (%)": r"5\s*Años\s*([\d.,]+%)",
            "TER": r"TER\s*([\d.,]+%)",
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            if match:
                data[key] = clean(match.group(1))

        return data

    except Exception:
        return None

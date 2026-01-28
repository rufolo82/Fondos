import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0", "Accept-Language": "es-ES"}

def get_from_investing(isin):
    search = f"https://www.investing.com/search/?q={isin}"
    r = requests.get(search, headers=HEADERS, timeout=3)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find("a", href=True)
    if not link:
        return None
    r = requests.get("https://www.investing.com" + link["href"], headers=HEADERS, timeout=10)
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
            "País": None,
            "Fuente": "investing.com",
        }
    except Exception:
        return None

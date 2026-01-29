import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def clean(text):
    return text.replace("%", "").replace(",", ".").strip()

def get_from_quefondos(isin):
    url = f"https://www1.quefondos.com/es/fondos/ficha/index.html?isin={isin}"
    r = requests.get(url, headers=HEADERS, timeout=3)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    try:
        nombre = soup.find("h1").get_text(strip=True)

        data = {
            "Nombre": nombre,
            "YTD (%)": None,
            "1Y (%)": None,
            "3Y (%)": None,
            "5Y (%)": None,
            "TER": None,
            "País": None,
            "Fuente": "quefondos.com",
        }

        # Buscar tabla de rentabilidades
        rows = soup.find_all("tr")
        for row in rows:
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cols) != 2:
                continue

            label, value = cols

            if "YTD" in label:
                data["YTD (%)"] = clean(value)
            elif "1 año" in label:
                data["1Y (%)"] = clean(value)
            elif "3 años" in label:
                data["3Y (%)"] = clean(value)
            elif "5 años" in label:
                data["5Y (%)"] = clean(value)
            elif "TER" in label:
                data["TER"] = clean(value)

        return data

    except Exception:
        return None

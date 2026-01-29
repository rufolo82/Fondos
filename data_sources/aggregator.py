from data_sources.investing import get_from_investing
from data_sources.finect import get_from_finect
from data_sources.quefondos import get_from_quefondos

def get_fund_data(isin):
    for source in (
        get_from_investing,   # 👈 principal
        get_from_finect,
        get_from_quefondos,
    ):
        data = source(isin)
        if data:
            return data
    return None

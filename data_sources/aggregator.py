from data_sources.quefondos import get_from_quefondos
from data_sources.finect import get_from_finect
from data_sources.investing import get_from_investing

def get_fund_data(isin):
    for source in (get_from_quefondos, get_from_finect, get_from_investing):
        data = source(isin)
        if data:
            return data
    return None

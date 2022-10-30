
from pandas import DataFrame

from app.stocks import fetch_stock_data


def test_fetch_stock_data():
    df = fetch_stock_data()
    assert isinstance(df, DataFrame)
    assert "timestamp" in df.columns
    assert "adjusted_close" in df.columns

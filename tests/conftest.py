import pandas as pd
import pytest

from betfairmarketvolumesclient.client import Client
from .utils import basepath


@pytest.fixture()
def mock_client() -> Client:
    return Client()


@pytest.fixture()
def mock_greyhound_place() -> pd.DataFrame:
    return pd.read_csv(f"{basepath}/resources/greyhoundplace.csv")


@pytest.fixture()
def mock_greyhound_win() -> pd.DataFrame:
    return pd.read_csv(f"{basepath}/resources/greyhoundwin.csv")


@pytest.fixture()
def mock_horse_racing_place() -> pd.DataFrame:
    return pd.read_csv(f"{basepath}/resources/horseracingplace.csv")


@pytest.fixture()
def mock_horse_racing_win() -> pd.DataFrame:
    return pd.read_csv(f"{basepath}/resources/horseracingwin.csv")

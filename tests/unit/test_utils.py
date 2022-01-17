from datetime import datetime

from pandas import DataFrame

from betfairmarketvolumesclient.resources.marketresource import MarketSelection
from betfairmarketvolumesclient.utils import (
    parse_from_data_frame,
    parse_to_data_frame,
    build_greyhound_url,
    build_horse_racing_url,
)


class TestUtils:
    def test_parse_from_data_frame(self, mock_greyhound_win: DataFrame):
        selections = parse_from_data_frame(mock_greyhound_win)
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_parse_to_data_frame(self, mock_greyhound_win: DataFrame):
        selections = parse_from_data_frame(mock_greyhound_win)

        df = parse_to_data_frame(selections)
        assert isinstance(df, DataFrame)

    def test_build_greyhound_url(self):
        assert (
                build_greyhound_url(
                    base_url="https://promo.betfair.com/betfairsp/prices/dwbf",
                    win_or_place="win",
                    date=datetime(2020, 1, 1),
                )
                == "https://promo.betfair.com/betfairsp/prices/dwbfgreyhoundwin01012020.csv"
        )

    def test_build_horse_racing_url(self):
        assert (
                build_horse_racing_url(
                    base_url="https://promo.betfair.com/betfairsp/prices/dwbf",
                    country="gb",
                    win_or_place="win",
                    date=datetime(2020, 1, 1),
                )
                == "https://promo.betfair.com/betfairsp/prices/dwbfpricesgbwin01012020.csv"
        )

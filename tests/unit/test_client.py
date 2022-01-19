from datetime import datetime
from typing import List

from pandas import DataFrame
from pytest_mock import MockFixture

from betfairmarketvolumesclient.client import Client
from betfairmarketvolumesclient.resources.marketresource import MarketSelection


class TestClient:
    def test___init__(self):
        client = Client()
        assert client.BASE_URL == "https://promo.betfair.com/betfairsp/prices/dwbf"
        assert client.request_timeout_sec == 120

    def test_get_gb_win_horse_racing_markets(
            self, mocker: MockFixture, mock_client: Client, mock_horse_racing_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_win,
        )
        selections: List[MarketSelection] = mock_client.get_gb_win_horse_racing_markets(
            datetime.utcnow()
        )
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_gb_place_horse_racing_markets(
            self,
            mocker: MockFixture,
            mock_client: Client,
            mock_horse_racing_place: DataFrame,
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_place,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_gb_place_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_ire_win_horse_racing_markets(
            self, mocker: MockFixture, mock_client: Client, mock_horse_racing_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_win,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_ire_win_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_ire_place_horse_racing_markets(
            self,
            mocker: MockFixture,
            mock_client: Client,
            mock_horse_racing_place: DataFrame,
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_place,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_ire_place_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_aus_win_horse_racing_markets(
            self, mocker: MockFixture, mock_client: Client, mock_horse_racing_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_win,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_aus_win_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_aus_place_horse_racing_markets(
            self,
            mocker: MockFixture,
            mock_client: Client,
            mock_horse_racing_place: DataFrame,
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_place,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_aus_place_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_usa_win_horse_racing_markets(
            self, mocker: MockFixture, mock_client: Client, mock_horse_racing_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_win,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_usa_win_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_usa_place_horse_racing_markets(
            self,
            mocker: MockFixture,
            mock_client: Client,
            mock_horse_racing_place: DataFrame,
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_place,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_usa_place_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_rsa_win_horse_racing_markets(
            self, mocker: MockFixture, mock_client: Client, mock_horse_racing_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_win,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_rsa_win_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_rsa_place_horse_racing_markets(
            self,
            mocker: MockFixture,
            mock_client: Client,
            mock_horse_racing_place: DataFrame,
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_horse_racing_place,
        )
        selections: List[
            MarketSelection
        ] = mock_client.get_rsa_place_horse_racing_markets(datetime.utcnow())
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_greyhound_win_markets(
            self, mocker: MockFixture, mock_client: Client, mock_greyhound_win: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_greyhound_win,
        )
        selections: List[MarketSelection] = mock_client.get_greyhound_win_markets(
            datetime.utcnow()
        )
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_greyhound_place_markets(
            self, mocker: MockFixture, mock_client: Client, mock_greyhound_place: DataFrame
    ):
        mocker.patch(
            "betfairmarketvolumesclient.client.Client._request",
            return_value=mock_greyhound_place,
        )
        selections: List[MarketSelection] = mock_client.get_greyhound_place_markets(
            datetime.utcnow()
        )
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

    def test_get_greyhound_markets_for_date(
            self, mocker: MockFixture, mock_client: Client
    ):
        win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_greyhound_win_markets"
        )
        place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_greyhound_place_markets"
        )
        mock_client.get_greyhound_markets_for_date(date=datetime.utcnow())
        win.assert_called()
        place.assert_called()

    def test_get_horse_racing_markets_for_date(
            self, mocker: MockFixture, mock_client: Client
    ):
        gb_win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_gb_win_horse_racing_markets"
        )
        gb_place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_gb_place_horse_racing_markets"
        )
        ire_win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_ire_win_horse_racing_markets"
        )
        ire_place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_ire_place_horse_racing_markets"
        )
        aus_win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_aus_win_horse_racing_markets"
        )
        aus_place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_aus_place_horse_racing_markets"
        )
        usa_win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_usa_win_horse_racing_markets"
        )
        usa_place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_usa_place_horse_racing_markets"
        )
        rsa_win = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_rsa_win_horse_racing_markets"
        )
        rsa_place = mocker.patch(
            "betfairmarketvolumesclient.client.Client.get_rsa_place_horse_racing_markets"
        )
        mock_client.get_horse_racing_markets_for_date(date=datetime.utcnow())
        gb_win.assert_called()
        gb_place.assert_called()
        ire_win.assert_called()
        ire_place.assert_called()
        aus_win.assert_called()
        aus_place.assert_called()
        usa_win.assert_called()
        usa_place.assert_called()
        rsa_win.assert_called()
        rsa_place.assert_called()

    def test__process_data(self, mock_client: Client, mock_greyhound_win: DataFrame):
        selections = mock_client._process_data(mock_greyhound_win)
        assert isinstance(selections, list)
        for s in selections:
            assert isinstance(s, MarketSelection)

        selections = mock_client._process_data([])
        assert selections == []

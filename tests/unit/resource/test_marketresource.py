from datetime import datetime

from betfairmarketvolumesclient.resources import MarketSelection


class TestMarketSelectionResource:
    def test___init__(self):
        market_selection = MarketSelection(
            event_id=175829050,
            menu_hint="IRE / Dund  23rd Nov",
            event_name="7f Hcap",
            event_dt=datetime(2020, 11, 23, 14, 55),
            selection_id=19450847,
            selection_name="Hiella",
            win_lose=0,
            bsp=10.564986,
            pp_wap=11.17356,
            morning_wap=15.82474,
            pp_max=18,
            pp_min=9.6,
            ip_max=1000,
            ip_min=11,
            morning_traded_volume=100.36,
            pp_traded_volume=10825.92,
            ip_traded_volume=1229,
        )
        assert market_selection.event_id == 175829050
        assert market_selection.menu_hint == "IRE / Dund  23rd Nov"
        assert market_selection.event_name == "7f Hcap"
        assert market_selection.event_dt == datetime(2020, 11, 23, 14, 55)
        assert market_selection.selection_id == 19450847
        assert market_selection.selection_name == "Hiella"
        assert market_selection.win_lose == 0
        assert market_selection.bsp == 10.564986
        assert market_selection.pp_wap == 11.17356
        assert market_selection.morning_wap == 15.82474
        assert market_selection.pp_max == 18
        assert market_selection.pp_min == 9.6
        assert market_selection.ip_max == 1000
        assert market_selection.ip_min == 11
        assert market_selection.morning_traded_volume == 100.36
        assert market_selection.pp_traded_volume == 10825.92
        assert market_selection.ip_traded_volume == 1229
        assert market_selection.market_id == "1.175829050"
        assert market_selection.is_place_market is False
        assert market_selection.is_forecast_market is False
        assert market_selection.is_alternative_market is False
        assert market_selection.is_win_market

        market_selection.event_name = "to be placed"
        assert market_selection.is_place_market
        assert market_selection.is_win_market is False

        market_selection.event_name = "forecast"
        assert market_selection.is_forecast_market
        assert market_selection.is_win_market is False

        market_selection.event_name = "each way"
        assert market_selection.is_alternative_market
        assert market_selection.is_win_market is False

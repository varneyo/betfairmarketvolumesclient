import logging
from datetime import datetime
from typing import Optional, List
from urllib.error import HTTPError

import pandas as pd
from tenacity import retry, wait_exponential, stop_after_attempt

from betfairmarketvolumesclient.resources.marketresource import MarketSelection
from betfairmarketvolumesclient.utils import (
    parse_from_data_frame,
    build_horse_racing_url,
    build_greyhound_url,
)

logger = logging.getLogger(__name__)


class Client:
    BASE_URL = "https://promo.betfair.com/betfairsp/prices/dwbf"

    def __init__(self, request_timeout_sec: int = 120):
        self.request_timeout_sec = request_timeout_sec  # TODO

    @retry(
        wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3)
    )
    def _request(self, url: str) -> Optional[pd.DataFrame]:

        logger.info(f"Requesting data for {url}")
        try:
            return pd.read_csv(url)
        except HTTPError as e:
            logger.error(f"Issue retrieving data for url: {url}, with exception: {e}")

    def _process_data(self, data: pd.DataFrame) -> List[MarketSelection]:
        if isinstance(data, pd.DataFrame) and data.shape[0] > 0:
            return parse_from_data_frame(data=data)
        return []

    def get_gb_win_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL, country="uk", win_or_place="win", date=date
                )
            )
        )

    def get_gb_place_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL,
                    country="uk",
                    win_or_place="place",
                    date=date,
                )
            )
        )

    def get_ire_win_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL, country="ire", win_or_place="win", date=date
                )
            )
        )

    def get_ire_place_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL,
                    country="ire",
                    win_or_place="place",
                    date=date,
                )
            )
        )

    def get_aus_win_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL, country="aus", win_or_place="win", date=date
                )
            )
        )

    def get_aus_place_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL,
                    country="aus",
                    win_or_place="place",
                    date=date,
                )
            )
        )

    def get_usa_win_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL, country="usa", win_or_place="win", date=date
                )
            )
        )

    def get_usa_place_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL,
                    country="usa",
                    win_or_place="place",
                    date=date,
                )
            )
        )

    def get_rsa_win_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL, country="rsa", win_or_place="win", date=date
                )
            )
        )

    def get_rsa_place_horse_racing_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_horse_racing_url(
                    base_url=self.BASE_URL,
                    country="rsa",
                    win_or_place="place",
                    date=date,
                )
            )
        )

    def get_horse_racing_markets_for_date(
            self,
            date: datetime,
            include_win_markets: bool = True,
            include_place_markets: bool = True,
            include_gb: bool = True,
            include_ire: bool = True,
            include_aus: bool = True,
            include_usa: bool = True,
            include_rsa: bool = True,
    ):
        all_selections = []

        if include_gb:
            if include_win_markets:
                all_selections.extend(self.get_gb_win_horse_racing_markets(date=date))
            if include_place_markets:
                all_selections.extend(self.get_gb_place_horse_racing_markets(date=date))

        if include_ire:
            if include_win_markets:
                all_selections.extend(self.get_ire_win_horse_racing_markets(date=date))
            if include_place_markets:
                all_selections.extend(
                    self.get_ire_place_horse_racing_markets(date=date)
                )

        if include_aus:
            if include_win_markets:
                all_selections.extend(self.get_aus_win_horse_racing_markets(date=date))
            if include_place_markets:
                all_selections.extend(
                    self.get_aus_place_horse_racing_markets(date=date)
                )

        if include_usa:
            if include_win_markets:
                all_selections.extend(self.get_usa_win_horse_racing_markets(date=date))
            if include_place_markets:
                all_selections.extend(
                    self.get_usa_place_horse_racing_markets(date=date)
                )

        if include_rsa:
            if include_win_markets:
                all_selections.extend(self.get_rsa_win_horse_racing_markets(date=date))
            if include_place_markets:
                all_selections.extend(
                    self.get_rsa_place_horse_racing_markets(date=date)
                )

        return all_selections

    def get_greyhound_win_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_greyhound_url(
                    base_url=self.BASE_URL, win_or_place="win", date=date
                )
            )
        )

    def get_greyhound_place_markets(self, date: datetime) -> List[MarketSelection]:
        return self._process_data(
            self._request(
                url=build_greyhound_url(
                    base_url=self.BASE_URL, win_or_place="place", date=date
                )
            )
        )

    def get_greyhound_markets_for_date(
            self,
            date: datetime,
            include_win_markets: bool = True,
            include_place_markets: bool = True,
    ):
        all_selections = []

        if include_win_markets:
            all_selections.extend(self.get_greyhound_win_markets(date=date))
        if include_place_markets:
            all_selections.extend(self.get_greyhound_place_markets(date=date))

        return all_selections

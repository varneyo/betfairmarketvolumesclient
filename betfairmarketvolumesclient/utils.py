import logging
from datetime import datetime
from typing import List, Optional

from pandas import DataFrame

from betfairmarketvolumesclient.resources.marketresource import MarketSelection

logger = logging.getLogger(__name__)


def parse_from_data_frame(data: DataFrame) -> List[MarketSelection]:
    if isinstance(data, DataFrame):
        try:
            return [MarketSelection(**d) for d in data.to_dict("records")]
        except Exception as e:
            logger.error(f"Issue parsing selections, {e}")
    return []


def parse_to_data_frame(data: List[MarketSelection]) -> Optional[DataFrame]:
    if isinstance(data, list):
        try:
            return DataFrame([d.dict() for d in data])
        except Exception as e:
            logger.error(f"Issue parsing selections, {e}")


def build_greyhound_url(base_url: str, win_or_place: str, date: datetime) -> str:
    return f"{base_url}greyhound{win_or_place}{date.strftime('%d%m%Y')}.csv"


def build_horse_racing_url(
        base_url: str, country: str, win_or_place: str, date: datetime
) -> str:
    return f"{base_url}prices{country}{win_or_place}{date.strftime('%d%m%Y')}.csv"

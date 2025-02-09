import logging
from datetime import datetime
from typing import List, Optional

from pandas import DataFrame

from betfairmarketvolumesclient.resources.marketresource import MarketSelection

logger = logging.getLogger(__name__)


def parse_from_data_frame(
    data: DataFrame, file_url: str, country: str
) -> List[MarketSelection]:
    all: List[MarketSelection] = []
    if isinstance(data, DataFrame):
        try:
            data.columns = [x.upper() for x in data.columns]
            for d in data.to_dict("records"):
                all.append(MarketSelection(**{**d, **{"_file_url": file_url, "country": country}}))
        except Exception as e:
            logger.error(f"Issue parsing selections, {e}")
        return all
    return []


def parse_to_data_frame(data: List[MarketSelection]) -> Optional[DataFrame]:
    if isinstance(data, list):
        try:
            return DataFrame([d.model_dump() for d in data])
        except Exception as e:
            logger.error(f"Issue parsing selections, {e}")


def build_greyhound_url(base_url: str, win_or_place: str, date: datetime) -> str:
    return f"{base_url}greyhound{win_or_place}{date.strftime('%d%m%Y')}.csv"


def build_horse_racing_url(
    base_url: str, country: str, win_or_place: str, date: datetime
) -> str:
    return f"{base_url}prices{country}{win_or_place}{date.strftime('%d%m%Y')}.csv"

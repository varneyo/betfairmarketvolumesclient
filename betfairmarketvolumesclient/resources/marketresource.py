from datetime import datetime
from typing import Union, Optional

from pydantic import Field, validator

from .baseresource import BaseResource


class MarketSelection(BaseResource):
    event_id: int = Field(alias="EVENT_ID")
    menu_hint: str = Field(alias="MENU_HINT")
    event_name: str = Field(alias="EVENT_NAME")
    event_dt: datetime = Field(alias="EVENT_DT")
    selection_id: int = Field(alias="SELECTION_ID")
    selection_name: str = Field(alias="SELECTION_NAME")
    win_lose: int = Field(alias="WIN_LOSE")
    bsp: float = Field(alias="BSP")
    pp_wap: float = Field(alias="PPWAP")
    morning_wap: float = Field(alias="PPMIN")
    pp_max: float = Field(alias="PPMAX")
    pp_min: float = Field(alias="PPMIN")
    ip_max: float = Field(alias="IPMAX")
    ip_min: float = Field(alias="IPMIN")
    morning_traded_volume: float = Field(alias="MORNINGTRADEDVOL")
    pp_traded_volume: float = Field(alias="PPTRADEDVOL")
    ip_traded_volume: float = Field(alias="IPTRADEDVOL")
    country: Optional[str] = None
    _file_url: Optional[str] = None

    @validator("event_dt", pre=True)
    def parse_event_dt(cls, v: Union[datetime, str]) -> datetime:
        if isinstance(v, datetime):
            return v
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d-%m-%Y %H:%M")
            except ValueError:
                pass
            return datetime.fromisoformat(v)

    @property
    def market_id(self) -> str:
        return f"1.{self.event_id}"

    @property
    def is_win_market(self) -> bool:
        return (
            True
            if (self.is_place_market is False)
               and (self.is_forecast_market is False)
               and (self.is_alternative_market is False)
            else False
        )

    @property
    def is_place_market(self) -> bool:
        return True if self.event_name.lower() == "to be placed" else False

    @property
    def is_forecast_market(self) -> bool:
        return (
            True
            if self.event_name.lower() in ["forecast", "forecsat", "reverse fc"]
            else False
        )

    @property
    def is_alternative_market(self) -> bool:
        return (
            True
            if (self.event_name.lower() in ["official going", "each way", "yes", "no"])
               or ("tbp" in self.event_name.lower())
            else False
        )

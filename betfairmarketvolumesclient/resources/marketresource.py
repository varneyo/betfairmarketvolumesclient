from datetime import datetime
from typing import Optional
import math
from pydantic import Field, computed_field, model_validator

from .baseresource import BaseResource


class MarketSelection(BaseResource):
    event_id: int = Field(alias="EVENT_ID")
    menu_hint: str = Field(alias="MENU_HINT")
    event_name: str = Field(alias="EVENT_NAME")
    event_dt: datetime = Field(alias="EVENT_DT")
    selection_id: int = Field(alias="SELECTION_ID")
    selection_name: str = Field(alias="SELECTION_NAME")
    win_lose: int = Field(alias="WIN_LOSE")
    bsp: Optional[float] = Field(None, alias="BSP")
    pp_wap: Optional[float] = Field(None, alias="PPWAP")
    morning_wap: float = Field(alias="MORNINGWAP")
    pp_max: float = Field(alias="PPMAX")
    pp_min: float = Field(alias="PPMIN")
    ip_max: float = Field(alias="IPMAX")
    ip_min: float = Field(alias="IPMIN")
    morning_traded_volume: float = Field(alias="MORNINGTRADEDVOL")
    pp_traded_volume: float = Field(alias="PPTRADEDVOL")
    ip_traded_volume: float = Field(alias="IPTRADEDVOL")
    country: Optional[str] = None
    _file_url: Optional[str] = None

    @model_validator(mode='before')
    def parse_event_dt(cls, data: dict) -> dict:
        if isinstance(data.get("EVENT_DT"), str):
            try:
                data["EVENT_DT"] = datetime.strptime(data["EVENT_DT"], "%d-%m-%Y %H:%M")
            except ValueError:
                data["EVENT_DT"] = datetime.fromisoformat(data["EVENT_DT"])
        return data

    @model_validator(mode='before')
    def parse_bsp_ppwap(cls, data: dict) -> dict:
        for field in ["BSP", "PPWAP"]:
            v = data.get(field)
            if v:
                if math.isnan(v):
                    data[field] = None
                elif isinstance(v, int):
                    data[field] = float(v)
        return data

    @computed_field
    @property
    def file_url(self) -> Optional[str]:
        return self._file_url

    @computed_field
    @property
    def market_id(self) -> str:
        return f"1.{self.event_id}"

    @computed_field
    @property
    def is_win_market(self) -> bool:
        return (
            True
            if (self.is_place_market is False)
            and (self.is_forecast_market is False)
            and (self.is_alternative_market is False)
            else False
        )

    @computed_field
    @property
    def is_place_market(self) -> bool:
        return True if self.event_name.lower() == "to be placed" else False

    @computed_field
    @property
    def is_forecast_market(self) -> bool:
        return (
            True
            if self.event_name.lower() in ["forecast", "forecsat", "reverse fc"]
            else False
        )

    @computed_field
    @property
    def is_alternative_market(self) -> bool:
        return (
            True
            if (self.event_name.lower() in ["official going", "each way", "yes", "no"])
            or ("tbp" in self.event_name.lower())
            else False
        )

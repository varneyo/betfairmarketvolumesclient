from datetime import datetime

from pydantic import Field, validator

from .baseresource import BaseResource


class Selection(BaseResource):
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

    @validator('event_dt', pre=True)
    def parse_event_dt(cls, v: str) -> datetime:
        if isinstance(v, str):
            return datetime.strptime(v, "%d-%m-%Y %H:%M")

    @property
    def market_id(self) -> str:
        return f"1.{self.event_id}"

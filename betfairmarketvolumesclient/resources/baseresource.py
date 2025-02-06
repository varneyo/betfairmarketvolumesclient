from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class BaseResource(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra='allow'
    )

    def info(self) -> Dict[str, Any]:
        return self.model_dump()

    def raw(self, exclude_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        exclude_fields = exclude_fields if exclude_fields else {}
        assert isinstance(exclude_fields, dict)
        return self.model_dump(by_alias=True, exclude=exclude_fields)

    # helper function for backwards compatibility
    @classmethod
    def create_from_dict(cls, d: Dict[str, Any]) -> "BaseResource":
        return cls.model_validate(d)

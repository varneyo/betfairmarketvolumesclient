from pydantic import BaseModel, ConfigDict


class BaseResource(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    @property
    def info(self):
        return self.model_dump()

    @property
    def _raw(self, exclude_fields: dict = None):
        exclude_fields = exclude_fields if exclude_fields else {}
        assert isinstance(exclude_fields, dict)
        return self.model_dump(by_alias=True, exclude=exclude_fields)

    # helper function for backwards compatibility ?
    @classmethod
    def create_from_dict(cls, d):
        return cls.model_validate(d)

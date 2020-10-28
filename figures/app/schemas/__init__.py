"""App schemas."""
import pydantic

from datetime import date, datetime


IdType = pydantic.constr(regex=r"^[0-9a-f]{24}$")


class Model(pydantic.BaseModel):

    @classmethod
    def from_mongo(cls, data):
        data['id'] = str(data['_id'])
        return cls(**data)

    def to_mongo(self):
        data = self.dict()
        return {k: datetime(v.year, v.month, v.day)
                if isinstance(v, date) else v
                for k, v in data.items()}

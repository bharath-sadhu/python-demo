from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt, PastDatetime, EmailStr

from .entities import StationType


class System(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    supreme_commander: EmailStr
    supreme_commander_name: str
    date_created: PastDatetime


class CreateSystem(BaseModel):
    name: str
    supreme_commander: EmailStr

    class config:
        strict = True


class CreatePlanet(BaseModel):
    name: str = Field(strict=True)
    project_id: UUID
    population_millions: NonNegativeInt = Field(strict=True)
    system_id: str = Field(strict=True)


class UpdatePlanet(BaseModel):
    name: str = Field(strict=True)
    population_millions: NonNegativeInt = Field(strict=True)


class Planet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    project_id: UUID
    population_millions: NonNegativeInt
    system_id: UUID
    system: System


class CreateStation(BaseModel):
    name: str = Field(strict=True)
    commander: str = Field(strict=True)
    established_on: PastDatetime
    type: StationType
    planet_id: UUID


class UpdateStation(BaseModel):
    name: str = Field(strict=True)
    commander: str = Field(strict=True)
    established_on: PastDatetime
    type: StationType


class Station(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    commander: str
    established_on: PastDatetime
    type: StationType
    planet_id: UUID
    planet: Planet

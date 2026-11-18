from pydantic import Field, BaseModel, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    station = SpaceStation(
        station_id="ISS001",
        name="NyahSS!",
        crew_size=13,
        power_level=77.8,
        oxygen_level=90.3,
        last_maintenance=datetime(year=2026, month=4, day=26)
    )
    print("Valid station created:")
    for key, value in station.model_dump().items():
        print(f"{key}: {value}")
    print("========================================")

    print("\nExpected validation error:")
    try:
        bad_station = SpaceStation(
            station_id="ISS001",
            name="NyahSS!",
            crew_size=200000000,
            power_level=77.8,
            oxygen_level=90.3,
            last_maintenance=datetime(year=2026, month=4, day=26)
        )
        print("Valid station created?")
        for key, value in bad_station.model_dump().items():
            print(f"{key}: {value}")
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()

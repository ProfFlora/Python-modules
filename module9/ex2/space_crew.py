from pydantic import Field, ValidationError, model_validator, BaseModel
from datetime import datetime
from enum import Enum
from typing import List


class Rank(Enum):
    cadet = "Cadet"
    officer = "Officer"
    lieutenant = "Lieutenant"
    captain = "Captain"
    commander = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> SpaceMission:
        errors: list[str] = []

        if not self.mission_id.startswith("M"):
            errors.append("Mission ID must start with 'M'")

        if all(member.rank.value != "Commander" for member in self.crew) and \
           all(member.rank.value != "Captain" for member in self.crew):
            errors.append(
                "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            if len([cm for cm in self.crew if cm.years_experience >= 5]) < \
               (len(self.crew) // 2):
                errors.append(
                    "Long missions (> 365 days) need 50% experienced crew"
                    "(5+ years)"
                    )

        if not all(cm.is_active for cm in self.crew):
            errors.append("All crew members must be active")

        if errors:
            raise ValueError(" | ".join(errors))

        return self


def main() -> None:
    print("Space Mission Data Validation")
    print("========================================")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 4, 26),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="CM01",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=42,
                    specialization="Mission Command",
                    years_experience=8,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=43,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM03",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=44,
                    specialization="Engineering",
                    years_experience=3,
                    is_active=True
                )
            ],
            budget_millions=6700.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Launch Date: {mission.launch_date}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions} million")
        print(f"Status: {mission.mission_status}")
        print(f"Crew Size: {len(mission.crew)} members")
        print("Crew Members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) = ",
                  member.specialization)
    except ValidationError as e:
        print(e)

    print("\n========================================")
    print("Expected validation error:")
    try:
        bad_mission = SpaceMission(
            mission_id="2024_MARS",
            mission_name="Mars Colonialism Establishment",
            destination="Mars",
            launch_date=datetime(2026, 4, 26),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="CM02",
                    name="Joe Mama",
                    rank=Rank.lieutenant,
                    age=25,
                    specialization="Navigation",
                    years_experience=2,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM03",
                    name="Jessica Jones",
                    rank=Rank.officer,
                    age=48,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=False
                )
            ],
            budget_millions=6900.0
        )
        print("Valid mission created:")
        print(f"Mission: {bad_mission.mission_name}")
        print(f"ID: {bad_mission.mission_id}")
        print(f"Destination: {bad_mission.destination}")
        print(f"Launch Date: {bad_mission.launch_date}")
        print(f"Duration: {bad_mission.duration_days} days")
        print(f"Budget: ${bad_mission.budget_millions} million")
        print(f"Status: {bad_mission.mission_status}")
        print(f"Crew Size: {len(bad_mission.crew)} members")
        print("Crew Members:")
        for member in bad_mission.crew:
            print(f"- {member.name} ({member.rank.value}) = ",
                  member.specialization)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()

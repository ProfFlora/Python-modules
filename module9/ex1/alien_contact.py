from pydantic import Field, ValidationError, model_validator, BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_ID(self) -> AlienContact:
        if not self.contact_id.startswith("AC"):

            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
                )
        return self

    @model_validator(mode='after')
    def validate_physical(self) -> AlienContact:
        if self.contact_type == ContactType.physical and not self.is_verified:

            raise ValueError(
                "Physical contact reports must be verified"
            )
        return self

    @model_validator(mode='after')
    def validate_telepathic(self) -> AlienContact:
        if self.contact_type == ContactType.telepathic and \
           self.witness_count < 3:

            raise ValueError(
                "Telepathic contact requires at least 3 witnesses",
            )
        return self

    @model_validator(mode='after')
    def validate_strong(self) -> AlienContact:
        if self.signal_strength > 7.0 and self.message_received is None:

            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    try:
        report = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-01-01",
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {report.contact_id}")
        print(f"Type: {report.contact_type}")
        print(f"Location: {report.location}")
        print(f"Signal: {report.signal_strength}/10")
        print(f"Duration: {report.duration_minutes} minutes")
        print(f"Witnesses: {report.witness_count}")
        print(f"Messsage: {report.message_received}\n")
    except ValidationError as e:
        print(e)

    print("========================================")
    print("Expected validation error:")
    try:
        bad_report = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-01-02",
            contact_type=ContactType.telepathic,
            location="Area 67, New Mexico",
            signal_strength=4.2,
            duration_minutes=90,
            witness_count=2,
            message_received="Rawr... X3 *nuzzles* UwU"
        )
        print(bad_report.message_received)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()

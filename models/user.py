from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class AmplitudeCBUser:
    """Defines a user data model based on Crowdbotics user to be identified in Amplitude"""

    user_id: str
    name: str
    email: str

    def dict(self) -> Dict[str, Any]:
        return asdict(self)

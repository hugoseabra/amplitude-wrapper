from dataclasses import dataclass, asdict
from typing import Any, Dict

from .user import AmplitudeCBUser


@dataclass
class AmplitudeCBProject:
    """Defines a user data model based on Crowdbotics project"""

    project_id: int
    name: str
    owner: AmplitudeCBUser

    def dict(self) -> Dict[str, Any]:
        return asdict(self)

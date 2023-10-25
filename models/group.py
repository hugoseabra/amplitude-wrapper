from dataclasses import dataclass, asdict
from typing import Any, Dict, List


@dataclass
class AmplitudeCBOrgGroup:
    """Defines a group model based on Crowdbotics Organization"""

    group_name: List[str]
    group_type: str = "org_id"

    def dict(self) -> Dict[str, Any]:
        return asdict(self)

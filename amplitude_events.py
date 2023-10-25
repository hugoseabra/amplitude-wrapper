from typing import List

from .base import AmplitudeBaseEvent
from .models import AmplitudeCBUser, AmplitudeCBOrgGroup


class UserEvent(AmplitudeBaseEvent):
    USER_REGISTRATION_SUCCEEDED = "USER_REGISTRATION_SUCCEEDED"
    USER_REGISTRATION_FAILED = "USER_REGISTRATION_SUCCEEDED"

    USER_2MULTI_FACTOR_ENABLED = "AUTH_2MULTI_FACTOR_ENABLED"
    USER_2MULTI_FACTOR_DISABLED = "AUTH_2MULTI_FACTOR_DISABLED"
    USER_PASSWORD_CHANGED = "AUTH_PASSWORD_CHANGED"

    PROFILE_CHANGED = "PROFILE_CHANGED"

    def identified(self, name: str, email: str):
        self._dispatch_user_identify(
            user=AmplitudeCBUser(
                name=name,
                email=email,
                user_id=self.user_id,
            )
        )

    def orgs_added(self, names: List[str]):
        self._dispatch_add_groups_to_user(group=AmplitudeCBOrgGroup(group_name=names))

from typing import Dict, Any

from amplitude import BaseEvent

from .models import AmplitudeEventProperties, AmplitudeCBUser, AmplitudeCBOrgGroup
from .tracker import AmplitudeTracker


class AmplitudeBaseEvent:
    def __init__(self, api_key: str, user_id: str):
        self.api_key = api_key
        self.user_id = user_id
        self._properties: Dict[str, Any] = {}

        self.tracker = AmplitudeTracker(api_key=self.api_key)

    def set_properties(self, **kwargs) -> "AmplitudeBaseEvent":
        """Sets event properties"""
        self._properties = kwargs
        return self

    def _dispatch_properties(self, event_type: str) -> AmplitudeEventProperties:
        return AmplitudeEventProperties(
            event_type=event_type,
            user_id=self.user_id,
            **self._properties,
        )

    def _dispatch(self, action: str) -> BaseEvent:
        self._properties["event_type"] = str(action)
        event = BaseEvent(**self._properties)
        return event

    def _dispatch_user_identify(self, user: AmplitudeCBUser) -> None:
        self.tracker.identify(user=user)

    def _dispatch_add_groups_to_user(self, group: AmplitudeCBOrgGroup) -> None:
        self.tracker.add_groups_to_user(group=group, user_id=self.user_id)

    def _dispatch(self, action: str) -> None:
        event = self._dispatch(action=action)
        self.tracker.track(event=event, user_id=self.user_id)

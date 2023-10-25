from .base import AmplitudeBaseEvent


class PageViewEvent(AmplitudeBaseEvent):
    PAGE_VIEWED = "PAGE_VIEWED"

    def viewed(self):
        return self._dispatch(action=self.PAGE_VIEWED)

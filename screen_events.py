from .base import AmplitudeBaseEvent


class ScreenEvent(AmplitudeBaseEvent):
    SCREEN_CREATED = "SCREEN_CREATED"
    SCREEN_CREATED_WITH_AI = "SCREEN_CREATED_WITH_AI"
    SCREEN_UPDATED = "SCREEN_UPDATED"
    SCREEN_UPDATED_WITH_AI = "SCREEN_UPDATED_WITH_AI"
    SCREEN_ADDED = "SCREEN_ADDED"
    SCREEN_PUBLISHED = "SCREEN_PUBLISHED"
    SCREEN_DELETED = "SCREEN_DELETED"

    def created(self):
        return self._dispatch(action=self.SCREEN_CREATED)

    def created_with_ai(self):
        return self._dispatch(action=self.SCREEN_CREATED_WITH_AI)

    def updated(self):
        return self._dispatch(action=self.SCREEN_UPDATED)

    def updated_with_ia(self):
        return self._dispatch(action=self.SCREEN_UPDATED_WITH_AI)

    def added(self):
        return self._dispatch(action=self.SCREEN_ADDED)

    def published(self):
        return self._dispatch(action=self.SCREEN_PUBLISHED)

    def deleted(self):
        return self._dispatch(action=self.SCREEN_DELETED)

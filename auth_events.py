from .base import AmplitudeBaseEvent


class AuthEvent(AmplitudeBaseEvent):
    AUTH_FAILED = "AUTH_AUTH_FAILED"
    AUTH_LOGGED_IN = "AUTH_LOGGED_IN"
    AUTH_LOGGED_OUT = "AUTH_LOGGED_OUT"

    def logged_in(self):
        return self._dispatch(action=self.AUTH_LOGGED_IN)

    def logged_out(self):
        return self._dispatch(action=self.AUTH_LOGGED_OUT)

    def failed(self):
        return self._dispatch(action=self.AUTH_FAILED)

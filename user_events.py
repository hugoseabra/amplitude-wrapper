from .base import AmplitudeBaseEvent


class UserEvent(AmplitudeBaseEvent):
    USER_REGISTRATION_SUCCEEDED = "USER_REGISTRATION_SUCCEEDED"
    USER_REGISTRATION_FAILED = "USER_REGISTRATION_SUCCEEDED"

    USER_2MULTI_FACTOR_ENABLED = "AUTH_2MULTI_FACTOR_ENABLED"
    USER_2MULTI_FACTOR_DISABLED = "AUTH_2MULTI_FACTOR_DISABLED"
    USER_PASSWORD_CHANGED = "AUTH_PASSWORD_CHANGED"

    PROFILE_CHANGED = "PROFILE_CHANGED"

    def registration_succeeded(self):
        return self._dispatch(action=self.USER_REGISTRATION_SUCCEEDED)

    def registration_failed(self):
        return self._dispatch(action=self.USER_REGISTRATION_FAILED)

    def two_multi_fa_enabled(self):
        return self._dispatch(action=self.USER_2MULTI_FACTOR_ENABLED)

    def two_multi_fa_disabled(self):
        return self._dispatch(action=self.USER_2MULTI_FACTOR_DISABLED)

    def password_changed(self):
        return self._dispatch(action=self.USER_PASSWORD_CHANGED)

    def profile_changed(self):
        return self._dispatch(action=self.USER_REGISTRATION_FAILED)

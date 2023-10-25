from .base import AmplitudeBaseEvent
from .models import AmplitudeCBProject, AmplitudeCBUser


class ProjectEvent(AmplitudeBaseEvent):
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    PROJECT_DEPLOY_SUCCEEDED = "PROJECT_DEPLOY_SUCCEEDED"
    PROJECT_DEPLOY_FAILED = "PROJECT_DEPLOY_FAILED"

    def set_project(
        self, project_id: int, name: str, owner: AmplitudeCBUser
    ) -> "ProjectEvent":
        """Creates an Amplitude Crowdbotics project object"""
        data = AmplitudeCBProject(project_id=project_id, name=name, owner=owner)
        self.set_properties(project=data.dict())
        return self

    def created(self):
        return self._dispatch(action=self.PROJECT_CREATED)

    def deleted(self):
        return self._dispatch(action=self.PROJECT_DELETED)

    def deploy_succeeded(self):
        return self._dispatch(action=self.PROJECT_DEPLOY_SUCCEEDED)

    def deploy_failed(self):
        return self._dispatch(action=self.PROJECT_DEPLOY_FAILED)

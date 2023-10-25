import asyncio
import logging
from typing import Optional

import amplitude

from .models import AmplitudeCBUser, AmplitudeCBOrgGroup

logger = logging.getLogger("AmplitudeTracker")


class AmplitudeAPIError(Exception):
    """Raised when interaction with Amplitude API fails."""


class AmplitudeTracker:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = amplitude.Amplitude(api_key=self.api_key)
        self.client.configuration.use_batch = True

    def identify(self, user: AmplitudeCBUser) -> None:
        """Sends user identification to amplitude"""
        identify = amplitude.Identify()
        for prop, value in user.dict().items():
            identify.set(key=prop, value=value)

        try:
            task = asyncio.create_task(
                coro=self.client.identify(
                    identify_obj=identify,
                    event_options=amplitude.EventOptions(str(user.user_id)),
                ),
                name="amplitue-identify-user",
            )
            asyncio.run(task)

            logger.info(
                f'Event "user-identify" tracked successfully for user {user.user_id}'
            )

        except Exception as e:
            logger.exception(f"Error occurred: {e}")
            raise AmplitudeAPIError(f"Error occurred: {e}")

    def add_groups_to_user(
        self, group: AmplitudeCBOrgGroup, user_id: str, owner: Optional[bool] = False
    ) -> None:
        """Adds an Amplitude identification of the user related to groups"""
        identify = amplitude.Identify()
        identify.set("owner", owner)
        event_options = amplitude.EventOptions(str(user_id))

        try:
            task = asyncio.create_task(
                coro=self.client.group_identify(
                    event_options=event_options, identify_obj=identify, **group.dict()
                ),
                name="amplitude-add-groups-to-user",
            )
            asyncio.run(task)

            logger.info(
                f'Event "group-identify" tracked successfully for user {user_id}'
            )

        except Exception as e:
            logger.exception(f"Error occurred: {e}")
            raise AmplitudeAPIError(f"Error occurred: {e}")

    def track(self, event: amplitude.BaseEvent, user_id: str):
        event.user_id = user_id

        try:
            task = asyncio.create_task(
                coro=self.client.track(event), name="amplitude-track-event"
            )
            asyncio.run(task)

            logger.info(
                f'Event "{event.event_type}" tracked successfully'
                f" for user {user_id}"
            )

        except Exception as e:
            logger.exception(f"Error occurred: {e}")
            raise AmplitudeAPIError(f"Error occurred: {e}")

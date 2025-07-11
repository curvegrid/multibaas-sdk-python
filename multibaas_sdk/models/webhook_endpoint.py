# coding: utf-8

"""
    MultiBaas API

    MultiBaas's REST APIv0.

    The version of the OpenAPI document: 0.0
    Contact: contact@curvegrid.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from multibaas_sdk.models.webhook_events_type import WebhookEventsType
from typing import Optional, Set
from typing_extensions import Self

class WebhookEndpoint(BaseModel):
    """
    WebhookEndpoint
    """ # noqa: E501
    url: StrictStr = Field(description="The URL to send the webhook to.")
    label: Annotated[str, Field(strict=True)] = Field(description="An alias to easily identify and reference the entity in subsequent requests.")
    subscriptions: List[WebhookEventsType] = Field(description="The events to subscribe to.")
    id: StrictInt
    next_attempt: Optional[datetime] = Field(default=None, description="The time the next attempt will be made.", alias="nextAttempt")
    last_attempt: Optional[datetime] = Field(default=None, description="The time the last attempt was made.", alias="lastAttempt")
    failed_calls: StrictInt = Field(description="The number of failed webhook endpoint calls since the last successful call.", alias="failedCalls")
    last_error: Optional[StrictStr] = Field(default=None, description="The last error received from the webhook endpoint.", alias="lastError")
    created_at: datetime = Field(description="The time the webhook was created.", alias="createdAt")
    updated_at: datetime = Field(description="The time the webhook was last updated.", alias="updatedAt")
    secret: StrictStr = Field(description="The secret key used to sign the webhook.")
    __properties: ClassVar[List[str]] = ["url", "label", "subscriptions", "id", "nextAttempt", "lastAttempt", "failedCalls", "lastError", "createdAt", "updatedAt", "secret"]

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z0-9_-]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z0-9_-]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebhookEndpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "label": obj.get("label"),
            "subscriptions": obj.get("subscriptions"),
            "id": obj.get("id"),
            "nextAttempt": obj.get("nextAttempt"),
            "lastAttempt": obj.get("lastAttempt"),
            "failedCalls": obj.get("failedCalls"),
            "lastError": obj.get("lastError"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "secret": obj.get("secret")
        })
        return _obj



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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AuditLog(BaseModel):
    """
    An audit log entry.
    """ # noqa: E501
    action_by_id: StrictInt = Field(description="The ID of the user who performed the action.", alias="actionByID")
    action_on_id: Optional[StrictInt] = Field(default=None, description="The ID of the user who was acted upon.", alias="actionOnID")
    action_by_user_email: StrictStr = Field(description="The email of the user who performed the action.", alias="actionByUserEmail")
    action_on_user_email: Optional[StrictStr] = Field(default=None, description="The email of the user who was acted upon.", alias="actionOnUserEmail")
    type: StrictStr = Field(description="The type of action that was performed.")
    created_at: datetime = Field(description="The time the action was performed.", alias="createdAt")
    activity_data: Dict[str, Any] = Field(description="The data associated with the action.", alias="activityData")
    __properties: ClassVar[List[str]] = ["actionByID", "actionOnID", "actionByUserEmail", "actionOnUserEmail", "type", "createdAt", "activityData"]

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
        """Create an instance of AuditLog from a JSON string"""
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
        """Create an instance of AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionByID": obj.get("actionByID"),
            "actionOnID": obj.get("actionOnID"),
            "actionByUserEmail": obj.get("actionByUserEmail"),
            "actionOnUserEmail": obj.get("actionOnUserEmail"),
            "type": obj.get("type"),
            "createdAt": obj.get("createdAt"),
            "activityData": obj.get("activityData")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from multibaas_sdk.models.contract_abi_error_argument import ContractABIErrorArgument
from typing import Optional, Set
from typing_extensions import Self

class ContractABIError(BaseModel):
    """
    A contract error.
    """ # noqa: E501
    id: Annotated[str, Field(min_length=66, strict=True, max_length=66)] = Field(description="The keccak256 hash as a hex string of 256 bits.")
    name: StrictStr
    signature: StrictStr
    inputs: List[ContractABIErrorArgument] = Field(description="List of contract event's input arguments.")
    notes: Optional[StrictStr] = Field(default=None, description="The developer documentation.")
    description: Optional[StrictStr] = Field(default=None, description="The user documentation.")
    __properties: ClassVar[List[str]] = ["id", "name", "signature", "inputs", "notes", "description"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0x[0-9a-f]{64}|0X[0-9A-F]{64})$", value):
            raise ValueError(r"must validate the regular expression /^(0x[0-9a-f]{64}|0X[0-9A-F]{64})$/")
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
        """Create an instance of ContractABIError from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inputs (list)
        _items = []
        if self.inputs:
            for _item_inputs in self.inputs:
                if _item_inputs:
                    _items.append(_item_inputs.to_dict())
            _dict['inputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractABIError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "signature": obj.get("signature"),
            "inputs": [ContractABIErrorArgument.from_dict(_item) for _item in obj["inputs"]] if obj.get("inputs") is not None else None,
            "notes": obj.get("notes"),
            "description": obj.get("description")
        })
        return _obj



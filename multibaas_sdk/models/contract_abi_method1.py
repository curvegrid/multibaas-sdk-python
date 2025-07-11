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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from multibaas_sdk.models.contract_abi_method_argument import ContractABIMethodArgument
from typing import Optional, Set
from typing_extensions import Self

class ContractABIMethod1(BaseModel):
    """
    A contract function.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A hex string.")
    name: StrictStr = Field(description="Name of the function.")
    signature: StrictStr = Field(description="The function signature.")
    const: StrictBool
    payable: StrictBool
    inputs: List[ContractABIMethodArgument] = Field(description="List of function arguments.")
    outputs: List[ContractABIMethodArgument] = Field(description="List of function outputs.")
    author: StrictStr
    notes: StrictStr
    description: StrictStr = Field(description="The function description.")
    __properties: ClassVar[List[str]] = ["id", "name", "signature", "const", "payable", "inputs", "outputs", "author", "notes", "description"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0x[0-9a-f]*|0X[0-9A-F]*)$", value):
            raise ValueError(r"must validate the regular expression /^(0x[0-9a-f]*|0X[0-9A-F]*)$/")
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
        """Create an instance of ContractABIMethod1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in outputs (list)
        _items = []
        if self.outputs:
            for _item_outputs in self.outputs:
                if _item_outputs:
                    _items.append(_item_outputs.to_dict())
            _dict['outputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractABIMethod1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "signature": obj.get("signature"),
            "const": obj.get("const"),
            "payable": obj.get("payable"),
            "inputs": [ContractABIMethodArgument.from_dict(_item) for _item in obj["inputs"]] if obj.get("inputs") is not None else None,
            "outputs": [ContractABIMethodArgument.from_dict(_item) for _item in obj["outputs"]] if obj.get("outputs") is not None else None,
            "author": obj.get("author"),
            "notes": obj.get("notes"),
            "description": obj.get("description")
        })
        return _obj



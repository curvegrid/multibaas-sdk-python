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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContractABIType(BaseModel):
    """
    A contract function or event argument type.
    """ # noqa: E501
    type: StrictStr
    size: Optional[StrictInt] = None
    tuple_elems: Optional[List[ContractABIType]] = Field(default=None, alias="tupleElems")
    tuple_raw_names: Optional[List[StrictStr]] = Field(default=None, alias="tupleRawNames")
    elem: Optional[ContractABIType] = None
    __properties: ClassVar[List[str]] = ["type", "size", "tupleElems", "tupleRawNames", "elem"]

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
        """Create an instance of ContractABIType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tuple_elems (list)
        _items = []
        if self.tuple_elems:
            for _item_tuple_elems in self.tuple_elems:
                if _item_tuple_elems:
                    _items.append(_item_tuple_elems.to_dict())
            _dict['tupleElems'] = _items
        # override the default output from pydantic by calling `to_dict()` of elem
        if self.elem:
            _dict['elem'] = self.elem.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractABIType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "size": obj.get("size"),
            "tupleElems": [ContractABIType.from_dict(_item) for _item in obj["tupleElems"]] if obj.get("tupleElems") is not None else None,
            "tupleRawNames": obj.get("tupleRawNames"),
            "elem": ContractABIType.from_dict(obj["elem"]) if obj.get("elem") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
ContractABIType.model_rebuild(raise_errors=False)


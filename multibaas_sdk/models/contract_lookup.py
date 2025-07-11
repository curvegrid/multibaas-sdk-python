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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ContractLookup(BaseModel):
    """
    The contract lookup item.
    """ # noqa: E501
    address: Annotated[str, Field(strict=True)] = Field(description="An ethereum address.")
    name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The name of the contract.")
    abi: StrictStr = Field(description="The contract ABI JSON string.")
    bytecode: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The smart-contract bytecode.")
    source: Optional[StrictStr] = Field(default=None, description="The contract's source code.")
    userdoc: Optional[StrictStr] = Field(default=None, description="The user documentation JSON string.")
    devdoc: Optional[StrictStr] = Field(default=None, description="The developer documentation JSON string.")
    verified: StrictBool = Field(description="Indicates whether the contract has been verified.")
    verified_source: Optional[StrictStr] = Field(default=None, description="The name of the service that provided the contract verification.", alias="verifiedSource")
    verified_link: Optional[StrictStr] = Field(default=None, description="The URL to the contract's verification details on the verification service.", alias="verifiedLink")
    proxy: StrictBool = Field(description="Indicates whether the contract is a proxy contract.")
    __properties: ClassVar[List[str]] = ["address", "name", "abi", "bytecode", "source", "userdoc", "devdoc", "verified", "verifiedSource", "verifiedLink", "proxy"]

    @field_validator('address')
    def address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^0[xX][a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0[xX][a-fA-F0-9]{40}$/")
        return value

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^\"#$%&\'\'()*+,\/:;<>?[\\\]^\x60{}~]*$", value):
            raise ValueError(r"must validate the regular expression /^[^\"#$%&''()*+,\/:;<>?[\\\]^\x60{}~]*$/")
        return value

    @field_validator('bytecode')
    def bytecode_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of ContractLookup from a JSON string"""
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
        """Create an instance of ContractLookup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "name": obj.get("name"),
            "abi": obj.get("abi"),
            "bytecode": obj.get("bytecode"),
            "source": obj.get("source"),
            "userdoc": obj.get("userdoc"),
            "devdoc": obj.get("devdoc"),
            "verified": obj.get("verified"),
            "verifiedSource": obj.get("verifiedSource"),
            "verifiedLink": obj.get("verifiedLink"),
            "proxy": obj.get("proxy")
        })
        return _obj



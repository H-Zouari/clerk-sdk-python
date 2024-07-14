"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ToggleTemplateDeliveryPathParamTemplateType(str, Enum):
    r"""The type of template to toggle delivery for"""
    EMAIL = "email"
    SMS = "sms"

class ToggleTemplateDeliveryRequestBodyTypedDict(TypedDict):
    delivered_by_clerk: NotRequired[Nullable[bool]]
    r"""Whether Clerk should deliver emails or SMS messages based on the current template"""
    

class ToggleTemplateDeliveryRequestBody(BaseModel):
    delivered_by_clerk: OptionalNullable[bool] = UNSET
    r"""Whether Clerk should deliver emails or SMS messages based on the current template"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nullableOptional", "optional"]
        nullable_fields = ["nullableRequired", "nullableOptional"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class ToggleTemplateDeliveryRequestTypedDict(TypedDict):
    template_type: ToggleTemplateDeliveryPathParamTemplateType
    r"""The type of template to toggle delivery for"""
    slug: str
    r"""The slug of the template for which to toggle delivery"""
    request_body: NotRequired[ToggleTemplateDeliveryRequestBodyTypedDict]
    

class ToggleTemplateDeliveryRequest(BaseModel):
    template_type: Annotated[ToggleTemplateDeliveryPathParamTemplateType, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The type of template to toggle delivery for"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The slug of the template for which to toggle delivery"""
    request_body: Annotated[Optional[ToggleTemplateDeliveryRequestBody], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from ..types import LabeledPrice
from .base import TelegramMethod


class CreateInvoiceLink(TelegramMethod[str]):
    """
    Use this method to create a link for an invoice. Returns the created invoice link as *String* on success.

    Source: https://core.telegram.org/bots/api#createinvoicelink
    """

    __returning__ = str
    __api_method__ = "createInvoiceLink"

    title: str
    """Product name, 1-32 characters"""
    description: str
    """Product description, 1-255 characters"""
    payload: str
    """Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes."""
    provider_token: str
    """Payment provider token, obtained via `BotFather <https://t.me/botfather>`_"""
    currency: str
    """Three-letter ISO 4217 currency code, see `more on currencies <https://core.telegram.org/bots/payments#supported-currencies>`_"""
    prices: List[LabeledPrice]
    """Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)"""
    max_tip_amount: Optional[int] = None
    """The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of :code:`US$ 1.45` pass :code:`max_tip_amount = 145`. See the *exp* parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0"""
    suggested_tip_amounts: Optional[List[int]] = None
    """A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*."""
    provider_data: Optional[str] = None
    """JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider."""
    photo_url: Optional[str] = None
    """URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service."""
    photo_size: Optional[int] = None
    """Photo size in bytes"""
    photo_width: Optional[int] = None
    """Photo width"""
    photo_height: Optional[int] = None
    """Photo height"""
    need_name: Optional[bool] = None
    """Pass :code:`True` if you require the user's full name to complete the order"""
    need_phone_number: Optional[bool] = None
    """Pass :code:`True` if you require the user's phone number to complete the order"""
    need_email: Optional[bool] = None
    """Pass :code:`True` if you require the user's email address to complete the order"""
    need_shipping_address: Optional[bool] = None
    """Pass :code:`True` if you require the user's shipping address to complete the order"""
    send_phone_number_to_provider: Optional[bool] = None
    """Pass :code:`True` if the user's phone number should be sent to the provider"""
    send_email_to_provider: Optional[bool] = None
    """Pass :code:`True` if the user's email address should be sent to the provider"""
    is_flexible: Optional[bool] = None
    """Pass :code:`True` if the final price depends on the shipping method"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            currency: str,
            prices: List[LabeledPrice],
            max_tip_amount: Optional[int] = None,
            suggested_tip_amounts: Optional[List[int]] = None,
            provider_data: Optional[str] = None,
            photo_url: Optional[str] = None,
            photo_size: Optional[int] = None,
            photo_width: Optional[int] = None,
            photo_height: Optional[int] = None,
            need_name: Optional[bool] = None,
            need_phone_number: Optional[bool] = None,
            need_email: Optional[bool] = None,
            need_shipping_address: Optional[bool] = None,
            send_phone_number_to_provider: Optional[bool] = None,
            send_email_to_provider: Optional[bool] = None,
            is_flexible: Optional[bool] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                title=title,
                description=description,
                payload=payload,
                provider_token=provider_token,
                currency=currency,
                prices=prices,
                max_tip_amount=max_tip_amount,
                suggested_tip_amounts=suggested_tip_amounts,
                provider_data=provider_data,
                photo_url=photo_url,
                photo_size=photo_size,
                photo_width=photo_width,
                photo_height=photo_height,
                need_name=need_name,
                need_phone_number=need_phone_number,
                need_email=need_email,
                need_shipping_address=need_shipping_address,
                send_phone_number_to_provider=send_phone_number_to_provider,
                send_email_to_provider=send_email_to_provider,
                is_flexible=is_flexible,
                **__pydantic_kwargs,
            )

from typing import Protocol, TypeAlias, Literal

PayType: TypeAlias = Literal["CASH", "CARD", "PHONE"]

class Payable(Protocol):

    def get_pay_type() -> PayType:
        if PayType not in ["CASH", "CARD", "PHONE"]:
            raise ValueError("Must be either 'CASH', 'CARD', or 'PHONE'.")


    def set_pay_type(payment_method: PayType) -> None:
        if payment_method not in PayType:
            raise ValueError("Must be either 'CASH', 'CARD', or 'PHONE'.")

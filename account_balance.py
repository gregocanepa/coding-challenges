from typing import List
from datetime import datetime


def solution(A: List[int], D: List[datetime]) -> int:
    dict_with_months = {
        month: {"num_expenses": 0, "total_expenses": 0} for month in range(1, 13)
    }
    account_balance = 0
    for transaction, transaction_date in zip(A, D):
        current_month = datetime.strptime(transaction_date, "%Y-%m-%d").month
        if transaction < 0:
            # it's a card payment
            account_balance -= abs(transaction)
            month_expenses_dict = dict_with_months[current_month]
            month_expenses_dict["num_expenses"] += 1
            month_expenses_dict["total_expenses"] += abs(transaction)
        else:
            account_balance += transaction
    card_fee_months = 12
    for month_dict in dict_with_months.values():
        if get_card_discount(month_dict):
            card_fee_months -= 1
    card_fees = card_fee_months * 5
    return account_balance - card_fees


def get_card_discount(month_dict: dict) -> bool:
    return (month_dict["num_expenses"] >= 3) & (month_dict["total_expenses"] >= 100)

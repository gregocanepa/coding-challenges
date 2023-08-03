from typing import List
from datetime import datetime

"""
Exercise: CardPayments
Total score: 100
Correctness: 100
Performance: N/A

(+) Solution is functionally correct
(+) Solution is simple to understand and variable names are meaningful,
data structures are clear and intuitive

(-) Some of the functionality was extracted to a separate method
so this is a good sign, but the main method is still very long and detailed.
More work could be done here.

"""
A = [23, 100, 80, -70, -30, -20]
D = ["2023-02-01", "2023-02-03", "2023-04-01", "2023-05-01", "2023-05-04", "2023-05-05"]


def init_months_dict() -> dict():
    return {month: {"num_expenses": 0, "total_expenses": 0} for month in range(1, 13)}


def get_month(transaction_date: str) -> int:
    return datetime.strptime(transaction_date, "%Y-%m-%d").month


def is_expense(transaction: int) -> bool:
    return transaction < 0


def add_expense(transaction: int, month_dict: dict) -> None:
    month_dict["num_expenses"] += 1
    month_dict["total_expenses"] += abs(transaction)


def get_card_discount(month_dict: dict) -> bool:
    return (month_dict["num_expenses"] >= 3) & (month_dict["total_expenses"] >= 100)


def calculate_card_fee(months_dict: dict) -> int:
    card_fee_months = 12
    for month_dict in months_dict.values():
        if get_card_discount(month_dict):
            card_fee_months -= 1
    return card_fee_months * 5


def process_card_fee(
    transaction: int, transaction_date: str, months_dict: dict
) -> None:
    if is_expense(transaction):
        month_expenses_dict = months_dict[get_month(transaction_date)]
        add_expense(transaction, month_expenses_dict)


def generate_balance(transactions: List[int], transactions_dates: List[str]) -> int:
    balance = 0
    months_dict = init_months_dict()
    for transaction, transaction_date in zip(transactions, transactions_dates):
        balance += transaction
        process_card_fee(transaction, transaction_date, months_dict)
    card_fee = calculate_card_fee(months_dict)
    return balance - card_fee


def solution(A: List[int], D: List[str]) -> int:
    return generate_balance(A, D)


if __name__ == "__main__":
    print(solution(A, D) == (203 - 120 - 55))
    print(solution(A=A, D=D))

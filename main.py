import sys
from typing import List

import app

from app.transaction import Transaction
from app.transaction_provider import TransactionProvider
from app.transfer import TransferProvider


def help():
    print(
        """tax_stocks: computes the profits (and losses) for stocks transactions and dividends for particular fiscal year.
Example: python main.py 2021"""
    )


def main():
    # try:
    #     year = int(sys.argv[1])
    # except (IndexError, ValueError):
    #     help()
    #     return
    year = 2022
    revolut = app.Revolut()

    # === Stocks ===

    transaction_providers: List[TransactionProvider] = [
        app.Degiro(),
        revolut,
    ]

    transactions: List[Transaction] = []
    for transaction_provider in transaction_providers:
        transactions += transaction_provider.provide_transactions()

    exchange = app.ExchangeNBP()

    account = app.Account(exchange)
    account.do_transactions(transactions, year=year)

    account.print_stocks(show_summary_per_stock=True, year=year)
    account.print_dividends(year=year)

    # # Debug current positions (validate with your portfolio):
    # account.print_current_positions()

    # Print out all taxable transactions (sells) with buy information.
    # This should contain everything you need to evaluate the tax.
    # account.print_stocks_transactions()

    # === Crypto ===

    transfer_providers: List[TransferProvider] = [
        revolut,
        app.Binance(),
    ]
    transfers = []
    for transfer_provider in transfer_providers:  # type: ignore[assignment]
        transfers += transfer_provider.provide_transfers()

    crypto = app.Crypto(transfers, exchange)
    crypto.print_summary(year=year)


if __name__ == "__main__":
    main()

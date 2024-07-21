"""Напишите программу банкомат. Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

import decimal

CMD_REPLENISH = 'r'
CMD_WITHDRAW = 'w'
CMD_EXIT = 'e'
MULTIPLICITY = 50
PERCENT_4_WITHDRAW = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_FEE = 30
MAX_FEE = 600
COUNT_OPERATION = 3
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
LUXURY_TAX = decimal.Decimal(10) / decimal.Decimal(100)
LUXURY_LIMIT = decimal.Decimal(5_000_000)

balance = decimal.Decimal(0)
count = 0
while True:
    cmd = input(
        f'Enter command ('
        f'{CMD_REPLENISH} = replenish, '
        f'{CMD_WITHDRAW} = withdraw, '
        f'{CMD_EXIT} = exit'
        f'): \n'
    )

    if cmd == CMD_EXIT:
        print(f'Your final balance is {balance}. Bye-bye!')
        break
    if balance > LUXURY_LIMIT:
        tax_amount = balance * LUXURY_TAX
        balance = balance - tax_amount
        print(f'Luxury tax amount taken as {tax_amount}. '
              f'Your current balance is {balance}')
    if cmd in (CMD_REPLENISH, CMD_WITHDRAW):
        amount = decimal.Decimal(input(f'Enter amount multiple {MULTIPLICITY}: \n'))
        while amount % MULTIPLICITY != 0:
            amount = decimal.Decimal(input(f'Enter amount multiple {MULTIPLICITY}: \n'))
        if cmd == CMD_WITHDRAW:
            withdrawal_fee = amount * PERCENT_4_WITHDRAW
            withdrawal_fee = MIN_FEE if withdrawal_fee < MIN_FEE else \
                MAX_FEE if withdrawal_fee > MAX_FEE else withdrawal_fee
            withdrawal_amount = amount + withdrawal_fee
            if balance > withdrawal_amount:
                balance = balance - withdrawal_amount
                print(
                    f'Transaction amount {amount}, '
                    f'Withdrawal amount {withdrawal_amount} '
                    f'including withdrawal fee {withdrawal_fee} '
                    f'Balance after withdraw {balance}')

                count += 1
            else:
                print(f'Insufficient money. Withdrawal amount{withdrawal_amount}. Balance {balance}')
        elif cmd == CMD_REPLENISH:
            balance += amount
            print(f'Your balance after replenishment is {balance}')
            count += 1

        if count % COUNT_OPERATION == 0:
            bonus = balance * PERCENT_DEPOSIT
            balance = balance + bonus
            print(f'This is your 3rd operation. You\'ve got bonus {bonus}. '
                  f'Total balance {balance}')

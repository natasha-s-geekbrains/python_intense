import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False


def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной 50 у.е.')


def withdraw(amount):
    global bank_account
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной 50 у.е.')
    withdrawal_fee = int(amount * PERCENT_REMOVAL)
    if withdrawal_fee < MIN_REMOVAL:
        withdrawal_fee = MIN_REMOVAL
    elif withdrawal_fee > MAX_REMOVAL:
        withdrawal_fee = MAX_REMOVAL

    withdrawal_amount = int(amount + withdrawal_fee)
    if bank_account >= withdrawal_amount:
        bank_account -= withdrawal_amount
        operations.append(
            f'Снятие с карты {amount} у.е. Процент за снятие {withdrawal_fee} у.е.. Итого {bank_account} у.е.'
        )
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {withdrawal_amount} у.е. На карте {bank_account} у.е.'
        )


def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        wealth_tax = round(bank_account * RICHNESS_PERCENT, 4)
        bank_account -= wealth_tax
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {wealth_tax} у.е. Итого {bank_account} у.е.'
        )

    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

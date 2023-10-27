import json
import random
import os


class BankAccount:

    def __init__(self, card_holder: str, money=0.0, card_number=None,
                 account_number=None):
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.account_number: str = self.get_random_digits(
            20) if account_number is None else account_number
        self.card_number: str = self.get_random_digits(
            16) if card_number is None else card_number

    @staticmethod
    def get_random_digits(count):
        random_digits = [str(random.randint(0, 9)) for _ in range(count)]
        return ''.join(random_digits)


def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    return {
        "card_holder": bank_account.card_holder,
        "money": bank_account.money,
        "account_number": bank_account.account_number,
        "card_number": bank_account.card_number
    }


def save_accounts(bank_account: dict[str, BankAccount], file_name: str):
    data = {number: convert_bank_account_to_dict(account)
            for number, account in bank_account.items()}
    with open(file_name, "w") as file:
        json.dump(data, file, indent=2)


def load_accounts(file_name) -> dict[str, BankAccount]:
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return {number: BankAccount(**data) for number, data in
                json.load(file).items()}


class Bank:
    def __init__(self, bank_accounts=None):
        self.bank_accounts: dict[str, BankAccount] = bank_accounts or {}

    def open_account(self, card_holder):
        new_account = BankAccount(card_holder)
        self.bank_accounts[new_account.account_number] = new_account
        return new_account

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    # bank = Bank()
    # ivan_account = bank.open_account('Ivan ivanov')
    # petr_account = bank.open_account('Petr petr')
    # for _, account in bank.bank_accounts.items():
    #     assert account.money == 0
    #
    # bank.add_money(ivan_account.account_number, 100)
    # bank.add_money(petr_account.account_number, 200)
    # assert ivan_account.money == 100
    # assert petr_account.money == 200

    def transfer_money(self, from_account_number, to_account_number, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_number].money += money

        print(f"Банк успешно перевел {money} с вашего счета "
              f"{from_account_number} на счет "
              f"получатея {to_account_number}")

    def external_transfer(self, from_account_number, to_external_number,
                          money):
        self.bank_accounts[from_account_number].money -= money

        print(
            f"Банк перевёл {money} с вашего счёта {from_account_number} на внешний счёт "
            f"{to_external_number}")


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print("Здравствуйте, наш банк открылся!")
        while True:
            print("Выберите действие:")
            print("0. Завершить программу")
            print("1. Открыть новый счёт")
            print("2. Просмотреть открытые счета")
            print("3. Положить деньги на счёт")
            print("4. Перевести деньги между счетами")
            print("5. Совершить платёж")

            input_number = int(input())
            if input_number == 0:
                save_accounts(self.bank.bank_accounts, self.data_file_name)
                print("До свидания!")
                break
            elif input_number == 1:
                input_name_surname = input("Введите, пожалуйста, "
                                           "Имя и Фамилию держателя карты")
                count = self.bank.open_account(card_holder=input_name_surname)
                print(f"Счёт {count.account_number} создан")

            elif input_number == 2:
                print('Все открытые счета: ')
                for account in self.bank.bank_accounts.values():
                    print(f"Номер счета: {account.account_number}")
                    print(f"Остаток на счету: {account.money}")
                    print(f"Номер карты: {account.card_number}")
                    print(f"Держатель карты: {account.card_holder}")

            elif input_number == 3:
                input_account_number = input("Пожалуйста, введите свой "
                                             "номер счета: ")
                input_money = float(input("Пожалуйста, введите сумму, "
                                          "на которую можно пополнить ваш "
                                          "номер счета: "))
                self.bank.add_money(account_number=input_account_number,
                                    money=input_money)
                print(f"На ваш счет зачислена сумма в {input_money}")

            elif input_number == 4:
                input_from_account_number = input("Пожалуйста, введите "
                                                  "номер счета отправителя: ")
                input_to_account_number = input("Пожалуйста, "
                                                "введите "
                                                "номер счета получателся: ")
                input_money = float(input("Введите количества денег для "
                                          "перевода: "))

                self.bank.transfer_money(input_from_account_number,
                                         input_to_account_number, input_money)

            elif input_number == 5:
                to_external_number = ''.join(
                    [str(random.randint(0, 9)) for _ in range(20)])
                input_from_account_number = input("Введите номер "
                                                  "счёта-отправителя: ")
                print(
                    f"Введите номер внешнего получателя: {to_external_number}")

                input_money = float(input("Введите количества денег для "
                                          "перевода"))

                self.bank.external_transfer(
                    from_account_number=input_from_account_number,
                    to_external_number=to_external_number, money=input_money)

            else:
                print("Вы ввели не существующую команду")


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()

import random


class BankAccount:

    def __init__(self, card_holder: str):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = self.get_random_digits(20)
        self.card_number = self.get_random_digits(16)

    @staticmethod
    def get_random_digits(count):
        random_digits = [str(random.randint(0, 9)) for _ in range(count)]
        return ''.join(random_digits)


ba = BankAccount("dasha")
print(ba.__dict__)


class Bank:
    def __init__(self):
        self.bank_accounts: dict[str, BankAccount] = dict()

    def open_account(self, card_holder):
        new_account = BankAccount(card_holder)
        self.bank_accounts[card_holder] = new_account
        return new_account.account_number

    def add_money(self, account_number, money):
        for account_number in self.bank_accounts:
            self.bank_accounts[account_number].money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        from_account_number = self.bank_accounts[from_account_number]
        to_account_number = self.bank_accounts[to_account_number]

        from_account_number -= money
        to_account_number += money

    def external_transfer(self, from_account_number, to_external_number,
                          money):
        from_account_number = self.bank_accounts[from_account_number]
        from_account_number -= money
        to_external_number += money
        print(f"Банк перевёл {money} с вашего счёта {from_account_number} на внешний счёт "
              f"{to_external_number}")

class Controller:
    def __init__(self):
        self.bank = Bank()

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
                print("До свидания!")
                break
            if input_number == 1:
                input_name_surname = input("Введите, пожалуйста, "
                                           "Имя и Фамилию держателя карты")
                count = self.bank.open_account(card_holder=input_name_surname)

                print(f"Счёт {count} создан")

            if input_number == 2:
                open_account = self.bank.bank_accounts
                for key, value in open_account.items():
                    print(f"ФИО: {key} \n" 
                          f"Номер аккаунта: {value.account_number}")







if __name__ == '__main__':
    controller = Controller()
    controller.run()
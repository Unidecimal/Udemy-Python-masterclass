import datetime
import pytz


class Accounts:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)
        if balance > 0:
            self._transaction_list.append((Accounts._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance.")
            self.show_balance()

    def show_balance(self):
        print("The balance is: {0._balance}".format(self))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':

    tim = Accounts("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(100)
    tim.withdraw(2000)
    # tim.__balance = 10
    tim.show_balance()
    tim.show_transactions()

    steph = Accounts("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
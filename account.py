class Account:
    def __init__(self, name: str) -> None:
        # Default values for account name and balance
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Increment the account balance by specified amount
        :param amount: Deposit amount (must be more than $0)
        :return: True for successful transaction, otherwise False
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Decrease the account balance by specified amount
        :param amount: Withdrawal amount (must be more than $0 but less than account balance)
        :return: True for successful transaction, otherwise False
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get account balance
        :return: Current account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get name on account
        :return: Name on account
        """
        return self.__account_name

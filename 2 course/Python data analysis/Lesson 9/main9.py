class BankAccount:

    def __init__(self, account_id: str, owner: str, initial_balance: float | int = 0.0) -> None:
        self.account_id: str = account_id
        self.owner: str = owner
        self._history: list[float] = []
        self._balance: float = 0.0
        self.balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float | int) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Баланс має бути числом")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self._balance = float(value)

    def deposit(self, amount: float | int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за 0")
        value = float(amount)
        self._balance += value
        self._history.append(value)

    def withdraw(self, amount: float | int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        value = float(amount)
        self._balance -= value
        self._history.append(-value)

    def __str__(self) -> str:
        return f"Рахунок [{self.account_id}] | Власник: {self.owner} | Баланс: {self.balance:.2f} грн."

    def __len__(self) -> int:
        return len(self._history)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            return False
        return self.account_id == other.account_id


if __name__ == "__main__":
    acc1 = BankAccount("UA1001", "Мирослава", 1000)
    acc2 = BankAccount("UA1001", "Мирослава")
    acc3 = BankAccount("UA1002", "Олег", 500)

    acc1.deposit(100)
    acc1.withdraw(200)

    print(acc1)
    print("Історія:", acc1._history)
    print("Кількість операцій:", len(acc1))
    print("acc1 == acc2:", acc1 == acc2)
    print("acc1 == acc3:", acc1 == acc3)

    for action in [
        lambda: BankAccount("UA1003", "Тест", -100),
        lambda: setattr(acc1, "balance", "не число"),
        lambda: acc1.deposit(-50),
        lambda: acc1.withdraw(10000),
    ]:
        try:
            action()
        except ValueError as error:
            print("Помилка:", error)
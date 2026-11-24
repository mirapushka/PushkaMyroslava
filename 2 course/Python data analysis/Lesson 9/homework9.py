class OrderItem:

    def __init__(self, title: str, price: float, quantity: int) -> None:
        self.title: str = title
        self.price: float = price
        self.quantity: int = quantity

    def get_cost(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"Товар: {self.title} | {self.quantity} шт. x {self.price:.0f} грн"


class ShoppingCart:

    def __init__(self, customer_name: str) -> None:
        self.customer_name: str = customer_name
        self._items: list[OrderItem] = []

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)

    def get_total_sum(self) -> float:
        total = 0.0
        for item in self._items:
            total += item.get_cost()
        return total


if __name__ == "__main__":
    cart = ShoppingCart("Мирослава")

    item1 = OrderItem("Мишка", 450.0, 2)
    item2 = OrderItem("Клавіатура", 1200.0, 1)

    cart.add_item(item1)
    cart.add_item(item2)

    print("Кількість товарів у корзині:", len(cart))
    print(f"Чек для клієнта: {cart.customer_name}")
    for item in cart._items:
        print(f"{item} = {item.get_cost():.2f} грн")
    print(f"Разом до сплати: {cart.get_total_sum():.2f} грн")
//13. Банківський рахунок
//У класі Account зробіть метод withdraw(double amount). 
//Якщо сума > баланс — виняток std::runtime_error
#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

class Account {
private:
    string owner_pushka;
    double balance_pushka;

public:
    Account(string owner, double balance) {
        owner_pushka = owner;
        balance_pushka = balance;
    }

    void withdraw(double amount) {
        if (amount > balance_pushka) {
            throw runtime_error("Недостатньо коштів на рахунку!");
        }
        balance_pushka = balance_pushka - amount;
    }

    double getBalance() {
        return balance_pushka;
    }
};

int main() {
    Account acc_pushka("Пушка", 1000.0);
    double sum_pushka;

    cout << "Баланс: " << acc_pushka.getBalance() << endl;
    cout << "Введіть суму: ";
    cin >> sum_pushka;

    try {
        acc_pushka.withdraw(sum_pushka);
        cout << "Знято! Новий баланс: " << acc_pushka.getBalance() << endl;
    }
    catch (runtime_error& e) {
        cout << "Помилка: " << e.what() << endl;
    }

    cout << "Кінець програми." << endl;
    return 0;
}
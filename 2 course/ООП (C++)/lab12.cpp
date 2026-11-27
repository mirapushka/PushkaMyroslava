#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

class Account {
private:
    string owner_ivanenko;
    double balance_ivanenko;

public:
    Account(string owner, double balance) {
        owner_ivanenko = owner;
        balance_ivanenko = balance;
    }

    void withdraw(double amount) {
        if (amount > balance_ivanenko) {
            throw runtime_error("Недостатньо коштів на рахунку!");
        }
        balance_ivanenko = balance_ivanenko - amount;
    }

    double getBalance() {
        return balance_ivanenko;
    }
};

int main() {
    Account acc_ivanenko("Іваненко", 1000.0);
    double sum_ivanenko;

    cout << "Баланс: " << acc_ivanenko.getBalance() << endl;
    cout << "Введіть суму: ";
    cin >> sum_ivanenko;

    try {
        acc_ivanenko.withdraw(sum_ivanenko);
        cout << "Знято! Новий баланс: " << acc_ivanenko.getBalance() << endl;
    }
    catch (runtime_error& e) {
        cout << "Помилка: " << e.what() << endl;
    }

    cout << "Кінець програми." << endl;
    return 0;
}
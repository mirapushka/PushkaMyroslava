#include <iostream>
#include <string>

using namespace std;

struct Date {
    int month;
    int year;
};

class CD {
private:
    string Name;
    Date recordDate;
    string Theme;
    double SIZE;

public:
    CD() {
        Name = "NoName";
        recordDate.month = 1;
        recordDate.year = 2026;
        Theme = "None";
        SIZE = 0;
        cout << "Створено об'єкт (конструктор за замовчуванням)" << endl;
    }

    CD(string n, int m, int y, string t, double s) {
        Name = n;
        recordDate.month = m;
        recordDate.year = y;
        Theme = t;
        SIZE = s;
        cout << "Створено об'єкт (конструктор з параметрами)" << endl;
    }

    ~CD() {
        cout << "Об'єкт видалено (деструктор)" << endl;
    }

    string getName() { return Name; }
    int getMonth() { return recordDate.month; }
    int getYear() { return recordDate.year; }
    string getTheme() { return Theme; }
    double getSize() { return SIZE; }

    void setName(string n) { Name = n; }
    void setDate(int m, int y) { recordDate.month = m; recordDate.year = y; }
    void setTheme(string t) { Theme = t; }
    void setSize(double s) { SIZE = s; }

    void input() {
        cout << "Введіть назву диска: ";
        cin >> Name;
        cout << "Введіть місяць і рік: ";
        cin >> recordDate.month >> recordDate.year;
        cout << "Введіть тему: ";
        cin >> Theme;
        cout << "Введіть розмір: ";
        cin >> SIZE;
    }

    void print() {
        cout << "Назва: " << Name << endl;
        cout << "Дата: " << recordDate.month << "." << recordDate.year << endl;
        cout << "Тема: " << Theme << endl;
        cout << "Розмір: " << SIZE << endl;
    }
};

int main() {
    CD fname_cd("Music", 5, 2026, "Rock", 700);
    fname_cd.print();

    cout << " Введення нових даних " << endl;
    fname_cd.input();

    cout << " Нові дані " << endl;
    fname_cd.print();

    fname_cd.setSize(650);
    cout << "Розмір через геттер: " << fname_cd.getSize() << endl;

    return 0;
}
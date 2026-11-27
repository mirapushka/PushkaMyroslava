#include "student.h"
#include <iostream>

using namespace std;

CD::CD() {
    Name = "NoName";
    recordDate.month = 1;
    recordDate.year = 2026;
    Theme = "None";
    SIZE = 0;
}

CD::CD(string n, int m, int y, string t, double s) {
    Name = n;
    recordDate.month = m;
    recordDate.year = y;
    Theme = t;
    SIZE = s;
}

CD::~CD() {
    cout << "Видалено об'єкт: " << Name << endl;
}

string CD::getName() { return Name; }
int CD::getMonth() { return recordDate.month; }
int CD::getYear() { return recordDate.year; }
string CD::getTheme() { return Theme; }
double CD::getSize() { return SIZE; }

void CD::setName(string n) { Name = n; }
void CD::setDate(int m, int y) {
    recordDate.month = m;
    recordDate.year = y;
}
void CD::setTheme(string t) { Theme = t; }
void CD::setSize(double s) { SIZE = s; }

void CD::input() {
    cout << "Назва диска (без пробілів): ";
    cin >> Name;
    cout << "Місяць і рік: ";
    cin >> recordDate.month >> recordDate.year;
    cout << "Тема: ";
    cin >> Theme;
    cout << "Розмір: ";
    cin >> SIZE;
}

void CD::print() {
    cout << "Назва: " << Name << endl;
    cout << "Дата: " << recordDate.month << "." << recordDate.year << endl;
    cout << "Тема: " << Theme << endl;
    cout << "Розмір: " << SIZE << endl;
}

void CD::saveToFile(const string& filename) {
    ofstream out(filename);
    if (out.is_open()) {
        out << Name << endl;
        out << recordDate.month << " " << recordDate.year << endl;
        out << Theme << endl;
        out << SIZE << endl;
        out.close();
    } else {
        cout << "Помилка відкриття файлу для запису!" << endl;
    }
}

void CD::loadFromFile(const string& filename) {
    ifstream in(filename);
    if (in.is_open()) {
        in >> Name;
        in >> recordDate.month >> recordDate.year;
        in >> Theme;
        in >> SIZE;
        in.close();
    } else {
        cout << "Помилка відкриття файлу для читання!" << endl;
    }
}
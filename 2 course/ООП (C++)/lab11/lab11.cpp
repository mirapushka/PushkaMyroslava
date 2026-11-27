#include <iostream>
#include "student.h"

using namespace std;

int main() {
    CD cd1;
    cd1.input();
    cd1.saveToFile("cd_data.txt");

    CD cd2;
    cd2.loadFromFile("cd_data.txt");

    cout << "\nЗчитані дані з файлу:" << endl;
    cd2.print();

    return 0;
}
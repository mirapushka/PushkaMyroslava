//Варіант 13.
//1. Описати структуру з ім‘ям COMPUTER, яка містить наступні поля:
//- Procesor – процесор комп‘ютера;
// - Ram – обсяг оперативної пам‘яті;
//- HDD – структура що містить поля (Namt- виробник, V_Ram - обсяг, V- швидкість обертання диску);
//- Monitor – ставка з урахуванням на 24 робочих дні;
//- Keyboard – нараховано заробітної плати з урахуванням ставки і кількості відпрацьованих днів;
//- Mouse – сума виплати заробітної плати працівнику з вирахуванням 20% податку.
//2. Написати програму, що використовує дану структуру і виконує наступні дії:
//вводить з клавіатури масив даних CLASS, що складається з N змінних типу COMPUTER;
//- Впорядковує записи по зростанню поля V_ram;
//- Виводить на екран всіх комп‘ютери за введеним процесором..

#include <iostream> 
#include <fstream> 
#include <string> 

using namespace std; 

string surname = "Пушка"; 

struct HDD { 
    string Namt; 
    int V_Ram; 
    int V; 
}; 

struct COMPUTER { 
    string Procesor; 
    int Ram; 
    HDD hdd; 
    double Monitor; 
    double Keyboard; 
    double Mouse; 
}; 

int main() { 
    int n; 
    string fileName = "Pushka_lab09.txt"; 

    cout << "Студент: " << surname << endl; 
    cout << "Введіть кількість комп'ютерів: "; 
    cin >> n;

    COMPUTER a[50]; 

    for (int i = 0; i < n; i++) { 
        int days; 
        cout << "\nКомп'ютер " << i + 1 << endl; 
        cout << "Procesor: "; 
        cin >> a[i].Procesor; 
        cout << "Ram: "; 
        cin >> a[i].Ram; 
        cout << "HDD Namt: "; 
        cin >> a[i].hdd.Namt; 
        cout << "HDD V_Ram: "; 
        cin >> a[i].hdd.V_Ram; 
        cout << "HDD V: "; 
        cin >> a[i].hdd.V; 
        cout << "Monitor (ставка за 24 дні): "; 
        cin >> a[i].Monitor;
        cout << "Відпрацьовано днів: ";
        cin >> days; 

        a[i].Keyboard = (a[i].Monitor / 24.0) * days;
        a[i].Mouse = a[i].Keyboard * 0.8;
    } 

    for (int i = 0; i < n - 1; i++) { 
        for (int j = 0; j < n - i - 1; j++) { 
            if (a[j].hdd.V_Ram > a[j + 1].hdd.V_Ram) { 
                COMPUTER temp = a[j]; 
                a[j] = a[j + 1]; 
                a[j + 1] = temp; 
            } 
        } 
    } 

    ofstream fout(fileName); 
    if (!fout.is_open()) { 
        cout << "Помилка відкриття файлу!" << endl; 
        return 1;
    } 

    fout << surname << " " << n << endl; 
    for (int i = 0; i < n; i++) { 
        fout << a[i].Procesor << " " << a[i].Ram << " " 
             << a[i].hdd.Namt << " " << a[i].hdd.V_Ram << " " << a[i].hdd.V << " "
             << a[i].Monitor << " " << a[i].Keyboard << " " << a[i].Mouse << endl;
    } 
    fout.flush(); 
    fout.close(); 

    ifstream fin(fileName); 
    string fSurname; 
    int fN; 
    fin >> fSurname >> fN; 

    COMPUTER b[50]; 
    for (int i = 0; i < fN; i++) { 
        fin >> b[i].Procesor >> b[i].Ram >> b[i].hdd.Namt >> b[i].hdd.V_Ram >> b[i].hdd.V 
            >> b[i].Monitor >> b[i].Keyboard >> b[i].Mouse; 
    } 
    fin.close(); 

    string proc; 
    cout << "\nВведіть процесор для пошуку: "; 
    cin >> proc; 

    cout << "\nРезультат (" << fSurname << "):" << endl; 
    for (int i = 0; i < fN; i++) { 
        if (b[i].Procesor == proc) { 
            cout << "Procesor: " << b[i].Procesor 
                 << ", V_Ram: " << b[i].hdd.V_Ram 
                 << ", Mouse: " << b[i].Mouse << endl; 
        } 
    } 
    return 0; 
} 
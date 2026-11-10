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
#include <string> 
using namespace std; 

string FNAME = "Пушка"; 
struct HardDrive { // структура для жорсткого диска
    string Namt; // виробник 
    int V_Ram; // обсяг 
    int V; // швидкість обертання 
};

struct COMPUTER { 
    string Procesor; // процесор комп’ютера
    int Ram; // обсяг оп
    HardDrive HDD; // структура жорсткого диска
    double Monitor; // ставка на 24 робочі дні
    double Keyboard; // зп
    double Mouse; // сума виплати з 20% податку
};

int main() { 
    int N = 0; // ініціалізація змінної кількості елементів
    cout << "Введіть кількість комп'ютерів: "; 
    cin >> N; 

    COMPUTER *CLASS = new COMPUTER[N]; // динамічний масив структур CLASS

    for (int i = 0; i < N; ++i) { // введення даних комп'ютера
        cout << "\nкомп'ютер #" << i + 1 << endl; 
        cout << "процесор: "; 
        cin >> CLASS[i].Procesor; 
        cout << "Ram: "; 
        cin >> CLASS[i].Ram; 
        cout << "HDD Namt (виробник): "; 
        cin >> CLASS[i].HDD.Namt; 
        cout << "HDD V_Ram (обсяг): "; 
        cin >> CLASS[i].HDD.V_Ram; 
        cout << "HDD V (швидкість): "; 
        cin >> CLASS[i].HDD.V; 
        cout << "Monitor (ставка): "; 
        cin >> CLASS[i].Monitor; 
        
        CLASS[i].Keyboard = CLASS[i].Monitor * 24; // розрахунок зп
        CLASS[i].Mouse = CLASS[i].Keyboard * 0.8; // виплата з 20% податку
    }

    for (int i = 0; i < N - 1; ++i) { // зовнішній цикл проходів
        for (int j = 0; j < N - i - 1; ++j) { // цикл порівняння сусідніх елементів
            if (CLASS[j].HDD.V_Ram > CLASS[j + 1].HDD.V_Ram) { // якщо попередній більший за наступний
                COMPUTER temp = CLASS[j]; // тимчасова змінна для збереження структури
                CLASS[j] = CLASS[j + 1]; // міняємо місцями
                CLASS[j + 1] = temp; 
            }
        }
    }

    cout << "\n Впорядкований список за V_ram " << endl; 
    for (int i = 0; i < N; ++i) { // виведення відсортованого масиву
        cout << i + 1 << ". Процесор: " << CLASS[i].Procesor << ", V_ram HDD: " << CLASS[i].HDD.V_Ram << endl; // виведення даних
    }

    string searchProc; //пошук процесора
    cout << "\nВведіть процесор для пошуку: ";
    cin >> searchProc;

    cout << "\n Результати пошуку " << endl; 
    bool found = false; // прапорець знаходження
    for (int i = 0; i < N; ++i) { // цикл пошуку за процесором
        if (CLASS[i].Procesor == searchProc) { // перевірка збігу процесора
            cout << "Знайдено. Процесор: " << CLASS[i].Procesor << ", Mouse (виплата): " << CLASS[i].Mouse << endl; 
            found = true; // встановлення прапорця
        }
    }
    if (!found) { // якщо нічого не знайдено
        cout << "Комп'ютерів з таким процесором не знайдено." << endl; 
    }

    delete[] CLASS; // звільнення динамічної пам'яті
    return 0; 
}
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string FNAME = "Пушка"; 

struct HardDrive {
    string Namt;   
    int V_Ram;     
    int V;        
};

struct COMPUTER {
    string Procesor; 
    int Ram;         
    HardDrive HDD;   
    double Monitor;  
    double Keyboard; 
    double Mouse;    
};


void saveToFile(COMPUTER* arr, int n, const string& filename) {
    ofstream outFile(filename); 
    if (!outFile.is_open()) {
        cout << "Помилка відкриття файлу для запису!\n";
        return;
    }

    outFile << FNAME << "\n";
    outFile << n << "\n";
    for (int i = 0; i < n; ++i) {
        outFile << arr[i].Procesor << " "
                << arr[i].Ram << " "
                << arr[i].HDD.Namt << " "
                << arr[i].HDD.V_Ram << " "
                << arr[i].HDD.V << " "
                << arr[i].Monitor << " "
                << arr[i].Keyboard << " "
                << arr[i].Mouse << "\n";
    }

    outFile.flush(); 
    outFile.close(); 
    cout << "Дані успішно збережено у файл \"" << filename << "\"!\n";
}

void loadFromFile(COMPUTER*& arr, int& n, const string& filename) {
    ifstream inFile(filename); 
    if (!inFile.is_open()) {
        cout << "Помилка відкриття файлу для читання!\n";
        return;
    }

    delete[] arr;

    string savedFName;
    inFile >> savedFName;
    inFile >> n;

    arr = new COMPUTER[n];
    for (int i = 0; i < n; ++i) {
        inFile >> arr[i].Procesor
               >> arr[i].Ram
               >> arr[i].HDD.Namt
               >> arr[i].HDD.V_Ram
               >> arr[i].HDD.V
               >> arr[i].Monitor
               >> arr[i].Keyboard
               >> arr[i].Mouse;
    }

    inFile.close();
    cout << "\nЗчитано дані (автор запису: " << savedFName << ", кількість: " << n << "):\n";
    for (int i = 0; i < n; ++i) {
        cout << i + 1 << ". Процесор: " << arr[i].Procesor
             << ", ОП: " << arr[i].Ram
             << ", HDD: " << arr[i].HDD.Namt << " (" << arr[i].HDD.V_Ram << " ГБ, " << arr[i].HDD.V << " об/хв)"
             << ", ЗП: " << arr[i].Keyboard
             << ", Виплата: " << arr[i].Mouse << "\n";
    }
}

int main() {
    setlocale(LC_ALL, "Ukrainian");

    int N = 0;
    COMPUTER* CLASS = nullptr;
    string filename = "computers.txt";
    int choice = -1;

    do {
        cout << "\n МЕНЮ (Студент: " << FNAME << ") \n";
        cout << "1. Ввести дані комп'ютерів\n";
        cout << "2. Зберегти структуру у текстовий файл\n";
        cout << "3. Зчитати дані з текстового файлу\n";
        cout << "4. Сортувати за V_Ram і знайти за процесором\n";
        cout << "0. Вихід\n";
        cout << "Ваш вибір: ";
        cin >> choice;

        if (choice == 1) {
            delete[] CLASS;
            cout << "Введіть кількість комп'ютерів: ";
            cin >> N;
            CLASS = new COMPUTER[N];

            for (int i = 0; i < N; ++i) {
                cout << "\nКомп'ютер #" << i + 1 << "\n";
                cout << "Процесор: ";
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

                CLASS[i].Keyboard = CLASS[i].Monitor * 24;
                CLASS[i].Mouse = CLASS[i].Keyboard * 0.8;
            }
        } else if (choice == 2) {
            if (N == 0 || CLASS == nullptr) {
                cout << "Спочатку введіть дані (пункт 1) або зчитайте з файлу (пункт 3)!\n";
            } else {
                cout << "Введіть ім'я файлу (наприклад, computers.txt): ";
                cin >> filename;
                saveToFile(CLASS, N, filename);
            }
        } else if (choice == 3) {
            cout << "Введіть ім'я файлу для читання (наприклад, computers.txt): ";
            cin >> filename;
            loadFromFile(CLASS, N, filename);
        } else if (choice == 4) {
            if (N == 0 || CLASS == nullptr) {
                cout << "Немає даних для обробки!\n";
            } else {
                for (int i = 0; i < N - 1; ++i) {
                    for (int j = 0; j < N - i - 1; ++j) {
                        if (CLASS[j].HDD.V_Ram > CLASS[j + 1].HDD.V_Ram) {
                            COMPUTER temp = CLASS[j];
                            CLASS[j] = CLASS[j + 1];
                            CLASS[j + 1] = temp;
                        }
                    }
                }

                cout << "\nВпорядкований список за V_Ram:\n";
                for (int i = 0; i < N; ++i) {
                    cout << i + 1 << ". Процесор: " << CLASS[i].Procesor
                         << ", V_Ram HDD: " << CLASS[i].HDD.V_Ram << "\n";
                }

                string searchProc;
                cout << "\nВведіть процесор для пошуку: ";
                cin >> searchProc;

                bool found = false;
                for (int i = 0; i < N; ++i) {
                    if (CLASS[i].Procesor == searchProc) {
                        cout << "Знайдено. Процесор: " << CLASS[i].Procesor
                             << ", Mouse (виплата): " << CLASS[i].Mouse << "\n";
                        found = true;
                    }
                }
                if (!found) {
                    cout << "Комп'ютерів з таким процесором не знайдено.\n";
                }
            }
        }
    } while (choice != 0);

    delete[] CLASS;
    return 0;
}
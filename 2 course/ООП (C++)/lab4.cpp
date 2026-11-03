//Заданий одномірний масив А(10). Знайти добуток a*2a*3a*…*10a.

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    string FNAME = "Пушка";
    cout << "Студент: " << FNAME << endl;
    
    srand(time(0)); // випадкові числа
    int A[10];      // оголошуємо масив на 10 елементів
    
    // заповнюємо масив випадковими числами
    for (int i = 0; i < 10; i++) {
        A[i] = rand() % 5 + 1;
    }
    
    // виводимо згенерований масив на екран
    cout << "Згенерований масив A: ";
    for (int i = 0; i < 10; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    // обчислюємо добуток елементів масиву
    long long dobutok = 1; // беремо 1, бо це нейтральний елемент для множення
    for (int i = 0; i < 10; i++) {
        dobutok = dobutok * A[i];
    }
    
    cout << "Добуток = " << dobutok << endl;
    
    return 0;
}

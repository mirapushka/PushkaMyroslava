//Дано дійсні числа c1, d1, c2, d2, що задають дійсні і уявні частини комплексних чисел c1+id1, c2+id2. 
// Написати функцію, що знаходить відношення цих двох комплексних чисел і
// повертає значення модуля отриманого комплексного числа, його дійсну частину передає через зовнішню змінну, 
// а його уявну частину і фазу — через параметри-вказівники. 

#include <iostream> 
#include <cmath> 

using namespace std;

double calc(double c1, double d1, double c2, double d2, double* real_part, double* imag_part, double* phase) 
{
    double z = c2 * c2 + d2 * d2; // знаменник
    
    *real_part = (c1 * c2 + d1 * d2) / z; // дійсна частина через вказівник
    *imag_part = (d1 * c2 - c1 * d2) / z; // уявна частина через вказівник
    *phase = atan2(*imag_part, *real_part); // фаза через вказівник
    
    return sqrt((*real_part) * (*real_part) + (*imag_part) * (*imag_part));
}

int main() 
{
    double c1, d1, c2, d2;
    double r_ptr, i_ptr, p_ptr; // змінні для збереження результатів через вказівники
    
    cout << " Введіть c1 i d1: ";
    cin >> c1 >> d1;
    cout << " Введіть c2 i d2: ";
    cin >> c2 >> d2;
    
    // Виклик функції з передачею адрес змінних через оператор &
    double mod = calc(c1, d1, c2, d2, &r_ptr, &i_ptr, &p_ptr);
    
    cout << "\n Результат:" << endl;
    cout << " Модуль = " << mod << endl;
    cout << " Дійсна частина = " << r_ptr << endl;
    cout << " Уявна частина = " << i_ptr << endl;
    cout << " Фаза = " << p_ptr << endl;
    
    return 0;
}
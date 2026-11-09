//Визначити добуток елементів парних стовпців матриці, її розмір вводити з клавіатури. 
//Елементи матриці, а також результат, розмістити в пам’яті динамічно

#include <iostream> 
using namespace std; 

int main() { 
    string FNAME = "Пушка"; 
    int rows, cols; 
    cout << "Введіть кількість рядків матриці: "; 
    cin >> rows; 
    cout << "Введіть кількість стовпців матриці: "; 
    cin >> cols; 

    int **matrix = new int*[rows]; 
    for(int i = 0; i < rows; i++) { 
        matrix[i] = new int[cols]; 
    }

    cout << "Введіть елементи матриці:" << endl;
    for(int i = 0; i < rows; i++) { 
        for(int j = 0; j < cols; j++) { 
            cout << "matrix[" << i << "][" << j << "] = "; 
            cin >> matrix[i][j]; 
        }
    }

    cout << "\nСтудент: " << FNAME << endl; 
    cout << "Введена матриця:" << endl; 
    for(int i = 0; i < rows; i++) { 
        for(int j = 0; j < cols; j++) { 
            cout << matrix[i][j] << "\t"; 
        }
        cout << endl;
    }

    int *result = new int[cols]; 

    cout << "\nРезультати обчислень:" << endl; 
    for(int j = 0; j < cols; j++) { 
        if(j % 2 != 0) { 
            int dob = 1; 
            for(int i = 0; i < rows; i++) { 
                dob = dob * matrix[i][j]; 
            }
            result[j] = dob; 
            cout << "Добуток елементів " << j + 1 << "-го стовпця = " << result[j] << endl; 
        }
    }

    for(int i = 0; i < rows; i++) { 
        delete[] matrix[i]; 
    }
    delete[] matrix; 
    delete[] result; 
    return 0; 
} 

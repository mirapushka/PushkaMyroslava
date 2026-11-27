#ifndef student_h
#define student_h

#include <string>
#include <fstream>

struct Date {
    int month;
    int year;
};

class CD {
private:
    std::string Name;
    Date recordDate;
    std::string Theme;
    double SIZE;

public:
    CD();
    CD(std::string n, int m, int y, std::string t, double s);
    ~CD();

    std::string getName();
    int getMonth();
    int getYear();
    std::string getTheme();
    double getSize();

    void setName(std::string n);
    void setDate(int m, int y);
    void setTheme(std::string t);
    void setSize(double s);

    void input();
    void print();
    void saveToFile(const std::string& filename);
    void loadFromFile(const std::string& filename);
};

#endif
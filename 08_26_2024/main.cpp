#include <iostream>

int main()
{
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;
    if (0 < x && x < 10)
    {
        std::cout << "the number entered is between 0 and 10." << std::endl;
    }
    else
    {
        std::cout << "The number entered is not between 0 and 10." << std::endl;
    }

    return 0;
}
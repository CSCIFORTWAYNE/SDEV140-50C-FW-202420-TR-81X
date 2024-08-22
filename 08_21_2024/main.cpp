#include <iostream>

struct x
{
    int HELLO, GOODBYE;
};

int main()
{
    x y;
    double length = 2 / 7.0 + 2 / 7.0 + 3 / 7.0;
    std::cout << length << std::endl;
    if (length == 1.0)
        std::cout << "Hello World!" << std::endl;
    // std::cout << y << std::endl;
    return 0;
}
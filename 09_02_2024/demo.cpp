#include <iostream>
#include <string>

int main()
{
    std::string filename = "something.txt";
    std::string filenameNoExt;
    bool foundDot = false;
    for (int i = 0; i < filename.length(); i++)
    {
        if (filename[i] != '.' && !foundDot)
        {
            std::cout << filename[i] << std::endl;
            filenameNoExt += filename[i];
        }
        else
        {
            foundDot = true;
        }
    }

    std::cout << filenameNoExt << std::endl;

    return 0;
}
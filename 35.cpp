#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

int main ()
{ 
    std::vector<char> RGB{'G', 'R', 'B', 'R', 'G', 'B', 'G', 'B', 'R', 'B'};

    std::partition(RGB.begin(), RGB.end(), [] (char c) { return c == 'R'; });
    std::partition(RGB.rbegin(), RGB.rend(), [] (char c) { return c == 'B'; });

    for (const auto& channel : RGB) {
        std::cout << channel << " ";
    }
    std::cout << std::endl;

    return 0;
}
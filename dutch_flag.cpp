#include <iostream>
#include <vector>
#include <iterator>

int main()
{
    std::vector nums {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
    const unsigned len = nums.size();
    int z = 0;          // starting position for 0
    int t = len - 1;    //starting position for 2
    
    while (nums[z] == 0) z++;
    while (nums[t] == 2) t--;
    for (int i = z; i <= t; ++i) {
        if (nums[i] == 0) {
            std::swap(nums[i], nums[z++]);            
        }
        else if (nums[i] == 2) {
            std::swap(nums[i], nums[t--]);
            // don't go to the next element
            // maybe the newly swapped needs to be swapped again = maybe it was 0
            i--;
        }
    }

    std::copy(nums.cbegin(), nums.cend(), std::ostream_iterator<int>(std::cout, " "));

    return 0;
}

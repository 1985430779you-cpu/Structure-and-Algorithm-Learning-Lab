#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    auto remove_nums_end = std::remove_if(
        nums.begin(), nums.end(), [] (int n) {
            return n == 4;
        }
    );
    nums.erase(remove_nums_end, nums.end());

    for (int i = 0; i < nums.size(); i++) {
        std::cout << nums[i] << std::endl;
    }
    
    return 0;
}
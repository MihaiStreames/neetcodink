#include <algorithm>
#include <vector>

using std::max;
using std::min;
using std::vector;

class Solution {
public:
    static int maxArea(vector<int>& heights) {
        int left = 0;
		int right = static_cast<int>(heights.size()) - 1;
		int area = 0;

		while (left < right) {
			int w = right - left;
			int h = min(heights[left], heights[right]);
			area = max(area, w * h);

			if (heights[left] < heights[right]) {
				left++;
			} else {
				right--;
			}
		}

		return area;
	}
};

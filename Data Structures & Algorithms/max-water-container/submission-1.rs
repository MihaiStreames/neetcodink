impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let (mut left, mut right) = (0, heights.len() - 1);
        let mut area = 0;

        while left < right {
            let w = (right - left) as i32;
            let h = heights[left].min(heights[right]);
            area = area.max(w * h);

            if heights[left] < heights[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        area
    }
}

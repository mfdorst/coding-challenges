//! https://leetcode.com/problems/search-insert-position/
//!
//! Given a sorted array of distinct integers and a target value, return the index if the target is
//! found. If not, return the index where it would be if it were inserted in order.
//! You must write an algorithm with O(log n) runtime complexity.
//!
//! Example 1:
//! Input: nums = [1,3,5,6], target = 5
//! Output: 2
//!
//! Example 2:
//! Input: nums = [1,3,5,6], target = 2
//! Output: 1
//!
//! Example 3:
//! Input: nums = [1,3,5,6], target = 7
//! Output: 4
//!
//! Constraints:
//! 1 <= nums.length <= 104
//! -10^4 <= nums[i] <= 10^4
//! nums contains distinct values sorted in ascending order.
//! -10^4 <= target <= 10^4

struct Solution;

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        Solution::search_insert_slice(&nums, target)
    }

    fn search_insert_slice(nums: &[i32], target: i32) -> i32 {
        if nums.len() <= 3 {
            Solution::search_insert_short(&nums, target)
        } else {
            let mid = nums.len() / 2;
            if target < nums[mid] {
                Solution::search_insert_slice(&nums[0..mid], target)
            } else {
                mid as i32 + Solution::search_insert_slice(&nums[mid..], target)
            }
        }
    }

    fn search_insert_short(nums: &[i32], target: i32) -> i32 {
        for (i, n) in nums.iter().enumerate() {
            if target <= *n {
                return i as i32;
            }
        }
        nums.len() as i32
    }
}

fn main() {
    let res = Solution::search_insert(vec![1, 3, 5, 6], 5);
    println!("{res}");
}

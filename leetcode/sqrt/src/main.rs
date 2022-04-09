//! https://leetcode.com/problems/sqrtx
//!
//! Given a non-negative integer x, compute and return the square root of x.
//!
//! Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
//!
//! Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
//!
//!  
//!
//! Example 1:
//!
//! Input: x = 4
//! Output: 2
//! Example 2:
//!
//! Input: x = 8
//! Output: 2
//! Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

struct Solution;

impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        for i in 1.. {
            if i as u64 * i as u64 == x as u64 {
                return i;
            } else if i as u64 * i as u64 > x as u64 {
                return i - 1;
            }
        }
        unreachable!();
    }
}

fn main() {
    let root = Solution::my_sqrt(2147483647);
    println!("{root}");
}

//! https://leetcode.com/problems/add-binary/
//!
//! Given two binary strings a and b, return their sum as a binary string.
//!
//! Example 1:
//!
//! Input: a = "11", b = "1"
//! Output: "100"
//! Example 2:
//!
//! Input: a = "1010", b = "1011"
//! Output: "10101"
//!  
//!
//! Constraints:
//!
//! 1 <= a.length, b.length <= 10^4
//! a and b consist only of '0' or '1' characters.
//! Each string does not contain leading zeros except for the zero itself.

struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a: Vec<u8> = a.chars().map(|c| if c == '0' { 0 } else { 1 }).collect();
        let b: Vec<u8> = b.chars().map(|c| if c == '0' { 0 } else { 1 }).collect();
        // Ensure a is at least as long as b. If not, swap them.
        let (a, b) = if a.len() > b.len() { (a, b) } else { (b, a) };
        let mut a_it = a.iter().enumerate().rev();
        let mut b_it = b.iter().rev();
        let mut carry: u8 = 0;
        let mut sum = vec!['0'; a.len()];
        loop {
            if let Some((i, a_bit)) = a_it.next() {
                let b_bit = b_it.next().unwrap_or(&0);

                match a_bit + b_bit + carry {
                    1 => {
                        sum[i] = '1';
                        carry = 0;
                    }
                    2 => carry = 1,

                    3 => {
                        sum[i] = '1';
                        carry = 1;
                    }
                    _ => {}
                }
            } else {
                if carry == 1 {
                    sum.insert(0, '1');
                }
                break sum.iter().collect();
            }
        }
    }
}

fn main() {
    let bin = Solution::add_binary("1010".to_owned(), "10110".to_owned());
    println!("{bin}");
}

//! https://leetcode.com/problems/length-of-last-word
//!
//! Given a string s consisting of words and spaces, return the length of the last word in the
//! string.
//!
//! A word is a maximal substring consisting of non-space characters only.
//!
//! Example 1:
//!
//! Input: s = "Hello World"
//! Output: 5
//! Explanation: The last word is "World" with length 5.
//! Example 2:
//!
//! Input: s = "   fly me   to   the moon  "
//! Output: 4
//! Explanation: The last word is "moon" with length 4.
//! Example 3:
//!
//! Input: s = "luffy is still joyboy"
//! Output: 6
//! Explanation: The last word is "joyboy" with length 6.
//!
//! Constraints:
//!
//! 1 <= s.length <= 10^4
//! s consists of only English letters and spaces ' '.
//! There will be at least one word in s.

struct Solution;

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut len = 1;
        let mut found_chars = false;
        for c in s.chars().rev() {
            if found_chars {
                match c {
                    ' ' => return len,
                    _ => len += 1,
                }
            } else if c != ' ' {
                found_chars = true;
            }
        }
        len
    }
}

fn main() {
    let len = Solution::length_of_last_word("Hello World   ".to_owned());
    println!("{len}");
}

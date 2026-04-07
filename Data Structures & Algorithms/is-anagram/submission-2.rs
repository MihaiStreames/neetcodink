impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = [0; 26];

        for c in s.bytes() {
            count[(c - b'a') as usize] += 1;
        }

        for c in t.bytes() {
            let idx = (c - b'a') as usize;
            count[idx] -= 1;
            
            if count[idx] < 0 {
                return false;
            }
        }

        true
    }
}
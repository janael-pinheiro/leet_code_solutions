use std::collections::HashSet;


pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
    let mut count: i32 = 0;
    let mut allowed_letters: HashSet<char> = vec![].into_iter().collect();
    for letter in allowed.chars() {
        allowed_letters.insert(letter);
    }
    for word in words.iter(){
        let mut unique_letters: HashSet<char> = vec![].into_iter().collect();
        for letter in word.chars(){
            unique_letters.insert(letter);
        }

        let a = unique_letters.difference(&allowed_letters).collect::<Vec<&char>>();
        if a.len() == 0{
            count += 1;
        }
    }
    return count;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_consistent_strings() {
        let words = vec!["ad".to_string(),"bd".to_string(),"aaab".to_string(),"baa".to_string(),"badab".to_string()];
        let result = count_consistent_strings("ab".to_string(), words);
        assert_eq!(result, 2);
    } 
}
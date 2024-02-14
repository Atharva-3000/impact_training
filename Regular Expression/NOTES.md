# REGULAR EXPRESSION

1. If we want to represent a group of strings according to a particular format or pattern then we shold go for regular expressions. 

2. RE is a mechanism to represnt a group of strings according to a particular format or pattern. 

# Ex:1 
We cant write a RE to represent mobile number. 

# Ex:2 
we can write a RE to represent all mail ids. 

The main important application areas of RE are: 
1. To develop validation frameworks or validation logic. 
2. To develop pattern matching application ex - ctrl f in windows and grep in linux. 
3. To develop transaltors like compilers and interpreters etc. To develop digital circuits. 
4. To develop comm protocols like tcp and udp.
5. To develop apps we can ... by using python module RE. 
## This module contains several inbuilt functions to se regular expressions very easily in our app. 

1. `compile()`- RE module contains compile fn to compile  pattern into regex obj.
2. `finditer()` - returns iterator obj which is match object for every match.

## On match object we can call the following methods:
1. `match()`: 
    1. We can use this function to check the given pattern at beginning of target string.
    2. If the match is available, then we will get match object, otherwise we will get `None`.

2. `fullMatch()`:
    1. We can use this method or function to match a pattern to all of target string, i.e. complete string should be matched according to the given pattern.
    2. If the complete string is matched, then this function will return th ematch object, otherwise it will return `None`.

3. `search()`:
    1. We can use this function to search a given pattern anywhere in the string.
    2. If match is available, it returns match object which represents the first occurence of the pattern, ekse it return `None`.

4. `findAll()`:
    1. To find all the occurences of the pattern in a given string.
    2. This function returns a list object which contains all occurrences.

5. `findIter()`
6. `sub()`:
    1. sub means substitution or replacement.
    2. In the target string, every matched pattern will be replaced with the provided replacement.

7. `subm()`:
    1. It is exactly same as `sub()`, but it can also return number of replacements.
8. `split()`: splits the string based on a given delimeter.

## ^ (cap) Symbol
1. We can use this symbol to check whether the given object string starts with our provided pattern or not.
2. If the target string starts with the given pattern, then it returns match object, otherwise `None`.

## $ (dollar) Symbol
1. We can use this symbol to check whether the given string ends with the given pattern or not.
2. If the target string starts with the given pattern, then it returns match object, otherwise `None`.

# Character Classes:

1. ### [abc]: 
    Matches any one of the characters within the brackets, in this case, 'a', 'b', or 'c'.

2. ### [a-z]: 
    Matches any lowercase letter from 'a' to 'z'.

3. ### [A-Z]: 
    Matches any uppercase letter from 'A' to 'Z'.

4. ### [0-9]: 
    Matches any digit from '0' to '9'.

5. ### [a-zA-Z]: 
    Matches any letter, either lowercase or uppercase.

6. ### [^abc]: 
    Matches any character that is not 'a', 'b', or 'c'. The caret (^) at the beginning negates the character class.
7. ### [\d] or [\D] for execpt: 
    Matches any digit, equivalent to [0-9].
8. ### [\w]: 
    Matches any word character, which includes letters, digits, and underscores.
9. ### [\s]: 
    Matches any whitespace character, such as space, tab, or newline.
10. ### [\S]:
    Everything except spaces.
10. ### [aeiou]: 
    Matches any of the vowels 'a', 'e', 'i', 'o', or 'u'.
11. ### [a-z&&[^aeiou]]: 
    Matches any lowercase letter except vowels ('a', 'e', 'i', 'o', 'u').
12. ### (.) :
    Any character including special characters.
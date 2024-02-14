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
    1. 
4. `findAll()`
5. `findIter()`
6. `sub()`
7. `subm()`
8. `split()`
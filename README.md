# AdventOfCode2023  
Day 1  
Idea is to index the word numbers and integers seperately then compare the indexes of those within the original prompt to see which is last and first  
Largest issue came from the fact that when indexing, it returns the first case. Therefore its fixed by indexing in reverse to find the last index. This is easy for integers but with worded numbers it requires indexing the reverse of the number on the reverse of the string

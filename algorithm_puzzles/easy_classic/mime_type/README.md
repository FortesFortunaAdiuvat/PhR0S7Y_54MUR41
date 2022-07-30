# Link
https://www.codingame.com/training/easy/mime-type

## Learning Opportunity
In this puzzle, you have to split a string into separate parts, compare them, and recognize similar strings using a case-insensitive algorithm.

You also have to create and use an associative array and go through a large dataset of elements.

## External Resources
https://en.wikipedia.org/wiki/Associative_array

## Skills
https://www.codingame.com/learn/strings
https://www.codingame.com/learn/hash-tables
https://www.codingame.com/learn/loops
https://www.codingame.com/learn/conditions

## Statement
Back to basics with this puzzle where you have to associate file names with their MIME type.

## Story
So many files, so little time... Let's tidy things up!

## Rules
You are provided with a table which associates MIME types to file extensions. You are also given a list of names of files to be transferred and for each one of these files, you must find the MIME type to be used.

The extension of a file is defined as the substring which follows the last occurrence, if any, of the dot character within the file name.
If the extension for a given file can be found in the association table (case insensitive, e.g. TXT is treated the same way as txt), then print the corresponding MIME type. If it is not possible to find the MIME type corresponding to a file, or if the file doesn’t have an extension, print UNKNOWN.
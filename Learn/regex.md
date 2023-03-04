# Basic syntax
- `. (dot)` matches any character except a newline
- `^` matches the start of a string
- `$` matches the end of a string
- `\` (backslash) is used to escape special characters or to create special sequences
- `[]` (square brackets) matches any character inside the brackets
- `|` (pipe) matches either the expression before or after it
- `()` (parentheses) groups expressions together

# Character classes
- `\d` matches any digit character (0-9)
- `\D` matches any non-digit character
- `\w` matches any word character (alphanumeric and underscore)
- `\W` matches any non-word character
- `\s` matches any whitespace character (space, tab, newline, etc.)
- `\S` matches any non-whitespace character

# Quantifiers
- `*` matches zero or more occurrences of the preceding character or group
- `+` matches one or more occurrences of the preceding character or group
- `?` matches zero or one occurrence of the preceding character or group
- `{n}` matches exactly n occurrences of the preceding character or group
- `{n,}` matches at least n occurrences of the preceding character or group
- `{n,m}` matches between n and m occurrences of the preceding character or group

# Special sequences
- `^` inside square brackets negates the character class 
  - e.g. `[^a-z]` matches any character that is not a lowercase letter
- `\b` matches a word boundary
- `\B` matches a non-word boundary
- `\n` matches a newline character
- `\t` matches a tab character
- `\r` matches a carriage return character
- `\f` matches a form feed character

# Anchors
- `\A` matches the start of a string 
  - like `^`, but doesn't match after a newline
- `\Z` matches the end of a string 
  - like `$`, but doesn't match before a newline
- `\b` matches a word boundary 
  - a zero-width boundary between a word character and a non-word character
- `\B` matches a non-word boundary 
  - a zero-width boundary between two word characters or two non-word characters

# Greedy and lazy quantifiers
- `*`, `+`, and `?` are greedy by default, meaning they match as much as possible 
  - e.g. `.*` matches the entire string
- `*?`, `+?`, and `??` are lazy versions of the same quantifiers, meaning they match as little as possible 
  - e.g. `.*?` matches the smallest possible substring

# Lookahead and lookbehind assertions
- `(?=...)` is a positive lookahead assertion, meaning it matches if the pattern inside the parentheses matches the characters ahead 
  - e.g. `\d+(?=\D)` matches one or more digits followed by a non-digit character, without including the non-digit character in the match
- `(?<=...)` is a positive lookbehind assertion, meaning it matches if the pattern inside the parentheses matches the characters behind 
  - e.g. `(?<=\d\s)\w+` matches one or more word characters preceded by a digit and a whitespace character, without including the digit and whitespace in the match
- `(?!...)` is a negative lookahead assertion, meaning it matches if the pattern inside the parentheses does not match the characters ahead 
  - e.g. `\d+(?!\D)` matches one or more digits that are not followed by a non-digit character
- `(?<!...)` is a negative lookbehind assertion, meaning it matches if the pattern inside the parentheses does not match the characters behind 
  - e.g. `(?<!\d\s)\w+` matches one or more word characters that are not preceded by a digit and a whitespace character

# Grouping and backreferences
- `(pattern)` groups a pattern together and captures the match as a numbered group
- `(?<name>pattern)` groups a pattern together and captures the match as a named group
- `\number` backreferences a numbered group.
  - e.g. `\1` refers to the first group, `\2` refers to the second group, etc.
- `\k<name>` backreferences a named group 
  - e.g. `\k<mygroup>` refers to the group named mygroup

# Non-capturing groups and flags
- `(?:pattern)` groups a pattern together, but does not capture the match as a group
- `(?i)` sets the IGNORECASE flag, making the regex match case-insensitively
- `(?s)` sets the DOTALL flag, making the `.` character match all characters, including newlines
- `(?m)` sets the MULTILINE flag, making `^` and `$` match the start and end of each line, rather than just the start and end of the string

# Atomic groups and possessive quantifiers
- `(?>pattern)` creates an atomic group, meaning the regex engine will not backtrack into the group once it has been matched 
  - useful for optimizing performance and preventing catastrophic backtracking
- `*+`,`++`, and `?+` are possessive versions of the greedy quantifiers, meaning they match as much as possible and do not backtrack 
  - useful for optimizing performance and preventing catastrophic backtracking
  
# Conditionals
- `(?(condition)yes-pattern|no-pattern)` creates a conditional, meaning that if the condition is true, the regex engine matches the yes-pattern, and if the condition is false, it matches the no-pattern. 
  - The condition can be a lookaround or a capturing group that matches a specific value.

# Recursion
- `(?R)` is a recursive reference that matches the entire pattern again. This can be used to match nested structures, like nested parentheses or HTML tags.

# Unicode character classes
- `\p{}` matches any character in a Unicode category or block. For example, `\p{L}` matches any letter, and `\p{Greek}` matches any character in the Greek block.

# Unicode properties
- `\p{}` can also be used with property names, like `\p{script=Arabic}` to match any Arabic script character. Some common Unicode properties include script, category, block, and general_category.

# Subroutine references
- `(?&name)` refers to a named capturing group with the given name. This can be used to create subroutines or sub-patterns that can be reused within the pattern.

# Lookbehinds
- `(?<=pattern)` is a positive lookbehind that matches the current position only if the preceding text matches the pattern. 
  - For example, `(?<=\b\w{3})\w+` matches any word that is preceded by three letters.
- `(?<!pattern)` is a negative lookbehind that matches the current position only if the preceding text does not match the pattern.

# Named capture groups
- `(?P<name>pattern)` creates a named capture group with the given name. 
  - This can make your regex more readable and easier to understand. 
  - For example, `(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})` matches a date in the format YYYY-MM-DD and captures the year, month, and day as named groups.

# Atomic groups
- `(?>pattern)` creates an atomic group that matches the pattern as a whole, without allowing backtracking into the group. 
  - This can be useful for optimizing performance and avoiding catastrophic backtracking.

# Lookahead and lookbehind conditions
- `(?=condition)` is a positive lookahead that matches the current position only if the following text matches the condition. 
  - For example, `^\d+(?=\.)` matches any number at the beginning of a line that is followed by a decimal point.
- `(?!condition)` is a negative lookahead that matches the current position only if the following text does not match the condition.
- `(?<=condition)` is a positive lookbehind that matches the current position only if the preceding text matches the condition.
- `(?<!condition)` is a negative lookbehind that matches the current position only if the preceding text does not match the condition.

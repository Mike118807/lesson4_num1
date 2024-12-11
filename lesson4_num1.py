# You have a script that extracts email addresses from a text but needs to be refined 
# to exclude certain domains (e.g.,'[exclude.com](http://exclude.com/)'). 
# Modify the script to extract all email addresses except those from the specified 
# domain.

# Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)


# Adapt the regex pattern to exclude email addresses from [exclude.com](http://exclude.com/)'



# Exclude email addresses from exclude.com, using a negative lookahead in the regex
# pattern. 


import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)
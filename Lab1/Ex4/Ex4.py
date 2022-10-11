# Write a script that converts a string of characters written in UpperCamelCase into
# lowercase_with_underscores.

import re

def convert(s):
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    print(s)  # camel_case_name

convert("HeiCeFaci")
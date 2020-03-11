"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

```
kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
```
"""

# Mya nd best way solution


import re


def kebabize(string):
    return re.sub(r'(?!^)([A-Z])', r'-\1', re.sub('\d', '', string)).lower()

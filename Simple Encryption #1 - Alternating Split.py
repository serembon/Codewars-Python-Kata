"""For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:
```
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"```

Write two methods:

```def encrypt(text, n)
def decrypt(encrypted_text, n)```

For both methods:

If the input-string is null or empty return exactly this value!
If `n` is `<= 0` then return the input text."""


# My solution

def decrypt1(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    text_list = list(encrypted_text)
    length = len(text_list)
    if length % 2 == 0:
        split_on = length // 2
    else:
        split_on = (length - 1) // 2
    first = text_list[0:split_on]
    second = text_list[split_on:length]

    result_list = [second[i // 2] if i % 2 == 0 else first[(i - 1) // 2] for i in range(0, length)]
    result = ''.join(result_list)
    return decrypt1(result, n - 1)


def encrypt1(text, n):
    if n <= 0:
        return text

    text_list = list(text)
    first = text_list[::2]
    second = text_list[1::2]
    encrypted = second + first
    result = ''.join(encrypted)

    return encrypt1(result, n - 1)

# Best way


def decrypt2(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt2(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

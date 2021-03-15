from .err import Text2qtiError

def remove_pre_tags(s: str):
    result = []

    i = 0
    while i < len(s):
        char = s[i]
        if char == '<' and s[i : i + 5] == '<pre>':
            # There is a pre tag, find the closing pre tag and ignore everything in the middle
            i = s.find('</pre>', i, -1) + 6
            continue
        result.append(char)
        i += 1

    return "".join(result)


        
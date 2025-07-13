from .constants import *

def parse_inline(text):
    result = ""
    i = 0
    n = len(text)

    while i < n:
        if text[i] == "\\":
            result += text[i+1] if i + 1 < n else "\\"
            i += 2 if i + 1 < n else 1
            continue

        if text[i:i+2] in ["**", "__"]:
            end = text.find(text[i:i+2], i + 2)
            if end != -1:
                result += BOLD + parse_inline(text[i+2:end]) + BOLD_
                i = end + 2
                continue

        if text[i] in ["*", "_"] and i+1 < n and text[i+1] != " ":
            end = text.find(text[i], i + 1)
            if end != -1:
                result += ITALIC + parse_inline(text[i+1:end]) + ITALIC_
                i = end + 1
                continue

        if text[i:i+2] == "~~":
            end = text.find("~~", i + 2)
            if end != -1:
                result += STRIKETHROUGH + parse_inline(text[i+2:end]) + STRIKETHROUGH_
                i = end + 2
                continue

        if text[i] == "`":
            end = text.find("`", i + 1)
            if end != -1:
                result += CODE + text[i+1:end] + RESETCOLOR
                i = end + 1
                continue

        if text[i] == "[":
            end_text = text.find("]", i + 1)
            if end_text != -1 and end_text + 1 < n and text[end_text + 1] == "(":
                end_url = text.find(")", end_text + 2)
                if end_url != -1:
                    label = text[i+1:end_text]
                    result += LINK + label + RESETCOLOR
                    i = end_url + 1
                    continue

        result += text[i]
        i += 1

    return result

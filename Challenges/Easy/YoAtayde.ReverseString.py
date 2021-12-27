def reverse(text: str) -> str:
    text2 = ""
    index = len(text)
    while index > 0 :
        index -= 1
        text2 += text[index]
    return text2


print(reverse("Hello World!"))

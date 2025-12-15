# string_utils.py

def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

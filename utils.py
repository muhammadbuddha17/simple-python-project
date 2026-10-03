def reverse(text):
 return text[::-1]
def is_palindrome(text):
 cleaned = "".join(c.lower() for c in text if c.isalnum())
 return cleaned == cleaned[::-1]
def word_count(text):
 return len(text.split())

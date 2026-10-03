from utils import reverse, is_palindrome, word_count
def test_reverse():
 assert reverse("abc") == "cba"
def test_palindrome():
 assert is_palindrome("A man, a plan, a canal: Panama")
 assert not is_palindrome("hello")
def test_word_count():
 assert word_count("hello big world") == 3

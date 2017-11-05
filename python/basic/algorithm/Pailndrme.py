class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

print(Palindrome.is_palindrome('Deleveled'))
1. Describe the Problem
    As a user, they wants to improve grammar by checking text.
    It should start with capital letter an ends with suitable sentence-ending punctuation mark.
    
2. Design the Function Signature
    The signature of a function includes:

    def grammar_checker(text):
        Verify if string starts with capital letter and ends with punctuation mark.

        Parameter:
        Text: a string of text to check

        Returns: a boolean value

        Example: True or False

        Side effects:
        Exception for inputs if it's not a string
        Exception for input that is equal to None
3. Examples as Tests

    """
    Given a string of 1 capitalized word and exclamaition mark.
    Returns True
    """
    def test_one_uppercase_word('Hello!'):
        ==> True

    """
    Given a string of 1 capitalized word without any punctuation marks.
    Returns False
    """

    def test_one_uppercase_word_no_puctuation('Hey'):
        ==> False
        
    """
    Given a string of a sentence witout capitalized letter and with full stop on the end.
    Returns False
    """

    def test_no_uppercase_with_punctuation('have a nice day.'):
        ==> False

    """
    Given a string with all capitalized words no puctuation.
    Return False
    """

    def test_sentence_uppercase_with_no_punctuation('HAVE A NICE DAY'):
        ==> False

    """
    Given an empty string.
    Raise Exception
    """

    def test_empty_string(''):
        ==> 'No string was given"

    """
    Given None type value.
    Raises Exception
    """

    def test_none_value(None):
        ==> 'No string was given"



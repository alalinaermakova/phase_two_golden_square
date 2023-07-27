1. Describe the Problem
   User wants to keep track of their tasks.
   Check if a text includes the string #TODO.

2. Design the Function Signature
    The signature of a function includes:

    def check_todos(text):

    Verify in text includes #TODO.

    Parameter:
    A string with text to check

    Returns:
    Bolean value

    Example:
    True or False

    Side effects:
    Exception for inputs if it's not a string
    Exception for input that is equal to None

3. Examples as Tests

    """
    Given a string of a sentence that includes #TODO
    Returns True
    """

    def test_string_with_todo('#TODO: Record the video for this challenge')
        ==> True

    """
    Given a string of a sentence that includes # and some words
    Returns False
    """

    def test_string_without_todo("#Make a list"):
        ==> False

    """
    Given a string of a sentence to do
    Returns False
    """

    def test_string_with_task("to do dishes"):
        ==> False

    """
    Given an empty string
    Raise Exception "No string was given"
    """

    def test_empty_string(''):
        raise Exception

    """
    Given a None value
    Raise Exception "No string was given"
    """

    def test_none_value(None):
        raise Exception 


    


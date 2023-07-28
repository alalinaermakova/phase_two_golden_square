1. Describe the problem
    User needs an interface that checks the text for grammar,
    for example if text begins with capital letter and ends with a sentence ending punctuation mark.

2. Design the function signature.
    The signature of a class includes:
    class GrammarStats:
        def __init__(self):
            pass
    
        def check(self, text):
            # Parameters:
            #   text: string
            # Returns:
            #   bool: true if the text begins with a capital letter and ends with a
            #         sentence-ending punctuation mark, false otherwise
            pass
    
        def percentage_good(self):
            # Returns:
            #   int: the percentage of texts checked so far that passed the check
            #        defined in the `check` method. The number 55 represents 55%.
            pass

3. Examples as Tests

"""
Giving the string of text
Returns boolean value True
"""

checker = GrammarStats()
checker.check("Hello!") ==> True

"""
Giving the string of text
Returns boolean value False
"""

checker = GrammarStats()
checker.check("Hello") ==> False

"""
Calculating the percentage of texts checked
Returns the integer
"""

checker = GrammarStats()
checker.check("Hello!") ==> True
checker.percentage_good() ==> 100

"""
Given an empty string.
Raise Exception
"""

checker = GrammarStats()
checker.check("") ==> 'No string was given" 

"""
Given None type value.
Raises Exception
"""

checker = GrammarStats()
checker.check(None) ==> 'No string was given"





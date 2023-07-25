1. Describe the Problem
As a user, they need to manage their time. We need to show an estimate of reading time for
a text. Assume that they can read 200 words per minute.

2. Design the Function Signature
The signature of a function includes:

def count_time_for_text_reading(text):
    """Counts how much time it takes to read the text"""


    Parameters:
    
    text = a string of text (e.g. "potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed viverra tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius duis at consectetur lorem donec massa sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor eu augue ut lectus arcu bibendum at varius vel pharetra vel turpis nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a cras semper auctor neque vitae tempus quam pellentesque nec nam aliquam sem et tortor consequat id porta nibh venenatis cras sed felis eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper quis lectus nulla at volutpat diam ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet proin fermentum leo vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget nullam non nisi est sit amet facilisis magna etiam tempor orci eu lobortis elementum nibh tellus molestie nunc non blandit massa enim nec dui nunc mattis enim ut tellus elementum sagittis")

    returns: a string with how many minutes

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """

3. Create Examples as Tests
These are examples of the function being called with particular arguments, and what the function should return in each situation.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the function to return the right value for the given arguments.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.
1. Describe the problem
    User need an interface that helps to: format diary entry, count words in a diary entry,
    reading time for contents, and recieve a chunk of a content that he can read in a given minutes.

2. Design the function signature.
    The signature of a class includes:
    4 different functions:
        1. def format():
            Parameters: none
            Returns: a formatted text
        2. def counting_words():
            Parameters: none
            Returns: the number of words in a diary entry
        3. def reading_time(wpm):
            Parameters: an integer that represents the number of words that user can read per minute
            Returns: a estimate reading time in minutes for the contents at a given wpm
        4. def reading_chunk(wpm, minutes):
            Parameters: an integer that represents the number of words that user can read per minute
            an integer that represents the number of minutes that user has to read
            Returns: a string which is a chunk of the contents that user could read in the given number of minutes.

3. Examples as Tests
    """
    Giving the title and contents through
    Format the content to show
    """

    my_diary = DiaryEntry('June 2023', 'On tuesday walk the neighbour's dog')
    my_diary.format() ==> 'June 2023: On tuesday walk the neighbour's dog'

    """
    Giving the contents in string format
    Returns the number of words in a diary entry (integer)
    """

    my_diary = DiaryEntry('June 2023', 'On tuesday walk the neighbour's dog')
    my_diary.counting_words() ==> 8

    """
    Giving the word per minute that user can read
    Returns the estimate reading time in number of minutes/seconds (float)
    """

    my_diary = DiaryEntry('June 2023', 'On tuesday walk the neighbour's dog')
    my_diary.reading time(200) ==> 0.03 seconds

    """
    Given the words per min and the number of minutes that user has to read
    Rturns a chunk of the content that user could read in the given number of minutes
    """

    my_diary = DiaryEntry('June 2023', 'On tuesday walk the neighbour's dog')
    my_diary.reading_chunk(200, 1) ==> "leo vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget nullam non nisi est sit amet facilisis magna etiam tempor orci eu lobortis elementum nibh tellus molestie nunc non blandit massa enim nec dui nunc mattis enim ut tellus elementum sagittis vitae et leo duis ut diam quam nulla porttitor massa id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada nunc vel risus commodo viverra maecenas accumsan lacus vel facilisis volutpat est velit egestas dui id ornare arcu odio ut sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor elit sed vulputate mi sit amet mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut consequat semper viverra nam libero justo laoreet sit amet cursus sit amet dictum sit amet justo donec enim diam vulputate ut pharetra sit amet aliquam id diam maecenas ultricies mi"
    





        
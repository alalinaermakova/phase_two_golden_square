def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        print(counter.items())
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[1][0]
    # we are putting reverse=True to get most common letter i.e the biggest number from the letter's value
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
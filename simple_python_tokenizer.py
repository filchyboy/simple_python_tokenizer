import re

sample = "Friends, Romans, countrymen, lend me your ears; \
    if my eyes but see through yon window breaks a lovely moon made of cheese."
sample.split(" ")
sample = sample+" 911"
#print(sample)
re.sub('[^a-zA-Z 0-9]', '', sample)

# now a function

def tokenize(text):
    """Parses a string into a list of semantic units (words)

    Args:
        text (str): The string that the function will tokenize.

    Returns:
        list: tokens parsed out by the mechanics of your choice
    """
    
    tokens = re.sub('[^a-zA-Z 0-9]', '', text)
    tokens = tokens.lower().split()
# return token to do something with this programmaticaly    
#    return tokens
# print tokens to just see what comes out.
    print(tokens)

tokenize(sample)
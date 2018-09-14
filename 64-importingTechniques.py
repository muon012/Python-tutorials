# Since "import" will give an error for files with "-" in their names, we can use the next method:
bj = __import__("63-blackjackGame")

# This returns "__main__" because we are working on this file. The name of this file will default to "main" if it is
# run from within;
print(__name__)
# This prints "63-blackjack" because it is the name of the file imported;
print(bj.__name__)
# We invoke a function from the file that we imported;
bj.play()

print("++++++++++++")
bj.deck_info()

# UNDERSCORES
# When using words that are reserved for python; We should add an underscore at the end of it to make it a new word
# that contextually makes sense; i.e. use "from_" instead of python's "from" for your new attribute/variable;
# In python, you can alter and access private objects imported to your files;
# This means, you can use or change anything in the imports; However, this is not recommended;
# A name with an underscore means that it should be protected and therefore, you should never change it or use it
# outside the module it comes from;


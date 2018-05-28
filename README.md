# sonnetMaker
A python program that can make sonnets, either out of a Markov chain or by listening to tweets.

Credits:
This idea was inspired by "The Longest Poem in the World"

http://www.longestpoemintheworld.com/

I used code from:
https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

https://stackoverflow.com/questions/46759492/syllable-count-in-python

https://github.com/kevin-brown/rhyme-detect/blob/master/rhyme_detect/rhymes.py

Thank you to those good people.

Dependencies:

The natural language toolkit: https://www.nltk.org/

Markovify: https://github.com/jsvine/markovify

This code was designed for Python 2.

Here's what it does
(The twitter half):

The code listens for 2000 tweets that are written with common English words.
It stores tweets that are written with ten syllables in another file (this mimics iambic pentameter).
It checks each line to see if it rhymes with another line. If they do rhyme, it stores that couplet in another file.
The file shuffles these lines around and prints a sonnet.
It also stores those couplets and that sonnet in poetry files.

Here's what it does
(The markov half):

The code looks at a file that's supposed to be filled with some seed text.
Then, it outputs some semi-randomly generated sentences based on that seed text using a Markov chain.
It stores the lines that are written with ten syllables in another file (this mimics iambic pentameter).
It checks each line to see if it rhymes with another line. If they do rhyme, it stores that couplet in another file.
The file shuffles these lines around and prints a sonnet.
It also stores those couplets and that sonnet in poetry files.

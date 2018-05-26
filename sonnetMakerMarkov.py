import nltk
import rhymes
import re
import string
import markovify

_numberOfLinesConstant = 4000
#I'm gonna take the time here to empty the contents of intake.txt, iambicPentameter.txt, and the couplet files
open('data/iambicPentameter.txt','w').close()
open('couplets.txt','w').close()

#this function will use a Markov chain to make human-like text based off of whatever is placed in corpus.txt
def intake():
    textOfCorpus = ''
    print('Training several thousand monkeys to write Shakespeare')
    print('Writing ' + str(_numberOfLinesConstant) + ' lines of text')
    open('data/intake.txt','w').close()

    with open('corpus.txt') as jkl:
        textOfCorpus = jkl.read()
    textOfCorpusModel = markovify.Text(textOfCorpus)
    with open('data/intake.txt','a') as markovOutput:
        for i in range(_numberOfLinesConstant):
            markovOutput.write(str(textOfCorpusModel.make_short_sentence(140)) + '\n')

    print('The monkeys have finished')

def iambicPentameter(tweet):
    #this is going to return a boolean
    #it'll tell the call statement whether each tweet has ten syllables or not
    listOfWordsInTweet = tweet.split()
    syllableCounter = 0
    for word in listOfWordsInTweet:
        syllableCounter = syllableCounter + syllable_count(word)
    if (syllableCounter == 10):
        return True
    else:
        return False

def syllable_count(word):
    #this will tell us how many syllables are in each word that we give it
    #I got this from https://stackoverflow.com/questions/46759492/syllable-count-in-python
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count

#okay. All that up ^ there was just function declarations.
#here's the bit where we call them all in
#and they all work together
# (like voltron)

intake()
unsortedLines = [line.rstrip('\n') for line in open('data/intake.txt')]
unsortedLines = [re.sub('rt ','',line) for line in unsortedLines] #this strips retweets of that weird 'rt ' tag
unsortedLinesWithoutWeirdStuff = []
for line in unsortedLines:
    unsortedLinesWithoutWeirdStuff.append(re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)) #gets rid of urls
for line in unsortedLinesWithoutWeirdStuff:
    if (iambicPentameter(line)):
        with open('data/iambicPentameter.txt','a') as p:
            p.write(line + '\n')
sortedLines = [line.rstrip('\n') for line in open('data/iambicPentameter.txt')]

print('Finished sorting tweets\nFinding rhymes')

#so now we have a list of lines which each have ten syllables
#we're gonna look through the iambicPentameter file for lines that rhyme with the first, second, etc, until we have seven couplets
numberOfCouplets = 0
indexOfLineA = 0
while (numberOfCouplets < 7):
    lineA = sortedLines[indexOfLineA]
    for lineB in sortedLines[(1 + indexOfLineA):]:
        if ((not (lineA.translate(None, string.punctuation).split()[-1] == lineB.translate(None, string.punctuation).split()[-1])) and (rhymes.line_similarity(lineA,lineB) > 2) and (not ((lineA in open('couplets.txt').read()) or (lineB in open('couplets.txt').read()) or (lineA == lineB)))):
            print('Found rhyme number ' + str(1 + numberOfCouplets))
            with open('couplets.txt','a') as k:
                k.write(lineB + '\n' + lineA + '\n')
            numberOfCouplets = numberOfCouplets + 1
            break
    indexOfLineA = indexOfLineA + 1
    print('Moving on to line ' + str(1 + indexOfLineA))
print('Finished checking for rhyming couplets\nPrinting finished sonnet')
#oof. That's some nasty code right there
#Trust me, it works (mostly)
#I've also changed it so that it ignores any tweet that already exists in the 'couplets' file
#it also ignores lines with the same word at the end
#this might not work if the line ends with an emoticon or punctuation though, I'm not sure
#that's what that crazy long conditional is for

coupletList = [line.rstrip('\n') for line in open('couplets.txt')]
poem = ''
title = ''
titleList = ''
titleList = coupletList[0].split()
title = titleList[0]
pageBreak = '----------------------------------------------------------'
poem = pageBreak + '\n\n' + title + '\n\n' + coupletList[0] + '\n' + coupletList[2] + '\n' + coupletList[1] + '\n' + coupletList[3] + '\n\n' + coupletList[4] + '\n' + coupletList[6] + '\n' + coupletList[5] + '\n' + coupletList[7] + '\n\n' + coupletList[8] + '\n' + coupletList[10] + '\n' + coupletList[9] + '\n' + coupletList[11] + '\n\n' + coupletList[12] + '\n' + coupletList[13] + '\n\n' + pageBreak
print(poem)
with open('completedSonnets.txt','a') as finishedWork:
    finishedWork.write(poem)

#just for fun, let's add each couplet to another .txt file
#that way, we'll end up with an ever-expanding poem that's far more simple than this sonnet business
with open('neverEndingCoupletPoem.txt','a') as extraPoem:
    for i in coupletList:
        extraPoem.write(i + '\n')
#done

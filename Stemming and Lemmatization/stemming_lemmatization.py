Stemming and Lemmatization
--> Both used to derive base word

1. Stemming - Use some rules, some fixed rules like removing ing, removing able etc. to transform the word to its base word.

2. Lemmatization - Use knowledge of the language to derive the base word, (linguistic knowledge)

importing libraries
import nltk
import spacy
Stemming in NLTK using PorterStemmer and SnowballStemmer
from nltk.stem import PorterStemmer, SnowballStemmer

## creating objects of the stemming classes
stemmer_p = PorterStemmer()
stemmer_s = SnowballStemmer(language = 'english') 
# help(nltk.stem.SnowballStemmer)
## let's apply stemming on some of the basis words

words = ['eating', 'ate', 'eats', 'eat', 'ability', 'enjoying', 'enjoyed', 'funny', 'meeting', 'gone', 'came']

print("Word", " | ", "Stemmer_P", " | ", "Stemmer_S")

for word in words:
    print(word, " | ", stemmer_p.stem(word), " | ", stemmer_s.stem(word))
Word  |  Stemmer_P  |  Stemmer_S
eating  |  eat  |  eat
ate  |  ate  |  ate
eats  |  eat  |  eat
eat  |  eat  |  eat
ability  |  abil  |  abil
enjoying  |  enjoy  |  enjoy
enjoyed  |  enjoy  |  enjoy
funny  |  funni  |  funni
meeting  |  meet  |  meet
gone  |  gone  |  gone
came  |  came  |  came
 
Lemmatization using Spacy
nlp = spacy.load("en_core_web_sm") #sm - small, md - medium
## application of lemmatization in spacy

docs = nlp('eating ate eats eaten ability enjoying enjoyed funny meeting gone came better')

for doc in docs:
    print(doc, " | ", doc.lemma_, " | ", doc.lemma)  #.lemma will o/p the hash of each word, unique identifier
eating  |  eat  |  9837207709914848172
ate  |  eat  |  9837207709914848172
eats  |  eat  |  9837207709914848172
eaten  |  eat  |  9837207709914848172
ability  |  ability  |  11565809527369121409
enjoying  |  enjoy  |  13716726989081948958
enjoyed  |  enjoy  |  13716726989081948958
funny  |  funny  |  4122592809438271869
meeting  |  meeting  |  14798207169164081740
gone  |  go  |  8004577259940138793
came  |  come  |  5307304325359566725
better  |  well  |  4525988469032889948
##lemmatization in mltk

from nltk.stem import WordNetLemmatizer

'''Wordnet is a large, free, and publicly available lexical database for the English language 
   aiming to establish structured semantic relationships between words.'''

nltk.download('wordnet')
nltk.download('omw-1.4')
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\saiba\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to
[nltk_data]     C:\Users\saiba\AppData\Roaming\nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!
True
## initialize wordnet lemmatizer
wordnet_lemma = WordNetLemmatizer()

words = ['eating', 'ate', 'eats', 'eaten', 'ability', 'enjoying', 'enjoyed', 'funny', 'meeting', 'gone', 'came', 'hardly', 'bought', 'better']

for token in words:
    print(token, " | ", wordnet_lemma.lemmatize(token, pos = 'v'))
    '''The code then performs lemmatization on each word in the list using the lemmatize() method of the WordNetLemmatizer class, 
    with the optional argument pos="v" indicating that the words should be lemmatized as verbs.'''
eating  |  eat
ate  |  eat
eats  |  eat
eaten  |  eat
ability  |  ability
enjoying  |  enjoy
enjoyed  |  enjoy
funny  |  funny
meeting  |  meet
gone  |  go
came  |  come
hardly  |  hardly
bought  |  buy
better  |  better
Customizing the attribute_ruler
nlp.pipe_names
['tok2vec', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']
## customizing the pipe
cr = nlp.get_pipe('attribute_ruler')  

cr.add([[{'TEXT':'Bro'}],[{'Text' : 'Brah'}]], {"LEMMA" : "Brother"})   #customizing the word bro and brah and will give brother whenever asked for lemma
'''for Bro and Brah base word will be Brother.'''

doc = nlp("Bro, do you wanna go? Brah, don't say no! I am exhausted.")

for token in doc:
    print(token.text, " | ", token.lemma_)
Bro  |  Brother
,  |  ,
do  |  do
you  |  you
wanna  |  wanna
go  |  go
?  |  ?
Brah  |  Brother
,  |  ,
do  |  do
n't  |  not
say  |  say
no  |  no
!  |  !
I  |  I
am  |  be
exhausted  |  exhaust
.  |  .
doc[0], doc[0].lemma_, doc[0].lemma
(Bro, 'Brother', 4347558510128575363)
Practice
1 . import necessary libraries and packages
import nltk
import spacy

from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
## importing libraries
from nltk.tokenize import word_tokenize

# nltk.download('wordnet')
# nltk.download('omw-1.4')
## loading english language package

nlp = spacy.load('en_core_web_sm')
Exercise 1 :
1. Convert these list of words into base form using Stemming and Lemmatization and observe the transformations
2. Write a short note on the words that have different base words using stemming and Lemmatization
## craeting instance of Stemmer classes
stemmer_p = PorterStemmer()
stemmer_s = SnowballStemmer(language = 'english')
#using stemming in nltk
list_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

print("WORD", " | ", "PorterStemmed_WORD", " | ", "SNOWBALLStremmed_WORD")

for token in list_words:
    print(token, " | ", stemmer_p.stem(token), " | ", stemmer_s.stem(token))
WORD  |  PorterStemmed_WORD  |  SNOWBALLStremmed_WORD
running  |  run  |  run
painting  |  paint  |  paint
walking  |  walk  |  walk
dressing  |  dress  |  dress
likely  |  like  |  like
children  |  children  |  children
whom  |  whom  |  whom
good  |  good  |  good
ate  |  ate  |  ate
fishing  |  fish  |  fish
#using lemmatization in spacy

doc = nlp("running painting walking dressing likely children who good ate fishing")
# lemmatization

for token in doc:
    print(token, " | ", token.lemma_)
running  |  run
painting  |  paint
walking  |  walk
dressing  |  dress
likely  |  likely
children  |  child
who  |  who
good  |  good
ate  |  eat
fishing  |  fishing
Conclusion :

Stemming is basically deriving base word of a word using some rules without knowledge of the language. For an example, ate is not converted to eat while using stemmer but lemmatizer has converted it to eat, cause it has the linguistic knowkedge.

On the other hand, children is converted to child by lemmatizer but it wasn't changed by stemmer.

Same happened with, fishing, where stemming has changed it to fish but lemmatization hasn't.

Exercise2:
convert the given text into it's base form using both stemming and lemmatization
text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""
##using stemming in nltk

##step - 1 : word tokenization
list_words = word_tokenize(text)

stemmed_words = []

## step - 2 : getting base form for each token using stemmer
for token in list_words:
    # print(token, " | ", stemmer_p.stem(token), " | ", stemmer_s.stem(token))
    stemmed_words.append(stemmer_p.stem(token))

    
#step3: joining all words in a list into string using 'join()'
final_text_stemming = ' '.join(stemmed_words)
print(final_text_stemming)
latha is veri multi talent girl.sh is good at mani skill like danc , run , sing , playing.sh also like eat pav bhagi . she ha a habit of fish and swim too.besid all thi , she is a wonder at cook too .
#using lemmatisation in spacy


#step1: Creating the object for the given text
doc = nlp(text)

list_words = []
#step2: getting the base form for each token using spacy 'lemma_'
for token in doc:
    # print(token, " | ", token.lemma_)
    list_words.append(token.lemma_)
    

#step3: joining all words in a list into string using 'join()'
final_text_lemma = ' '.join(list_words)
print(final_text_lemma)
Latha be very multi talented girl . she be good at many skill like dancing , running , singing , play . she also like eat Pav Bhagi . she have a 
 habit of fishing and swim too . besides all this , she be a wonderful at cook too . 

## lemmatization using nltk

## step - 1 : creating word tokenize
list_words = word_tokenize(text)
lemmatized_words = []

## step - 2 : lemmatization using WordNetLemmatizer Class
word_net = WordNetLemmatizer()
for token in list_words:
    # print(token, " | ", word_net.lemmatize(token, pos = 'v'))
    lemmatized_words.append(word_net.lemmatize(token, pos = 'v'))
    
    
## step - 3 : joining all words in a list into string using `join()`
final_text_lemmatize_nltk = ' '.join(lemmatized_words)
print(final_text_lemmatize_nltk)
Latha be very multi talented girl.She be good at many skills like dance , run , sing , playing.She also like eat Pav Bhagi . she have a habit of fish and swim too.Besides all this , she be a wonderful at cook too .

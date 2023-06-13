Natural Language Processing with Spacy and Python
NoteBook Context :
SpaCy Structure
Sentence Boundary Detection(SBD):
Token Attributes
Part of Speech Tagging(POS)
Named Entity Recognition(NER)
Word Vectors
spaCy's Pipelines
## importing packages

import spacy
import en_core_web_sm
## creating instance for work

nlp = spacy.load("en_core_web_sm")
nlp
<spacy.lang.en.English at 0x266e1f92e50>
with open('data/wiki_us.txt', 'r') as f:
    text = f.read()
# print(text)
SpaCy Structure
SpaCy Structure

## applying the instance

Doc = nlp(text)
# print(Doc)
## compare between Doc and text

print(len(text))
print(len(Doc))
3535
652
## deep dive into text and Doc

for token in text[:10]:
    print(token)
T
h
e
 
U
n
i
t
e
d
for token in Doc[:10]:
    print(token)
The
United
States
of
America
(
U.S.A.
or
USA
)
Doc object is considering only the tokens like word or punctuations, whereas the text object is taking all letter seperately into accounts.

for token in text.split(' ')[:10]:
    print(token)
The
United
States
of
America
(U.S.A.
or
USA),
commonly
known
Sentence Boundary Detection(SBD):
In NLP, sentence boundary detection, or SBD, is the identification of sentences in a text. -- Sentence Tokenizer

for sent in Doc.sents:
    print(sent)
The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America.
It consists of 50 states, a federal district, five major unincorporated territories, 326 Indian reservations, and some minor possessions.[j]
At 3.8 million square miles (9.8 million square kilometers), it is the world's third- or fourth-largest country by total area.[d]
The United States shares significant land borders with Canada to the north and Mexico to the south, as well as limited maritime borders with the Bahamas, Cuba, and Russia.[22] With a population of more than 331 million people, it is the third most populous country in the world.
The national capital is Washington, D.C., and the most populous city is New York.


Paleo-Indians migrated from Siberia to the North American mainland at least 12,000 years ago, and European colonization began in the 16th century.
The United States emerged from the thirteen British colonies established along the East Coast.
Disputes over taxation and political representation with Great Britain led to the American Revolutionary War (1775Ã¢â‚¬â€œ1783), which established independence.
In the late 18th century, the U.S. began expanding across North America, gradually obtaining new territories, sometimes through war, frequently displacing Native Americans, and admitting new states; by 1848, the United States spanned the continent.
Slavery was legal in the southern United States until the second half of the 19th century when the American Civil War led to its abolition.
The SpanishÃ¢â‚¬â€œAmerican War and World War I established the U.S. as a world power, a status confirmed by the outcome of World War II.


During the Cold War, the United States fought the Korean War and the Vietnam War but avoided direct military conflict with the Soviet Union.
The two superpowers competed in the Space Race, culminating in the 1969 spaceflight that first landed humans on the Moon.
The Soviet Union's dissolution in 1991 ended the Cold War, leaving the United States as the world's sole superpower.


The United States is a federal republic and a representative democracy with three separate branches of government, including a bicameral legislature.
It is a founding member of the United Nations, World Bank, International Monetary Fund, Organization of American States, NATO, and other international organizations.
It is a permanent member of the United Nations Security Council.
Considered a melting pot of cultures and ethnicities, its population has been profoundly shaped by centuries of immigration.
The country ranks high in international measures of economic freedom, quality of life, education, and human rights, and has low levels of perceived corruption.
However, the country has received criticism concerning inequality related to race, wealth and income, the use of capital punishment, high incarceration rates, and lack of universal health care.


The United States is a highly developed country, accounts for approximately a quarter of global GDP, and is the world's largest economy.
By value, the United States is the world's largest importer and the second-largest exporter of goods.
Although its population is only 4.2% of the world's total, it holds 29.4% of the total wealth in the world, the largest share held by any country.
Making up more than a third of global military spending, it is the foremost military power in the world; and it is a leading political, cultural, and scientific force internationally.[23]
# sentence1 = Doc.sents[0]
TypeError: 'generator' object is not subscriptable


We got an error. That is because the sents attribute is a generator. In python, we can usually iterate over generators by converting them into a list. So, let’s do that.

sentence1 = list(Doc.sents)[0]
print(sentence1)
The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America.
Token Attributes
The token object contains a lot of different attributes that are VITAL do performing NLP in spaCy, such as:

text

head

left_edge

right_edge

ent_type_

iob_

lemma_

morph

pos_

dep_

lang_

Text: The original word text.

Lemma: The base form of the word.

POS: The simple UPOS part-of-speech tag.

Tag: The detailed part-of-speech tag.

Dep: Syntactic dependency, i.e. the relation between tokens.

Shape: The word shape – capitalization, punctuation, digits.

is alpha: Is the token an alpha character?

is stop: Is the token part of a stop list, i.e. the most common words of the language?

token2 = sentence1[7]
print(token2)
or
Text
token2.text
'or'
Head
This tells to which word it is governed by, in this case, the primary verb, “is”, as it is part of the noun subject.

token2.head
U.S.A.
left_edge
token2.left_edge
or
right_edge
token2.right_edge
or
### type of entity

token2.ent_type
0
### name of entity type

token2.ent_type_
''
### ent_iob

'''IOB code of named entity tag. 
“B” means the token begins an entity, 
“I” means it is inside an entity, 
“O” means it is outside an entity, 
and "" means no entity tag is set.'''

token2.ent_iob_
'O'
### lemma

'''Base form of the token, with no inflectional suffixes'''

token2.lemma_
'or'
# sentence1[12]

sentence1[12].lemma_
'know'
### morph

token2.morph, sentence1[12].morph
(ConjType=Cmp, Aspect=Perf|Tense=Past|VerbForm=Part)
### POS(Parts of Speech)


'''Coarse-grained part-of-speech from the Universal POS tag set.'''

token2.pos_, sentence1[12].pos_
('CCONJ', 'VERB')
### Syntatic Dependency

'''Syntactic dependency relation.'''

token2.dep_, sentence1[12].dep_, sentence1[2].dep_ 
('cc', 'acl', 'nsubj')
'cc' --> conjunction
'nsubj' --> noun subject
'acl' --> adnominal clause
### Language

'''Languageof the parent document's vocabulary'''

token2.lang_
'en'
Part of Speech Tagging(POS)
for token in sentence1:
    print(token.text, token.pos_, token.dep_)
The DET det
United PROPN compound
States PROPN nsubj
of ADP prep
America PROPN pobj
( PUNCT punct
U.S.A. PROPN appos
or CCONJ cc
USA PROPN conj
) PUNCT punct
, PUNCT punct
commonly ADV advmod
known VERB acl
as ADP prep
the DET det
United PROPN compound
States PROPN pobj
( PUNCT punct
U.S. PROPN appos
or CCONJ cc
US PROPN conj
) PUNCT punct
or CCONJ cc
America PROPN conj
, PUNCT punct
is AUX ROOT
a DET det
country NOUN attr
primarily ADV advmod
located VERB acl
in ADP prep
North PROPN compound
America PROPN pobj
. PUNCT punct
text2 = "I hope this framework will be very useful for all of your machine learning projects that you plan to deploy in the future. Let's go to the next video."
Doc2 = nlp(text2)
print(Doc2)
I hope this framework will be very useful for all of your machine learning projects that you plan to deploy in the future. Let's go to the next video.
sentence2 = Doc2.sents
print(list(sentence2))
[I hope this framework will be very useful for all of your machine learning projects that you plan to deploy in the future., Let's go to the next video.]
for token in Doc2:
    print(token.text, token.pos_, token.dep_)
I PRON nsubj
hope VERB ROOT
this DET det
framework NOUN nsubj
will AUX aux
be AUX ccomp
very ADV advmod
useful ADJ acomp
for ADP prep
all PRON pobj
of ADP prep
your PRON poss
machine NOUN compound
learning NOUN compound
projects NOUN pobj
that PRON dobj
you PRON nsubj
plan VERB relcl
to PART aux
deploy VERB xcomp
in ADP prep
the DET det
future NOUN pobj
. PUNCT punct
Let VERB ROOT
's PRON nsubj
go VERB ccomp
to ADP prep
the DET det
next ADJ amod
video NOUN pobj
. PUNCT punct
## visualize the sentence with displacy function

from spacy import displacy
displacy.render(Doc2, style = 'dep')
IPRON
hopeVERB
thisDET
frameworkNOUN
willAUX
beAUX
veryADV
usefulADJ
forADP
allPRON
ofADP
yourPRON
machineNOUN
learningNOUN
projectsNOUN
thatPRON
youPRON
planVERB
toPART
deployVERB
inADP
theDET
future.NOUN
LetVERB
'sPRON
goVERB
toADP
theDET
nextADJ
video.NOUN
text3 = 'My name is Saibal.'

Doc3 = nlp(text3)
for token in Doc3:
    print(token.text, token.lemma_, token.pos_,
         token.tag_, token.dep_, token.shape_,
         token.is_alpha, token.is_stop)
My my PRON PRP$ poss Xx True True
name name NOUN NN nsubj xxxx True True
is be AUX VBZ ROOT xx True True
Saibal Saibal PROPN NNP attr Xxxxx True False
. . PUNCT . punct . False False
## visualize the sentence

from spacy import displacy
displacy.render(Doc3, style = 'dep')
MyPRON
nameNOUN
isAUX
Saibal.PROPN
Named Entity Recognition(NER)
for ent in Doc.ents:
    print(ent.text, ent.label_)
The United States of America GPE
U.S.A. GPE
USA GPE
the United States GPE
U.S. GPE
US GPE
America GPE
North America LOC
50 CARDINAL
five CARDINAL
326 CARDINAL
Indian NORP
3.8 million square miles QUANTITY
9.8 million square kilometers QUANTITY
third- or fourth DATE
The United States GPE
Canada GPE
Mexico GPE
Bahamas GPE
Cuba GPE
more than 331 million CARDINAL
third ORDINAL
Washington GPE
D.C. GPE
New York GPE
Paleo-Indians NORP
Siberia LOC
North American NORP
at least 12,000 years ago DATE
European NORP
the 16th century DATE
The United States GPE
thirteen CARDINAL
British NORP
the East Coast LOC
Great Britain GPE
the American Revolutionary War ORG
1775Ã¢â‚¬â€œ1783 CARDINAL
the late 18th century DATE
U.S. GPE
North America LOC
Native Americans NORP
1848 DATE
the United States GPE
United States GPE
the second half of the 19th century DATE
the American Civil War ORG
The SpanishÃ¢â‚¬â€œAmerican War and World War EVENT
U.S. GPE
World War II EVENT
the Cold War EVENT
the United States GPE
the Korean War EVENT
the Vietnam War EVENT
the Soviet Union GPE
two CARDINAL
the Space Race FAC
1969 DATE
first ORDINAL
Moon PERSON
The Soviet Union's GPE
1991 DATE
the Cold War EVENT
the United States GPE
The United States GPE
three CARDINAL
the United Nations ORG
World Bank ORG
International Monetary Fund ORG
Organization of American States ORG
NATO ORG
the United Nations Security Council ORG
centuries DATE
The United States GPE
approximately a quarter DATE
the United States GPE
second ORDINAL
only 4.2% PERCENT
29.4% PERCENT
more than a third CARDINAL
## Visualize the Named Entity Recognition(NER)

from spacy import displacy
displacy.render(Doc, style = 'ent')
The United States of America GPE ( U.S.A. GPE or USA GPE ), commonly known as the United States GPE ( U.S. GPE or US GPE ) or America GPE , is a country primarily located in North America LOC . It consists of 50 CARDINAL states, a federal district, five CARDINAL major unincorporated territories, 326 CARDINAL Indian NORP reservations, and some minor possessions.[j] At 3.8 million square miles QUANTITY ( 9.8 million square kilometers QUANTITY ), it is the world's third- or fourth DATE -largest country by total area.[d] The United States GPE shares significant land borders with Canada GPE to the north and Mexico GPE to the south, as well as limited maritime borders with the Bahamas GPE , Cuba GPE , and Russia.[22] With a population of more than 331 million CARDINAL people, it is the third ORDINAL most populous country in the world. The national capital is Washington GPE , D.C. GPE , and the most populous city is New York GPE . Paleo-Indians NORP migrated from Siberia LOC to the North American NORP mainland at least 12,000 years ago DATE , and European NORP colonization began in the 16th century DATE . The United States GPE emerged from the thirteen CARDINAL British NORP colonies established along the East Coast LOC . Disputes over taxation and political representation with Great Britain GPE led to the American Revolutionary War ORG ( 1775Ã¢â‚¬â€œ1783 CARDINAL ), which established independence. In the late 18th century DATE , the U.S. GPE began expanding across North America LOC , gradually obtaining new territories, sometimes through war, frequently displacing Native Americans NORP , and admitting new states; by 1848 DATE , the United States GPE spanned the continent. Slavery was legal in the southern United States GPE until the second half of the 19th century DATE when the American Civil War ORG led to its abolition. The SpanishÃ¢â‚¬â€œAmerican War and World War EVENT I established the U.S. GPE as a world power, a status confirmed by the outcome of World War II EVENT .During the Cold War EVENT , the United States GPE fought the Korean War EVENT and the Vietnam War EVENT but avoided direct military conflict with the Soviet Union GPE . The two CARDINAL superpowers competed in the Space Race FAC , culminating in the 1969 DATE spaceflight that first ORDINAL landed humans on the Moon PERSON . The Soviet Union's GPE dissolution in 1991 DATE ended the Cold War EVENT , leaving the United States GPE as the world's sole superpower. The United States GPE is a federal republic and a representative democracy with three CARDINAL separate branches of government, including a bicameral legislature. It is a founding member of the United Nations ORG , World Bank ORG , International Monetary Fund ORG , Organization of American States ORG , NATO ORG , and other international organizations. It is a permanent member of the United Nations Security Council ORG . Considered a melting pot of cultures and ethnicities, its population has been profoundly shaped by centuries DATE of immigration. The country ranks high in international measures of economic freedom, quality of life, education, and human rights, and has low levels of perceived corruption. However, the country has received criticism concerning inequality related to race, wealth and income, the use of capital punishment, high incarceration rates, and lack of universal health care. The United States GPE is a highly developed country, accounts for approximately a quarter DATE of global GDP, and is the world's largest economy. By value, the United States GPE is the world's largest importer and the second ORDINAL -largest exporter of goods. Although its population is only 4.2% PERCENT of the world's total, it holds 29.4% PERCENT of the total wealth in the world, the largest share held by any country. Making up more than a third CARDINAL of global military spending, it is the foremost military power in the world; and it is a leading political, cultural, and scientific force internationally.[23]
 
Word Vectors
Important


Word vectors, or word embeddings, are numerical representations of words in multidimensional space through matrices. The purpose of the word vector is to get a computer system to understand a word. Computers cannot understand text efficiently. They can, however, process numbers quickly and well. For this reason, it is important to convert a word into a number.

## importing libraries

import spacy
!python -m spacy download en_core_web_md
Collecting en-core-web-md==3.4.1
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.4.1/en_core_web_md-3.4.1-py3-none-any.whl (42.8 MB)
     ---------------------------------------- 42.8/42.8 MB 8.2 MB/s eta 0:00:00
Requirement already satisfied: spacy<3.5.0,>=3.4.0 in c:\users\saiba\anaconda3\lib\site-packages (from en-core-web-md==3.4.1) (3.4.4)
Requirement already satisfied: srsly<3.0.0,>=2.4.3 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.4.5)
Requirement already satisfied: thinc<8.2.0,>=8.1.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (8.1.7)
Requirement already satisfied: wasabi<1.1.0,>=0.9.1 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.10.1)
Requirement already satisfied: packaging>=20.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (21.3)
Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.10 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (3.0.11)
Requirement already satisfied: pathy>=0.3.5 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.10.1)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.0.7)
Requirement already satisfied: smart-open<7.0.0,>=5.2.1 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (5.2.1)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (4.64.1)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.28.1)
Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (3.3.0)
Requirement already satisfied: setuptools in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (63.4.1)
Requirement already satisfied: numpy>=1.15.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (1.21.5)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (1.10.4)
Requirement already satisfied: typer<0.8.0,>=0.3.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.7.0)
Requirement already satisfied: jinja2 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.11.3)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (1.0.9)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (3.0.8)
Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.0.8)
Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in c:\users\saiba\anaconda3\lib\site-packages (from spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (1.0.4)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\users\saiba\anaconda3\lib\site-packages (from packaging>=20.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (3.0.9)
Requirement already satisfied: typing-extensions>=4.2.0 in c:\users\saiba\anaconda3\lib\site-packages (from pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (4.3.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\saiba\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (1.26.11)
Requirement already satisfied: charset-normalizer<3,>=2 in c:\users\saiba\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\saiba\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2022.9.14)
Requirement already satisfied: idna<4,>=2.5 in c:\users\saiba\anaconda3\lib\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (3.3)
Requirement already satisfied: confection<1.0.0,>=0.0.1 in c:\users\saiba\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.0.4)
Requirement already satisfied: blis<0.8.0,>=0.7.8 in c:\users\saiba\anaconda3\lib\site-packages (from thinc<8.2.0,>=8.1.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.7.9)
Requirement already satisfied: colorama in c:\users\saiba\anaconda3\lib\site-packages (from tqdm<5.0.0,>=4.38.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (0.4.5)
Requirement already satisfied: click<9.0.0,>=7.1.1 in c:\users\saiba\anaconda3\lib\site-packages (from typer<0.8.0,>=0.3.0->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (8.0.4)
Requirement already satisfied: MarkupSafe>=0.23 in c:\users\saiba\anaconda3\lib\site-packages (from jinja2->spacy<3.5.0,>=3.4.0->en-core-web-md==3.4.1) (2.0.1)
[+] Download and installation successful
You can now load the package via spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_md')
with open('data/wiki_us.txt', "r") as f:
    text = f.read()
Doc = nlp(text) 
sentence1 = list(Doc.sents)[0]
sentence1
The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America.
# ## find synonyms of words in PyDictionary

# from PyDictionary import PyDictionary

# dictionary = PyDictionary()

# words = ['like', 'hate']

# for word in words:
#     syns = dictionary.synonym(word)
#     print(f"{word}: {syns[0:5]}\n")
# sentence1[0].vector
Why to use WordVectors
import numpy as np


word = input()

## most similar
ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]]), n = 10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]

distances = ms[2]
print(words)
country
['country—0,467', 'nationâ\x80\x99s', 'countries-', 'continente', 'Carnations', 'pastille', 'бесплатно', 'Argents', 'Tywysogion', 'Teeters']
## Document similarity

doc1 = nlp("I am good boy.")
doc2 = nlp("I donot study for whole year.")

print(doc1, "<->", doc2, doc1.similarity(doc2))
I am good boy. <-> I donot study for whole year. 0.5653599591420513
doc3 = nlp("Google, amazon, microsoft are big tech giant.")
doc4 = nlp("All these company has started layoff.")

print(doc3, "<->", doc4, doc3.similarity(doc4))
Google, amazon, microsoft are big tech giant. <-> All these company has started layoff. 0.6975344676195314
doc5 = nlp("John likes Harleen.")
doc6 = nlp("Harleen likes John")

print(doc5, "<->", doc6, doc5.similarity(doc6))
John likes Harleen. <-> Harleen likes John 0.8435589703721093
doc7 = nlp("Write down the code of building website using HTML, CSS, JS")
doc8 = nlp("I want to write the code to build portfolio website using HTML, CSS, HS")
print(doc7, "<->", doc8, doc7.similarity(doc8))
Write down the code of building website using HTML, CSS, JS <-> I want to write the code to build portfolio website using HTML, CSS, HS 0.7628555129063627
spaCy's Pipelines
 

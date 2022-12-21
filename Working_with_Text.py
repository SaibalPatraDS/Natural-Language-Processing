## Working with Text


----------------------

text1 = "Ethics are built right into the ideals and objectives of the United Nations "


len(text1)  #length of the text

text2 = text1.split(' ') ## will return a list of words, seperating by ' '

# text2
len(text2)

text2

### List Comprehension to find specific words

------------------------

## find words which are greater than 3 letters

[w for w in text2 if len(text2)>3]

## Capitalize words in text2

[w for w in text2 if w.istitle()]

### w.istitle() will return those words which starts with capital letters but rest of the words are small

## words end with 's'

[w for w in text2 if w.endswith('s')]

### Find Unique words

--------------------

text3 = 'To be or not to be'

text4 = text3.split(' ')

len(text4)

## finding unique value

len(set(text4))

set(text4) ## unique words

'To' and 'to' are identified as different elements

## converting to lower strings

[w.lower() for w in text4]

## unique elements

set([w.lower() for w in text4])

len(set([w.lower() for w in text4])) ##length of unique elements only

### Processing Free Text


----------------------

text5 = '"Ethics are built right into the ideals and objectives of the United Nations" \
#UNSG @NY Society for Ethical Culture bit.ly/2guVelr'

text6 = text5.split(' ')

len(text6)

## finding hashtag

[w for w in text6 if w.startswith('#')]

## finding call-outs

[w for w in text6 if w.startswith('@')]

text7 = '@UN @UN_Women "Ethics are built right into the ideals and objectives of the United Nations" \
#UNSG @ NY Society for Ethical Culture bit.ly/2guVelr'

text8 = text7.split(' ')

text8

## finding hashtags

[w for w in text8 if w.startswith('#')]

## finding callouts

[w for w in text8 if w.startswith('@')]

## regex

import re

[w for w in text8 if re.search(r'@[a-zA-Z0-9_]+', w)]

[w for w in text8 if re.search(r'#[a-zA-Z0-9_]+', w)]


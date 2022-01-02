# import nltk
# from nltk.tag.stanford import StanfordNERTagger
# st = NERTagger('stanford-ner/all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')
# text = """YOUR TEXT GOES HERE"""

# for sent in nltk.sent_tokenize(text):
#     tokens = nltk.tokenize.word_tokenize(sent)
#     tags = st.tag(tokens)
#     for tag in tags:
#         if tag[1]=='PERSON': print (tag)

import spacy
from spacy.lang.en.examples import sentences 
# import spacy spacy.load('en_core_web_sm')

# NER = spacy.load("en_core_web_sm")

NER = spacy.load("en_core_web_sm")
raw_text=[['T. V. Raman',   1989,    'M.Sc. (Mathematics)', 'Computer scientist'  ,'[43]'],
['History of IITs'],['AIIMSs IIITs IIMs IISc IISERs NITs NIPERs SPAs NIDs NIFTs NISER']]


# raw_text = 'AIIMSs IIITs IIMs IISc IISERs NITs NIPERs SPAs NIDs NIFTs NISER'

# text1= NER(raw_text)
# print(text1)

new_list=[]

for i in raw_text:
    str1 = ''.join(str(e) for e in i)
    text1= NER(str1)
    for word in text1.ents:
        if(word.label_ == 'PERSON'):
            new_list.append(i);
            print(word.text,word.label_)
            break;
            
print(new_list)


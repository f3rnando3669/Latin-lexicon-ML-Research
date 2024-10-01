import re
#from lxml import etree
import xml.etree.ElementTree as ET
from xml.dom import minidom
from nltk import ngrams
from nltk.probability import FreqDist
from nltk.corpus import brown
import json

# Get all words from the Brown Corpus
brown_words = brown.words()
# Open and read the JSON file
#with open('/Users/user/Documents/LatinDict/la.nolorem.tok.latalphabetonly.v2.json', 'r') as file:
    #LatinData = json.load(file)

def DictOrg(text):
    subj = r'[/]([\w".\s]+):'
    definition = r':(.*?)►'
    Latin = r'►(\s*[\w\()\s]+)'
    source = r'¶(.*?).\s*(.*?)\.'
    adj = r'[a][d][j][.]([\w\s]+)'
    #sepereated the given data best i can
    start = "//"
    chunks = text.split(start)
    

    # Iterate through the matches and add to XML
    #trying to figure out the format to conv to TEI xml
    '''
    for i in matches:
        member = etree.SubElement(root, "member")
        member.attrib['title'] = i
    # Convert XML to string and print
    out = etree.tostring(root, pretty_print=True, encoding='unicode')
    print(out)
    '''
    root = ET.Element("root")
     # insert list element into sub elements
    for chunk in chunks:
        subject = re.findall(subj, chunk, flags=re.IGNORECASE)
        Def = re.findall(definition, chunk, flags=re.IGNORECASE)
        Latin_list = re.findall(Latin, chunk, flags=re.IGNORECASE)
        sources = re.findall(source, chunk, flags=re.IGNORECASE)
        #print(chunk,"source: ",sources)
        for i in range(len(Def)):
            # create sub element
            English_words = ET.SubElement(root, "word")
            Subject_word = ET.SubElement(English_words,"Subject")
            #Latin_word = ET.SubElement(English_words,"Latin")
            #Sources_word = ET.SubElement(English_words,"source")
                
                
            English_words.text = str(Def[i]).strip() 
            for word in Latin_list:
                Latin_word = ET.SubElement(English_words,"Latin")
                Latin_word.text = word.strip()
            Subject_word.text = str(subject[i]).strip()
            for word in sources:
                if i < len(sources):
                    Sources_word = ET.SubElement(English_words,"source")
                    Sources_word.text = str(word) 
    #tree = ET.ElementTree(root)
    # write the tree into an XML file
    xml_string = ET.tostring(root, encoding='utf-8')

      # Use minidom to pretty print the XML string
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    # Write the pretty printed XML to a file
    with open("Output.xml", "w", encoding='utf-8') as f:
        f.write(pretty_xml)
 
text = "//    GEOGRAPHICAL NAMES // /general city: King's Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.// /general city: Newcastle, Neuchâtel, Châteauneuf  ► Novum Castellum  ¶ 1771 WAY dedication page (of the county in Delaware).// /general city: Newport, Nieuwpoort  ► Neoportus, ûs m.  ¶ Graesse.  ► Neoportum, i n.  ¶ 1674 MILTON XIII. 28, of Belgian town."
text2 = '// /town names in "St".: examples of use:  to the town of Saint-Laurent  ad fanum Divi Laurentii (1652 TURS. 371)  |  from the town of Saint-Laurent  e fano Divi Laurentii (1652TURS. 372)// 2 Bengali  ► lingua Bengalica// Arctic  arcticus, a, um (Hyg.; DANTE Aqua 477; EGGER S.L. 7)  ► arctôus (SEN. in tragedies; MART. )'
text2_modified = '// /town names in "St".: examples of use:  to the town of Saint-Laurent  ► ad fanum Divi Laurentii ¶ (1652 TURS. 371)  |  from the town of Saint-Laurent   ►e fano Divi Laurentii ¶ (1652TURS. 372)// 2 Bengali  ► lingua Bengalica// Arctic  arcticus, a, um (Hyg.; DANTE Aqua 477; EGGER S.L. 7)  ► arctôus ¶ (SEN. in tragedies; MART. )'
DictOrg(text2_modified)


def N_grams(txt,word):
    words = list(txt)  # Convert to list if it's already iterable
    #word = word.strip()
    #Calculating unigram probabilities
    unigrams = ngrams(words, 1)
    fdistUnigrams = FreqDist(unigrams)
    '''for unigram, count in fdistUnigrams.items():
        probability = count / len(words)
        print(f'P({unigram[0]}) = {probability}')'''
    # Get the count of the word in corpus
    wordCount = fdistUnigrams[(word,)]
    totalWords = len(words)
    # Calculate probability
    probability = 0
    probability += wordCount / totalWords
    return probability
    #print(f'P({word}) = {probability}')




Findwords = re.findall(r'\w+[a-zA-Z]', text2)        
#LatinData1 = str(LatinData).split() 
for word in Findwords:
    if N_grams(brown_words,word) == 0:
        print(word,"prop: ",N_grams(brown_words,word))
    '''
    if word == word+1:
      continue
    else:
        prop1 = float(N_grams(brown_words,word))
        prop2 = float(N_grams(LatinData1,word))
        if prop1 < prop2:
            print(word)
        else:
            continue'''
        
    
#N_grams(text2)
#N_grams(LatinData)
#find a way to compare propability of text2 to brown corpus


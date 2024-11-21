import re
import requests
#from lxml import etree
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys

#Add the path to the folder `test.py`
sys.path.insert(0, '/Users/fernandovargas/Desktop/latinDict/Computer-Science-Research-Summer-master')
#Importing the `generate_response function from test.py
from test1 import generate_response # type: ignore
def DictOrg(text):
    subj = r'(?<=\/)[\w".\s]+'
    definition = r':(.*?)►'
    Latin = r'►(\s*[\w\()\s]+)'
    source = r'\((.*?)\)|¶(.*?).\s*(.*?)\.'
    adj = r'[a][d][j][.]([\w\s]+\.)'

    #print(listoflatin)
    #sepereated the given data best i can
    start = "//"
    chunks = text.split(start)
    root = ET.Element("root")
     # insert list element into sub elements
    for chunk in chunks:
        print(chunk)
        #cheking if the chunk is empty
        if not chunk:
            continue
        else:
            #finding the subject
            #subject = re.findall(subj, chunk, flags=re.IGNORECASE)
            #if not found through regex use gpt api
            subject = []
            #print(f'give me a one word response for a hypernym from this text: {chunk}')
            response = generate_response(f'only One-word hypernym for: {chunk}')
            subject.append(response)
            #using the same logic here
            Def = re.findall(definition, chunk, flags=re.IGNORECASE)
            #termchunk = re.findall(r'\/(.*?)►|\/(.*?)\(', chunk)
            if Def == []:
                response2 = generate_response(f'only One-word term described in text:{chunk}')
                Def.append(response2)
            #find sources
            sources = re.findall(source, chunk, flags=re.IGNORECASE)
            #in here we use a data base and find the bigram probabilities for latins words if not found through regex
            Latin_list = re.findall(Latin, chunk, flags=re.IGNORECASE)
            if Latin_list == []:
                words = re.findall(r'\b[a-zA-Z]+(?:[a-zA-Z]+)?\b', chunk)
                listoflatin = LatinwordExtractor(words)
                #poslatsource = re.findall(r'\((.*?)\)|¶(.*?).\s*(.*?)\.', listoflatin)
                #making sure we do not add a latin word from the sources
                for latinword,i in zip(listoflatin,range(len(listoflatin))):
                    if latinword in sources: # and latinword in poslatsource
                        listoflatin.remove(latinword)
                    Latin_list.append(latinword)
            adjs = re.findall(adj, chunk, flags=re.IGNORECASE)
            # if adjs == []:
            #     return None
            print("Subject:", subject)
            print("Definition:", Def)
            # print("Latin Words:", Latin_list)
            # print("Sources:", sources)
            # print("Adjectives:", adjs)
            for i in range(len(Def)):
                # create sub element
                English_words = ET.SubElement(root, "word")
                English_words.text = str(Def[i]).strip()
                adjective = ET.SubElement(English_words,"adj")
                adjective.text = str(adjs).strip()
                    # for sub_word in subject:
                if i < len(subject):
                    Subject_word = ET.SubElement(English_words,"Subject")
                    Subject_word.text = str(subject).strip()
                for lat_word ,sourc_word in zip(Latin_list,sources):
                        # if i < len(Latin_list):
                    if len(Latin_list) == len(sources):
                        Latin_word = ET.SubElement(English_words,"Latin")
                        Latin_word.text = lat_word.strip()
                        Sources_word = ET.SubElement(English_words,"source")
                        Sources_word.text = str(sourc_word) 
                else:
                    Latin_word = ET.SubElement(English_words,"Latin")
                    Latin_word.text = str(Latin_list).strip()
                    
                    Sources_word = ET.SubElement(English_words,"source")
                    Sources_word.text = str(sources)
        #tree = ET.ElementTree(root)
        # write the tree into an XML file
        xml_string = ET.tostring(root, encoding='utf-8')

        # Use minidom to pretty print the XML string
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
        
        # Write the pretty printed XML to a file
        with open("Output.xml", "w", encoding='utf-8') as f:
            f.write(pretty_xml)
 
text1 = '''//GEOGRAPHICAL NAMES 
// /general city: King's Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.
// /general city: Newcastle, Neuchâtel, Châteauneuf  ► Novum Castellum  ¶ 1771 WAY dedication page (of the county in Delaware).
// /general city: Newport, Nieuwpoort  ► Neoportus, ûs m.  ¶ Graesse.  ► Neoportum, i n.  ¶ 1674 MILTON XIII. 28, of Belgian town.'''
text2 = '''// /town names in "St".: examples of use:  to the town of Saint-Laurent ad fanum Divi Laurentii (1652 TURS. 371)  |  from the town of Saint-Laurent  e fano Divi Laurentii (1652TURS. 372)
// 2 Bengali  ► lingua Bengalica// Arctic  arcticus, a, um (Hyg.; DANTE Aqua 477; EGGER S.L. 7)  ► arctôus (SEN. in tragedies; MART. )'''
text3 = '''// 2 Bengali  ► lingua Bengalica 
// Arctic  arcticus, a, um (Hyg.; DANTE Aqua 477; EGGER S.L. 7)  ► arctôus (SEN. in tragedies; MART. )
// Arctic Ocean  Glacialis Oceanus (1811 PALLAS vi)  ► Mare Glaciale (1595 MERCATOR II " Polus Arcticus" map; 1811 PALLAS xi)
// Arctic zone  zona arctica (1811 PALLAS 52)// Arctic: Antarctic  adj.  antarcticus, a, um (EGGER D.L. 25)
// Arctic: Antarctica  terra antarctica (EGGER D.L. 25)'''
text4 = '''//1 Austria cities: Vienna  ► Vienna, ae f.  ¶ 1595 MERCATOR I, "Germaniae."  1652 TURS. 252 et passim.  1843 TRAPPEN 26.  EGGER S.L. 58, quoting Latin inscription of 16th-century coin.  ► Vindobona, ae f.  ¶ 1891 VELENOVSKÝ vi.  EGGER S.L. 57.  |  adj.  ► Viennensis, e  ¶ 1595 MERCATOR I, "Germaniae."  1652 TURS. 332.  ►► Vienna is slightly more common than Vindobona in printed books (WC).
//1 Austria regions: Carinthia  Carinthia, ae f. (1595 MERCATOR I, "Salzburg" map)
//1 Austria regions: Styria   Stiria, ae f. (1595 MERCATOR I, "Stiria")
//1 Austrian  subst.  ► Austriacus, i (1652 TURS. 314; 1784 DUCRUE 265; 1843 TRAPPEN 51; PERUGINI, Concordata 42)  |  adj.  ► Austriacus, a, um (1595 MERCATOR I, "Austria";1652 TURS. 249 et passim; PERUGINI, Concordata 33; EGGER S.L. 57)
//1 Belgium  ► Belgium, i n.  ¶ EGGER S.L. 78.  ► Belgium Meridiânum  ¶ Cf. the use of Belgium Septentrionale of the Netherlands:  Alexander Suerman, Specimen historico-medicum de cholerae Asiaticae itinere per Belgium septentrionale, annis 1832-1834 (Utrecht, 1835).    ►► The term Belgium, at least through the 18th century, refers in Latin to the Low Countries generally.'''

def LatinwordExtractor(words):
    wordsl = []
    for i in range(len(words)-1):
        word_pairs = (f"{words[i]}+{words[i+1]}")
        #print(word_pairs)
        response = requests.get(f"https://api.ngrams.dev/eng/search?query={word_pairs}&flags=cr+ep+e")
        #response = requests.get(f"https://api.ngrams.dev/eng/search?query=saint-laurent+ad")
        responsej = response.json()
        #jprint(responsej)
        unique_words = set()  # Set to store unique words

        if 'ngrams' in responsej:
            if responsej['ngrams'] == []:
                qtokens = responsej['queryTokens']
                for element in qtokens:
                    text = element['text'].strip(",")
                    if text and not text.isspace() and text not in unique_words:
                        wordsl.append(text)
    newlist = list(set(wordsl))
    return newlist

#DictOrg(text1)
#DictOrg(text2)
#DictOrg(text3)
#DictOrg(text4)
        
# #text3point5 = '// Arctic: North Pole  ► polus arcticus  ¶ DANTE Aqua 477.  1315 MARCO POLO B 3, 16.  ► polus septentrionalis  ¶ EGGER S.L. 44.   ► axis septentrionalis  ¶ EGGER S.L. 44.  ►polus glacialis  ¶ OV. M. 2, 173.   ► polus gelidus  ¶ OV. H. 18, 152.// Arctic: South Pole  polus antarcticus (APUL.; DANTE Aqua 477)  ► polus austrâlis (OV. M. 2, 131)  ► polus austrînus (PLIN. 5, 56)// Atlantic islands: Azores  ►► Tertiariae Insulae (1652 TURS. 263)// Atlantic islands: Canary Islands  ► Insulae Fortûnâtae (f. pl.)  ¶ PLIN.  1595 MERCATOR II "Europa."  1794 RUIZ viii.  ► Insulae Canariae (f. pl.)  ¶ Arn.  1595 MERCATOR II"Europa."// Atlantic islands: Canary Islands: Tenerife  ► Teneriffa, ae f.  ¶ 1794 RUIZ viii.  ► Ninguâria, ae f.  ¶ Plin. 6, 204.  Egger N.L.  ► Nivâria, ae f.  ¶ Plin. 6, 204 (variant reading). Egger N.L.// Atlantic islands: Madeira  Materia, ae f.// Atlantic Ocean  Mare Atlanticum (CIC.; 1595 MERCATOR II "Africa."  ► Oceanus Atlanticus (EGGER S.L. 34)// Eurasia  Eurôpâsia, ae f., Eurâsia, ae f.;  adj.  Eurôpâsiânus, a, um, Eurâsiânus, a, um// Pacific Ocean  Mare Pacific'
# start = "//"
# chunks = text3.split(start)
# for chunk in chunks:
#     short = r'\/(.*?)\('
#     match = re.search(short, chunk)
#     if match:
#         print(match.group(1))  # Print only the matched text

    #print(termchunk)

response = generate_response(f'only One-word hypernym for: ///general city: King\'s Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.')
print(response)
        

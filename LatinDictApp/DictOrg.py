import re
import requests
#from lxml import etree
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys

#Add the path to the folder `test.py`
sys.path.insert(0, '/Users/fernandovargas/Desktop/latinDict/Computer-Science-Research-Summer-master/MachineLearningSummer/clean_space')
#Importing the `generate_response function from test.py
from test import generate_response # type: ignore
def DictOrg(text):
    subj = r'(?<=\/)[\w".\s]+'
    term = r':(.*?)►'
    Latin = r'►(\s*[\w\()\s]+)|►(\s*[\w\()\s]+)\,'
    source = r'\(([^)]{2,})\)|¶\s*([^\n►]+)'
    adj = r'[a][d][j][.]([\w\s]+\.)'

    #print(listoflatin)
    #sepereated the given data best i can
    start = "//"
    chunks = text.split(start)
    root = ET.Element("root")
     # insert list element into sub elements
    for chunk in chunks:
        #cheking if the chunk is empty
        chunk = chunk.strip()
        if not chunk or chunk == "GEOGRAPHICAL NAMES" :
            continue
        else:
            #finding the subject
            subject = re.findall(subj, chunk, flags=re.IGNORECASE)
            #if not found through regex use gpt api
            if not subject:
            #print(f'give me a one word response for a hypernym from this text: {chunk}')
                response = generate_response(f'give only One-word hypernym for: {chunk}')
                subject.append(response)
            #using the same logic here


            Term = re.findall(term, chunk, flags=re.IGNORECASE)
            #termchunk = re.findall(r'\/(.*?)►|\/(.*?)\(', chunk)
            if Term == []:
                response2 = generate_response(f'give only the word term described in Def or text:{chunk}')
                Term.append(response2)


            #find sources
            # Perform regex matching
            sources = re.findall(source, chunk)
            print("Source found using regex:", sources)
            sources = ["".join(x) for x in sources if any(x)]  # `any(x)` ensures we don't include empty tuples
            print("Flattened and filtered sources:", sources)
            sourcenew = re.findall(r'\b[a-zA-Z]+(?:[a-zA-Z]+)?\b', str(sources))

            # Filter out tuples where both elements are empty
            # filtered_sources = [tup for tup in sources if str(tup[0]).strip(',') or str(tup[1]).strip(',')]
            # print("Filtered sources:", filtered_sources)

            #in here we use a data base and find the bigram probabilities for latins words if not found through regex
            Latin_list = re.findall(Latin, chunk, flags=re.IGNORECASE)
            print("prev latin word ", Latin_list,"\n")
            filtered_words = []
            for lat in Latin_list:
                if "(" in lat[0]:
                    print("has paranthesis:",lat)
                    filt_list = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', lat[0])
                    print("filtered list", filt_list)
                    for word in filt_list:
                        print("word:",word)
                        if word not in sourcenew:
                            print("word ",word,"not in",sourcenew)
                            filtered_words.append(word)
                            print("words found:",filtered_words)
                            Latin_list = [" ".join(filtered_words)]
                else: 
                    Latin_list = ["".join(x) for x in Latin_list if any(x)]
            print("comtinued" ,Latin_list)

            # Latin_list = [item[0].replace('(', '').replace(')', '').strip() for item in Latin_list]
            # print("getting rid of parathesis",Latin_list)
            # for item in Latin_list:
            #     print("item:",item.split())
            #     for word in item.split():
            #         print("word",word,"not in",sources)
            #         if word not in sources:
            #             Latin_list = ["".join(word)]

            print("latin list as is without extractor function:", Latin_list)


            #print("latin wirds found using regex: ",Latin_list)
            if Latin_list == []:
                sourcenew = re.findall(r'\b[a-zA-Z]+(?:[a-zA-Z]+)?\b', str(sources))
                listoflatin = []
                if "|" in chunk:
                    newchunk = chunk.split("|")
                    for part in newchunk:
                        #print("the part:", part)
                        part = re.findall(r'\b[a-zA-Z]+(?:[a-zA-Z]+)?\b', part)
                        newlatinwords = LatinwordExtractor(part)
                        listoflatin.append([word for word in newlatinwords if word not in sourcenew and word not in ["adj", "um","Laurent",","]])
                        # print("what we get per part: ",newlatinwords)
                        # listoflatin = ["".join(word) for word in newlatinwords]
                    print("what we get when we join: ",listoflatin) 
                else:      
                    words = re.findall(r'\b[a-zA-Z]+(?:[a-zA-Z]+)?\b', chunk)
                    listoflatin = LatinwordExtractor(words)
                    listoflatin = [word for word in listoflatin if word not in sourcenew and word not in ["adj", "um","Laurent",","]]

                    #print("latin list without the split: ",listoflatin)
                #print("latin list out of loop: ",listoflatin) 
                #making sure we do not add a latin word from the sources
                # for latinword in listoflatin:
                #     print("latin word here ",latinword)
                #     print("comparing if its in here:",sourcenew)
                #     if latinword in sourcenew or latinword == "adj" or latinword == "um": # and latinword in poslatsource
                #         print("removed this: ",latinword)
                #         listoflatin.remove(latinword)
                #     else:
                #         Latin_list.append(latinword)
                print("list of latin words",listoflatin)
                for latinwords in listoflatin:
                    Latin_list.append(latinwords)
                print("end result of using latin word extractor",Latin_list)
                Latin_list = [word for word in Latin_list if word not in sources]
            print("latin list as is without extractor function: ",Latin_list)

            adjs = re.findall(adj, chunk, flags=re.IGNORECASE)

            for i in range(len(Term)):
                # create sub element
                English_words = ET.SubElement(root, "word")
                English_words.text = str(Term[i]).strip()

                adjective = ET.SubElement(English_words,"adj")
                adjective.text = adjs[0] if adjs else "None"


                    # for sub_word in subject:
                if i < len(subject):
                    Subject_word = ET.SubElement(English_words,"Subject")
                    Subject_word.text = str(subject).strip("[]")
                    #print("Subject: ",Subject_word.text

                if len(Latin_list) == len(sources):
                    for lat_word ,sourc_word in zip(Latin_list,sources):
                            Latin_word = ET.SubElement(English_words,"Latin")
                            Latin_word.text = str(lat_word).strip("[]")
                            print("latin word: ",Latin_word.text)

                            # Create source entry
                            Sources_word = ET.SubElement(English_words, "source")
                            Sources_word.text = str(sourc_word).strip()
                else:
                    Latin_word = ET.SubElement(English_words, "Latin")
                    Latin_word.text = str(Latin_list).strip("[]")
                    print("latin word: ", Latin_word.text)

                    Sources_word = ET.SubElement(English_words, "source")
                    if sources == []:  # If no source, set it to "None"
                         Sources_word.text = "None"
                    else:
                        Sources_word.text = str(sources).strip("[]")
                    #print("Source ", Sources_word.text, "\n")
            
        #tree = ET.ElementTree(root)
        # write the tree into an XML file
        xml_string = ET.tostring(root, encoding='utf-8')

        # Use minidom to pretty print the XML string
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
        print(checkxml(pretty_xml,chunk))
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
alltext = text1+text2+text3+text4
def checkxml(xml,text):
    check = generate_response(f'check if the xml format {xml} correctly matches {text}, if it does print yes, else fix the xml and only print that')
    for word in check:
        if "yes" in word:
            continue
        else:
            print(check)


def LatinwordExtractor(words):
    wordsl = []
    unique_words = set()  # Set to store unique words
    for i in range(len(words)-1):
        word_pairs = (f"{words[i]}+{words[i+1]}")
        #print(word_pairs)
        response = requests.get(f"https://api.ngrams.dev/eng/search?query={word_pairs}&flags=cr+ep+e")
        #response = requests.get(f"https://api.ngrams.dev/eng/search?query=saint-laurent+ad")
        responsej = response.json()

        if 'ngrams' in responsej:
            if responsej['ngrams'] == []:
                qtokens = responsej['queryTokens']
                for element in qtokens:
                    text = element['text'].strip(",")
                    if text and not text.isspace() and text not in unique_words:
                        unique_words.add(text)
                        wordsl.append(text)
    #print(unique_words)
    newlist = list(wordsl)
    return newlist
ex = '// Arctic Ocean  Glacialis Oceanus (1811 PALLAS vi)  ► Mare Glaciale (1595 MERCATOR II " Polus Arcticus" map; 1811 PALLAS xi)'
ex2 = "//21 Black Sea: Aegean Sea  ► mare Aegaeum  ¶  ► Aegaeopelagus, i m.  ¶ OED s.v. archipelago in etymological note, citing medieval sources.  ► Archipelagus, i m.  ¶ OED s.v.archipelago in etymological note, citing 13th c. treaty.  Bondelmontius 53: \"mare Archipelagi.\"  Linné Species 2, 794: \"Habitat ad Archipelagum.\"  Bentley 2, 603-04 (on Manil. 4, 617): \"Propontis illud est mare quod Archipelagum inter et Pontum Euxinum iacet.\"  C. G. Heyne, Variae lectiones et observationes in Iliadem (Leipzig, 1802), v. 2, pt. 3, p.180, discussing  βορέης  in the Iliad: \"Sub illud tempus per totum Archipelagum aquilones spirant.\"  1807 Sprengel 1, 377: \"Per tres annos Graeciam, Archipelagum, Asian Minorem, Syriam et Aegyptum perquisivit."
# DictOrg(text1)

with open('/Users/fernandovargas/Desktop/latinDict/LatinDictApp/Geo_input.txt', 'r') as file:
    content = file.read()
DictOrg(content)

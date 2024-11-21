

# def N_grams(txt,word):
#     words = list(txt)  # Convert to list if it's already iterable
#     #word = word.strip()
#     #Calculating unigram probabilities
#     unigrams = ngrams(words, 1)
#     fdistUnigrams = FreqDist(unigrams)
#     # Get the count of the word in corpus
#     wordCount = fdistUnigrams[(word,)]
#     totalWords = len(words)
#     # Calculate probability
#     probability = 0
#     probability += wordCount / totalWords
#     return probability
#     #print(f'P({word}) = {probability}')  
# def prop_bigram(txt, word_pair): #list_of_latin_words
#     words = word_tokenize(str(txt))
#     bigrams = list(ngrams(words, 2))
#     #valid_bigrams = [bg for bg in bigrams if bg[0] in list_of_latin_words and bg[1] in list_of_latin_words]
#     fdistBigrams = FreqDist(bigrams)
#     totalBigrams = len(bigrams)
#     # Count the occurrences of the word_pair in valid bigrams
#     wordCount = fdistBigrams[word_pair]
#     probability = wordCount/ totalBigrams if totalBigrams > 0 else 0
#     return probability
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def DictOrg(text):
    # Adjusted regex patterns
    subj = r'\/([\w".\s]+)' 
 # Matches subject until the colon before examples
    definition = r':\s*(.*?)\s*►'  # Matches the definition section up to "►"
    Latin = r'►\s*([^\(]+?)\s*(?=\(|$)'  # Captures Latin words without parentheses
    source = r'\((.*?)\)'  # Matches sources enclosed in parentheses
    adj = r'adj\.\s*([\w\s]+)'  # Matches adjectives after "adj."

    # Split text by `//` to parse sections
    sections = text.split('//')
    root = ET.Element("root")
    
    for section in sections:
        subject_match = re.findall(subj, section)
        definition_match = re.findall(definition, section)
        latin_match = re.findall(Latin, section)
        sources_match = re.findall(source, section)
        adj_match = re.findall(adj, section)
        
        # Debugging print statements
        print("Subject:", subject_match)
        print("Definition:", definition_match)
        print("Latin Words:", latin_match)
        print("Sources:", sources_match)
        print("Adjectives:", adj_match)

        # Create XML structure if any matches are found
        if subject_match or definition_match or latin_match or sources_match:
            word_element = ET.SubElement(root, "word")
            
            if subject_match:
                subj_element = ET.SubElement(word_element, "Subject")
                subj_element.text = subject_match[0].strip()

            if definition_match:
                def_element = ET.SubElement(word_element, "Definition")
                def_element.text = definition_match[0].strip()

            if latin_match:
                latin_element = ET.SubElement(word_element, "Latin")
                latin_element.text = ", ".join(latin_match).strip()

            if sources_match:
                sources_element = ET.SubElement(word_element, "Sources")
                sources_element.text = ", ".join(sources_match).strip()

            if adj_match:
                adj_element = ET.SubElement(word_element, "Adjective")
                adj_element.text = adj_match[0].strip()

    # Convert XML to a pretty-printed string
    xml_string = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    with open("Output.xml", "w", encoding='utf-8') as f:
        f.write(pretty_xml)

# Test with text2
text2 = '// /town names in "St".: examples of use: to the town of Saint-Laurent ad fanum Divi Laurentii (1652 TURS. 371) | from the town of Saint-Laurent e fano Divi Laurentii (1652TURS. 372)// 2 Bengali ► lingua Bengalica// Arctic arcticus, a, um (Hyg.; DANTE Aqua 477; EGGER S.L. 7) ► arctôus (SEN. in tragedies; MART. )'
DictOrg(text2)

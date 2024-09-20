import re
#from lxml import etree
import xml.etree.ElementTree as ET
def DictOrg():
    text = "//    GEOGRAPHICAL NAMES // /general city: King's Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.// /general city: Newcastle, Neuchâtel, Châteauneuf  ► Novum Castellum  ¶ 1771 WAY dedication page (of the county in Delaware).// /general city: Newport, Nieuwpoort  ► Neoportus, ûs m.  ¶ Graesse.  ► Neoportum, i n.  ¶ 1674 MILTON XIII. 28, of Belgian town."
    title = r'/([\w\s]+):'
    definition = r':(.*?)►'
    Latin = r'►\s*([\w\(\)]+(?:\s*\w+)*)'
    source = r'¶(.*?).\s*(.*?)\.'
    #sepereated the given data best i can
    subject = re.findall(title, text, flags=re.IGNORECASE)
    Def = re.findall(definition, text, flags=re.IGNORECASE)
    Latin_list = re.findall(Latin, text, flags=re.IGNORECASE)
    sources = re.findall(source, text, flags=re.IGNORECASE)
   #Create XML root
    #root = etree.Element('root')

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
    for i in range(len(Def)):
     # we make root element
        root = ET.Element("root")
 
        # insert list element into sub elements
        for i in range(len(Def)):
            # create sub element
            English_words = ET.SubElement(root, "word")
            Latin_word = ET.SubElement(English_words,"Latin")
            Subject_word = ET.SubElement(English_words,"Subject")
            Sources_word = ET.SubElement(English_words,"source")
            
            
            English_words.text = str(Def[i]) 
            Latin_word.text = str(Latin_list[i])
            Subject_word.text = str(subject[i])
            Sources_word.text = str(sources[i])
      
        tree = ET.ElementTree(root)
        # write the tree into an XML file
        tree.write("Output.xml", encoding ='utf-8', xml_declaration = True)
        
 

DictOrg()
#rescources: https://stackoverflow.com/questions/39029570/saving-list-of-tuples-in-xml
#https://regex101.com/r/nI18g9/1
'''           
        for i in range(len(Def)):
            usr2 = ET.SubElement(usrconfig, "type")
            usr2.text = str(Def[i])
        for i in range(len(matches3)):
            usr3 = ET.SubElement(usrconfig, "type")
            usr3.text = str(matches3[i])
        for i in range(len(Latin_list)):
            usr4 = ET.SubElement(usrconfig, "type")
            usr4.text = str(Latin_list[i])
        for i in range(len(scources)):
            usr5 = ET.SubElement(usrconfig, "type")
            usr5.text = str(scources[i])
        '''
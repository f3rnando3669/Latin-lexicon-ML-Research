import re
#from lxml import etree
import xml.etree.ElementTree as ET
def DictOrg():
    text = "//    GEOGRAPHICAL NAMES // /general city: King's Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.// /general city: Newcastle, Neuchâtel, Châteauneuf  ► Novum Castellum  ¶ 1771 WAY dedication page (of the county in Delaware).// /general city: Newport, Nieuwpoort  ► Neoportus, ûs m.  ¶ Graesse.  ► Neoportum, i n.  ¶ 1674 MILTON XIII. 28, of Belgian town."
    title = r'/([\w\s]+):'
    Def = r':(.*?)►'
    rest = r'►(.*?).\/'
    Latin = r'►\s*([\w\(\)]+(?:\s*\w+)*)'
    sources = r'¶(.*?).\s*(.*?)\.'
    #sepereated the given data best i can
    matches = re.findall(title, text, flags=re.IGNORECASE)
    matches2 = re.findall(Def, text, flags=re.IGNORECASE)
    matches3 = re.findall(rest, text, flags=re.IGNORECASE)
    matches4 = re.findall(Latin, text, flags=re.IGNORECASE)
    matches5 = re.findall(sources, text, flags=re.IGNORECASE)
   # Create XML root
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
    for i in matches:
     # we make root element
        usrconfig = ET.Element("root")
 
        # create sub element
        usrconfig = ET.SubElement(usrconfig, "div")
 
        # insert list element into sub elements
        for user in range(len( matches)):
            usr = ET.SubElement(usrconfig, "type")
            usr.text = str(matches[user])       
        for i in range(len(matches2)):
            usr2 = ET.SubElement(usrconfig, "type")
            usr2.text = str(matches2[i])
        for i in range(len(matches3)):
            usr3 = ET.SubElement(usrconfig, "type")
            usr3.text = str(matches3[i])
        for i in range(len(matches4)):
            usr4 = ET.SubElement(usrconfig, "type")
            usr4.text = str(matches4[i])
        for i in range(len(matches5)):
            usr5 = ET.SubElement(usrconfig, "type")
            usr5.text = str(matches5[i])
 
        tree = ET.ElementTree(usrconfig)
 
        # write the tree into an XML file
        tree.write("Output.xml", encoding ='utf-8', xml_declaration = True)
        
 

DictOrg()
#rescources: https://stackoverflow.com/questions/39029570/saving-list-of-tuples-in-xml
#https://regex101.com/r/nI18g9/1

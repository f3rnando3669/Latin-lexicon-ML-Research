import re
from lxml import etree
def DictOrg():
    text = "//    GEOGRAPHICAL NAMES // /general city: King's Mountain, Königsberg, Monterrey, Montréal  ► Regi(o)montium, i n.// /general city: Newcastle, Neuchâtel, Châteauneuf  ► Novum Castellum  ¶ 1771 WAY dedication page (of the county in Delaware).// /general city: Newport, Nieuwpoort  ► Neoportus, ûs m.  ¶ Graesse.  ► Neoportum, i n.  ¶ 1674 MILTON XIII. 28, of Belgian town."
    title = r'/([\w\s]+):'
    Def = r':(.*)►'
    rest = r'►(.*)'
    #sepereated the given data best i can
    matches = re.findall(title, text, flags=re.IGNORECASE)
    matches2 = re.findall(Def, text, flags=re.IGNORECASE)
    matches3 = re.findall(rest, text, flags=re.IGNORECASE)
   # Create XML root
    root = etree.Element('root')

    # Iterate through the matches and add to XML
    #trying to figure out the format to conv to TEI xml
    for i in matches:
        member = etree.SubElement(root, "member")
        member.attrib['title'] = i
    # Convert XML to string and print
    out = etree.tostring(root, pretty_print=True, encoding='unicode')
    print(out)


DictOrg()
#rescources: https://stackoverflow.com/questions/39029570/saving-list-of-tuples-in-xml
#https://regex101.com/r/nI18g9/1

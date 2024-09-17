from requests_html import HTMLSession
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# List of letters to iterate through
'''letters = [ '#a','#b','#c','#d','#e','#f','#g','#h','#i',
            '#j','#k','#l','#m','#n','#o','#p','#q','#r','#s','#t','#u','#v','#w','#x','#y','#z']'''
session = HTMLSession()
list_words = []
list_url = []

#for letter in letters:
url = f'https://neolatinlexicon.org/latin'
response = session.get(url)
    # Check for successful access of url
if response.status_code == 200:
    print('Successfull')
    soup = BeautifulSoup(response.html.html, 'html.parser')
    #get words from neolexicon latin list
    words = soup.select('div.d-md-flex.justify-content-center a')
    for word in words:
        word_text = word.get_text(strip=True)
        word_url = word.get('href')
        #print(word_text)
        list_words.append(word_text)
        list_url.append(word_url)   
    #print (list_words)
    #print(list_url)
        definition_url = f'https://neolatinlexicon.org{word_url}' 
        definition_response = session.get(definition_url)
        if definition_response.status_code == 200:
            print(f'Fetching definition for: {word_text}')
            definition_soup = BeautifulSoup(definition_response.html.html, 'html.parser')            
        
            definition = definition_soup.select_one('div.sense-header strong')
            if definition:            
                print(f'{word_text}: {definition.get_text(strip=True)}')
            else:
                print(f'No definition found for, {word_text}')
        else:
                print(f'Failed to reach website')     
       
            
const fs = require('fs');
const { DOMParser } = require('xmldom'); // Import the DOMParser

// Read the XML file
fs.readFile('output.xml', 'utf-8', (err, data) => {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }

  // Parse the XML file
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(data, 'text/xml');

  // Example: Get all <tagName> elements
  const tagElements = xmlDoc.getElementsByTagName('tagName'); // Replace 'tagName' with actual tags

  // Log each tag and its text content
  for (let i = 0; i < tagElements.length; i++) {
    console.log(`${tagElements[i].tagName}: ${tagElements[i].textContent}`);
  }
});

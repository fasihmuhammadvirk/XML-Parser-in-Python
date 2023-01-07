import xml.etree.ElementTree as ET
import csv 

# Parse the XML file
tree = ET.parse('compiler.xml')
root = tree.getroot()

try:
    
    # Open the CSV file in write mode
    with open('compiler.csv', 'w', newline='') as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['book_id', 'author_name', 'title', 'genre', 'price', 'publish_date', 'description'])

        # Write the data rows
        for book in tree.findall('book'):
            book_id = book.get('id')
            author_name = book.find('author').text
            title = book.find('title').text
            genre = book.find('genre').text
            price = book.find('price').text
            publish_date = book.find('publish_date').text
            description = book.find('description').text
            writer.writerow([book_id, author_name, title, genre, price, publish_date, description])

except:
    
    print("Unexpected Error Occur")
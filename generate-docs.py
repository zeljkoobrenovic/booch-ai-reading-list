import json
import datetime

books = json.load(open('data/books.json'))
template = open('templates/books.html').read()

dateString = datetime.date.today().strftime('%Y-%m-%d')
content = template.replace('${date}', dateString).replace('${data}', json.dumps(books['data']))

with open('docs/index.html', 'w') as html_file:
    html_file.write(content.replace("class=\"hidden", ""))

import csv


def html_tag(tag):

    def wrapper(text, indentation_with_tab=False):
        if indentation_with_tab:
            text = text.split('\n')
            text = '\n\t'.join(text)
            return "<{0}>\n\t{1}\n</{0}>".format(tag, text)
        
        return "<{0}>{1}</{0}>".format(tag, text)

    return wrapper

def csv_to_html(file_path):

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        fieldnames = csv_reader.fieldnames

        th = html_tag('th')
        header = []
        for field in fieldnames:
            header.append(th(field))
        
        header = ''.join(header)

        td = html_tag('td')
        rows = []
        for line in csv_reader:
            row = []
            for field in line:
                row.append(td(line[field]))
            
            row = ''.join(row)
            rows.append(row)
        
        tr = html_tag('tr')
        table_rows = []
        table_rows.append(tr(header))
        for row in rows:
            table_rows.append(tr(row))
        
        table_rows = '\n'.join(table_rows)

        table_tag = html_tag('table')
        table = table_tag(table_rows, indentation_with_tab=True)

        body_tag = html_tag('body')
        body = body_tag(table, indentation_with_tab=True)

        htmltag = html_tag('html')
        html = htmltag(body, indentation_with_tab=True)

    with open('sample.html', 'w') as html_file:
        html_file.write(html)

csv_to_html('sample.csv')
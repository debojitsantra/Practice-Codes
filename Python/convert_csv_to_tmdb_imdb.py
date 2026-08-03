import csv
import requests
import time

OMDB_API_KEY = ''

def get_imdb_id(title, year):
    url = 'http://www.omdbapi.com/'
    params = {'apikey': OMDB_API_KEY, 't': title, 'y': str(year), 'type': 'movie'}
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get('Response') == 'True' and data.get('imdbID'):
            return data['imdbID']
    except Exception:
        pass
    return ''

input_filename = 'watched.csv'
output_filename = 'tmdb_importable.csv'

with open(input_filename, encoding='utf-8') as infile, \
     open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Type', 'IMDb', 'Name', 'Release Date']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        title = row.get('Name', '').strip()
        year = row.get('Year', '').strip()
        imdb_id = get_imdb_id(title, year)
        release_date = f'{year}-01-01' if year else ''
        writer.writerow({
            'Type': 'movie',
            'IMDb': imdb_id,
            'Name': title,
            'Release Date': release_date
        })
        time.sleep(0.2)  

print(f'Conversion complete. Output saved as {output_filename}')

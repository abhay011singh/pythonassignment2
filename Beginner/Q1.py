import requests
import csv

API_KEY = '1e64d9d7'  # <-- Corrected API key here
BASE_URL = 'https://www.omdbapi.com/'


def get_movie_data(title):
    params = {
        't': title,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print(f"DEBUG: API response for '{title}': {data}")  # Debug line to see API response

    if data['Response'] == 'True':
        return {
            'Title': data.get('Title'),
            'Year': data.get('Year'),
            'Genre': data.get('Genre'),
            'Director': data.get('Director'),
            'imdbRating': data.get('imdbRating'),
            'Plot': data.get('Plot'),
            'Language': data.get('Language'),
            'Country': data.get('Country')
        }
    else:
        print(f"❌ Title not found or error: '{title}'")
        return None

def save_to_csv(movie_list, filename='movie_data.csv'):
    if not movie_list:
        print("No valid movie data to save.")
        return

    keys = movie_list[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(movie_list)
    print(f"✅ Data saved to {filename}")

def main():
    user_input = input("Enter movie/series titles (comma-separated): ")
    titles = [t.strip() for t in user_input.split(',')]

    all_data = []

    for title in titles:
        data = get_movie_data(title)
        if data:
            print(f"🎬 {data['Title']} ({data['Year']})")
            all_data.append(data)

    save_to_csv(all_data)

if __name__ == '__main__':
    main()

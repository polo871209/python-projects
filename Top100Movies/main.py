from bs4 import BeautifulSoup
import requests

site_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
res = requests.get(site_url)
soup = BeautifulSoup(res.text, 'lxml')
all_movies = soup.find_all(name='h3', class_='title')
movies_lst = []

for movie in all_movies:
    data = movie.getText().replace(')', '.')
    movies_lst.append(data)


def main():
    for movie in movies_lst[::-1]:
        with open('top100_movies.txt', mode='a') as f:
            f.write(f'{movie}\n')


if __name__ == '__main__':
    main()

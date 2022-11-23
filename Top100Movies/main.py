from bs4 import BeautifulSoup
import requests

site_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
res = requests.get(site_url)
soup = BeautifulSoup(res.text, 'lxml')
all_movies = soup.find_all(name='h3', class_='title')


movies_lst = [movie.getText().replace(')', '.')
              for movie in all_movies[::-1]]


def main():
    for movie in movies_lst:
        with open('top100_movies.txt', mode='a') as f:
            f.write(f'{movie}\n')


if __name__ == '__main__':
    main()

# Scraping top 100 movies

**Scraping data using beaitiful soup**

**[100 Greatest Movies Of All Time](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/ "100 Greatest Movies Of All Time")**

**This are only quick note for beautiful soup, Will update a much complete project in the future**

## Results
Output file as follow
```
1. The Godfather
2. The Empire Strikes Back
3. The Dark Knight
.
.
.
98. Amelie
99. Raging Bull
100. Stand By Me
```

### Get HTML from site
```python
site_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
res = requests.get(site_url)
```
### Read from soup
```python
# pip install lxml to install lxml parser
soup = BeautifulSoup(res.text, 'lxml')
all_movies = soup.find_all(name='h3', class_='title')
```
### Get all movie text
```python
movies_lst = [movie.getText().replace(')', '.')
              for movie in all_movies[::-1]]
```
### Write file
```python
def main():
    for movie in movies_lst[::-1]:
        with open('top100_movies.txt', mode='a') as f:
            f.write(f'{movie}\n')


if __name__ == '__main__':
    main()
```
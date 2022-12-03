import datetime
import database

welcome = "Welcome to the watchlist app!"
menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection: """


def add_movie_prompt():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, '%d-%m-%Y')
    timestamp = parsed_date.timestamp()
    database.add_movies(title, timestamp)


def print_movie_list(heading, movies):
    print(f'\n---{heading} movies---')
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        date = movie_date.strftime('%b %d %Y')
        print(f"{_id}: {title} (on {date})")
    print('\n')


def watched_movie_prompt():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def show_watched_movie_prompt():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("That user had no watched movies.")


def add_user_prompt():
    new_user = input("New user: ")
    database.add_user(new_user)


def search_movie_prompt():
    search_term = input("Enter partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Found", movies)
    else:
        print("No such movie")


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "8":
    if user_input == "1":
        add_movie_prompt()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list('Upcoming', movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list('All', movies)
    elif user_input == "4":
        watched_movie_prompt()
    elif user_input == "5":
        show_watched_movie_prompt()
    elif user_input == "6":
        add_user_prompt()
    elif user_input == "7":
        search_movie_prompt()
    else:
        print("\nInvalid input, please try again!\n")

import datetime

movies = {}

def add_a_movie(movie_name):
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    movie_setup = {
        "date": current_date,
        "time": current_time,
        "name": movie_name,
        "ratings": []
    }
    movies[movie_name] = movie_setup
    print(f"'{movie_name}' added! successfully")

def rate_a_movie(movie_dict, movie_name, rating):
    if movie_name in movie_dict:
        movie_dict[movie_name]["ratings"].append(rating)
        print(f"Rating {rating} added to '{movie_name}'!")
    else:
        print("Movie not found.")

def view_average_ratings(movie_dict, movie_name):
    if movie_name in movie_dict:
        ratings = movie_dict[movie_name]["ratings"]
        if ratings:
            average = sum(ratings) / len(ratings)
            print(f"Average rating for '{movie_name}' is: {average}")
        else:
            print(f"'{movie_name}' has no ratings yet.")
    else:
        print("Movie not found.")

def view_movies(movie_dict):
    if not movie_dict:
        print("Movies is empty.")
    else:
        for movie in movie_dict.values():
            print(f"Movie: {movie['name']}, Added on: {movie['date']} at {movie['time']}")

def display():
    print("""
Welcome to Olamide Movie Rating App
1. Add movie
2. View Movie
3. Rate a movie
4. View Average Ratings
5. Exit
""")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        display()
        return

    match choice:
        case 1:
            movie_name = input("Enter movie name: ")
            add_a_movie(movie_name)
        case 2:
            view_movies(movies)
        case 3:
            movie_name = input("Enter movie name to rate: ")
            try:
                rating = int(input("Enter rating (1-5): "))
                if 1 <= rating <= 5:
                    rate_a_movie(movies, movie_name, rating)
                else:
                    print("Rating must be between 1 and 5.")
            except ValueError:
                print("Invalid rating.")
        case 4:
            movie_name = input("Enter movie name to view average rating: ")
            view_average_ratings(movies, movie_name)
        case 5:
            print("Exiting...")
            return
        case _:
            print("Invalid choice.")

    display()
display()
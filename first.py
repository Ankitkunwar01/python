
movies = []


num_movies = int(input("How many movies would you like to add? "))

for i in range(num_movies):
    movie_name = input(f"Enter the name of movie {i+1}: ")
    movies.append(movie_name)

print("\nList of movies you entered:")

for i, movie in enumerate(movies,start=1):
    
    print(f"{i}.{movie}")

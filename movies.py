movies = []

# num= input("enter the name of 3 movies")

while True:
    movie = input("enter movie 3 name (you enter 3 movie name write 'done')  ")
    movies.append(movie)
    if movie.lower() == 'done':
        movies.pop()
        break
    
    # num+=1
print("List of movies name")
for name in movies:
    print(name)
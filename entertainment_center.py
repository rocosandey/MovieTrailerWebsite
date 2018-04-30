from media import Movie
from ud036_StarterCode.fresh_tomatoes import open_movies_page

# Instantiate 4 movie objects from the Movie class
pulp_fiction = Movie("Pulp Fiction","https://pics.filmaffinity.com/Pulp_Fiction-210382116-large.jpg","https://www.youtube.com/watch?v=s7EdQ4FqbhY")
snatch = Movie("Snatch","https://pics.filmaffinity.com/snatch-921179475-large.jpg","https://www.youtube.com/watch?v=9Jar2XkBboo")
casino = Movie("Casino","https://pics.filmaffinity.com/casino-827783261-large.jpg", "https://www.youtube.com/watch?v=EJXDMwGWhoA")
full_metal_jacket = Movie("Full Metal Jacket","https://pics.filmaffinity.com/full_metal_jacket-577943737-large.jpg","https://www.youtube.com/watch?v=x9f6JaaX7Wg")

# Group all movies in a list
list_of_movies = [pulp_fiction,snatch,casino,full_metal_jacket]

# Call open_movies_page function to create html page
open_movies_page(list_of_movies)


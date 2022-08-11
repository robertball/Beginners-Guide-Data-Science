import imdb

imdb_obj = imdb.IMDb()
with open("movies.csv", "w") as f:
    start_id = 88763  # start with 'Back to the Future'
    total_movies = 50000  # the number of movies you want
    count = 0  # how many movies so far
    id = start_id  # the current IMDB id
    print("IMDB_id,title,year,stars,rating,genres,plot")
    f.write("IMDB_id,title,year,stars,rating,genres,plot\n")
    while count < total_movies:
        try:
            movie = imdb_obj.get_movie(id)
            genres_string = ';'.join(movie['genres'])  # convert the list into a semicolon-separated list
            first_plot = movie['plot'][0].replace('"', "'")  # get the first plot returned. Sometimes there are many. Also, relace all double quotes with a single quote.
            certificates = movie['certificates']
            certificate_rating = ''
            for certificate in certificates:
                if "United States" in certificate and "TV" not in certificate:
                    certificate_rating = certificate.split(':')[1]
            # this skips any movie that does not have a rating in the United States (e.g., G,PG,PG-13, etc.) It also skip TV ratings.
            if certificate_rating == '':
                continue  
            print(f'{id},"{movie["title"]}",{movie["year"]},{movie["rating"]},{certificate_rating},{genres_string},"{first_plot}"')  # this line is so that you can follow the progress.
            f.write(f'{id},"{movie["title"]}",{movie["year"]},{movie["rating"]},{certificate_rating},{genres_string},"{first_plot}"\n')
            count += 1  # only increment count if all parts of the movie that we want are found
        except:
            continue  # if there is any error then skip this movie
        finally:
            id += 1  # move to the next movie no matter what


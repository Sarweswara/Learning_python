import json

def write_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_movie(file_path, movie):
    channel = read_from_json(file_path)
    channel["Channel"]["movies"].append(movie)
    write_to_json(file_path, channel)

def read_movie(file_path, title):
    channel = read_from_json(file_path)
    movies = channel["Channel"]["movies"]
    for movie in movies:
        if movie["title"] == title:
            return movie
    return None

def update_movie(file_path, title, updated_info):
    channel = read_from_json(file_path)
    movies = channel["Channel"]["movies"]
    for movie in movies:
        if movie["title"] == title:
            movie.update(updated_info)
            write_to_json(file_path, channel)
            return True
    return False

def delete_movie(file_path, title):
    channel = read_from_json(file_path)
    movies = channel["Channel"]["movies"]
    for i, movie in enumerate(movies):
        if movie["title"] == title:
            del movie[i]
            write_to_json(file_path, channel)
            return True
    return False

# Sample usage:
if __name__ == "__main__":
    file_path = 'movies.json'
    
    # Create a new movie
    new_movie = {"title": "Telugu Movie10 ", "director": "Director5", "year": 2024}
    create_movie(file_path, new_movie)
    
    # Read a new movie
    print(read_movie(file_path, "Telugu Movie3"))
    
    # Update a book
    update_movie(file_path, "Telugu Movie4", {"year": 2022})
    
    # Delete a book
    delete_movie(file_path, "Telugu Movie1")

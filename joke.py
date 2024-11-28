import requests

def get_joke_by_category_and_flags(category, flags):
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags={flags}"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        if joke['type'] == 'single':
            return joke['joke']
        else:
            return f"{joke['setup']} - {joke['delivery']}"
    else:
        return "Failed to retrieve a joke."

def search_jokes(category, flags, search_term):
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags={flags}&contains={search_term}"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        if joke['error']:
            return "No jokes found."
        if joke['type'] == 'single':
            return joke['joke']
        else:
            return f"{joke['setup']} - {joke['delivery']}"
    else:
        return "Failed to retrieve a joke."

if __name__ == "__main__":
    category = "Programming"
    flags = "nsfw,religious,political,racist,sexist,explicit"
    
    print("Random Joke:")
    print(get_joke_by_category_and_flags(category, flags))
    
    search_term = "Python"
    print("\nSearch Joke:")
    print(search_jokes(category, flags, search_term))

print(" ")
print(search_jokes("programming", "nsfw", "maths"))
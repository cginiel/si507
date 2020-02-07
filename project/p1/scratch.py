import requests

# BASE_URL = "https://itunes.apple.com/search?"

# user_entry = input("Enter a search term, or 'exit' to quit: ")

# search_item = f"term={user_entry}"

# response = requests.get(f"{BASE_URL}{search_item}").json()

# print(response)


BASE_URL = "https://itunes.apple.com/search?" # only interested in media

def get_media(url=BASE_URL, params=None):
    '''
    '''
    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url, params=params).json()

    return response

def user_entry():
    '''
    '''
    user_entry = input("Enter a search term, or 'exit' to quit: ")

    search_item = f"term={user_entry}"

    print(f"search item: {search_item}")

    return search_item
    
print(get_media(params={user_entry()}))
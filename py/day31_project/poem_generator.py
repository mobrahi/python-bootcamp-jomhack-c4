import requests

def get_daily_poem():
    # API endpoint for a random poem
    url = "https://poetrydb.org/random"
    
    try:
        # 1. Fetch data from PoetryDB API
        response = requests.get(url)
        response.raise_for_status() # Check for errors
        data = response.json()
        
        # API returns a list, so we take the first item
        poem_data = data[0]
        title = poem_data['title']
        author = poem_data['author']
        lines = poem_data['lines']
        line_count = int(poem_data['linecount'])

        # 2. Check maximum length requirement (55 lines)
        if line_count <= 55:
            save_poem(title, author, lines)
            print(f"Success! '{title}' has been saved.")
        else:
            print(f"Poem too long ({line_count} lines). Retrying...")
            get_daily_poem() # Recursive call to find a shorter poem

    except Exception as e:
        print(f"An error occurred: {e}")

def save_poem(title, author, lines):
    # 3. Save to a text file
    with open("daily_poem.txt", "w", encoding="utf-8") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Author: {author}\n")
        file.write("-" * 20 + "\n")
        # Join the list of lines into a single string with newlines
        file.write("\n".join(lines))

if __name__ == "__main__":
    get_daily_poem()

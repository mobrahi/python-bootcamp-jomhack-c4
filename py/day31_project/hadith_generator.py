import requests
from datetime import datetime
from hijridate import Gregorian
import random

# Function to fetch a random Sahih Hadith
def get_random_hadith():
    # Use the specific endpoint for random Hadith
    url = "https://hadithapi.pages.dev?" 
    
    try:
        response = requests.get(url, timeout=10)
        
        # 1. Check if the request was successful
        if response.status_code != 200:
            return f"Server Error: {response.status_code}"

        # 2. Check if the content type is actually JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            return "Error: API did not return JSON. It might be down or blocked."

        hadith_data = response.json()
        
        # 3. Access the correct keys based on current API structures
        # Common keys in 2026: 'hadith_english', 'data', or 'text'
        return hadith_data.get('hadith_english') or hadith_data.get('data', {}).get('hadith_english')
        
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"

# Main function
def main():
    print("Welcome to the Islamic Daily Sahih Hadith Generator!")
    
  # Current Gregorian date 
    today = datetime.now()

    # Convert to Hijri date using hijridate (v2.3.0)
    hijri_date = Gregorian(today.year, today.month, today.day).to_hijri()

    # Display both dates
    print(f"Today's Date: {today.strftime('%d %B %Y')} / "
f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year}H")
    
    # Fetch and display a random hadith
    hadith = get_random_hadith()
    print("Today's Hadith:")
    print(hadith)

if __name__ == "__main__":
    main()

import requests
from datetime import datetime
import json

class PrayerTimesScheduler:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.base_url = "http://api.aladhan.com/v1/timingsByCity"
        
    def get_prayer_times(self, date=None):
        """Fetch prayer times from Aladhan API"""
        if date is None:
            date = datetime.now().strftime("%d-%m-%Y")
        
        params = {
            'city': self.city,
            'country': self.country,
            'method': 2  # Islamic Society of North America (ISNA)
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['code'] == 200:
                return data['data']['timings']
            else:
                print("Error fetching prayer times")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
    
    def display_prayer_times(self, timings):
        """Display prayer times in a formatted way"""
        if not timings:
            print("No prayer times available")
            return
        
        prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        
        print("\n" + "="*50)
        print(f"Prayer Times for {self.city}, {self.country}")
        print(f"Date: {datetime.now().strftime('%A, %B %d, %Y')}")
        print("="*50)
        
        for prayer in prayers:
            time = timings.get(prayer, "N/A")
            print(f"{prayer:15} {time}")
        
        print("="*50 + "\n")
    
    def get_next_prayer(self, timings):
        """Find the next upcoming prayer"""
        if not timings:
            return None, None
        
        prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        current_time = datetime.now().strftime("%H:%M")
        
        for prayer in prayers:
            prayer_time = timings.get(prayer, "").split()[0]  # Remove timezone info
            if prayer_time > current_time:
                return prayer, prayer_time
        
        # If no prayer left today, next is Fajr tomorrow
        return "Fajr (Tomorrow)", timings.get('Fajr', 'N/A')
    
    def save_to_file(self, timings, filename="prayer_times.txt"):
        """Save prayer times to a text file"""
        if not timings:
            print("No data to save")
            return
        
        with open(filename, 'w') as f:
            f.write(f"Prayer Times for {self.city}, {self.country}\n")
            f.write(f"Date: {datetime.now().strftime('%A, %B %d, %Y')}\n")
            f.write("="*50 + "\n")
            
            prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
            for prayer in prayers:
                time = timings.get(prayer, "N/A")
                f.write(f"{prayer}: {time}\n")
        
        print(f"Prayer times saved to {filename}")

def main():
    print("Islamic Prayer Times Scheduler")
    print("="*50)
    
    # Get user input
    city = input("Enter your city: ").strip()
    country = input("Enter your country: ").strip()
    
    # Create scheduler instance
    scheduler = PrayerTimesScheduler(city, country)
    
    # Main menu loop
    while True:
        print("\nMenu:")
        print("1. View today's prayer times")
        print("2. Check next prayer")
        print("3. Save prayer times to file")
        print("4. Change location")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            timings = scheduler.get_prayer_times()
            scheduler.display_prayer_times(timings)
            
        elif choice == '2':
            timings = scheduler.get_prayer_times()
            next_prayer, next_time = scheduler.get_next_prayer(timings)
            if next_prayer:
                print(f"\nNext Prayer: {next_prayer} at {next_time}")
            
        elif choice == '3':
            timings = scheduler.get_prayer_times()
            scheduler.save_to_file(timings)
            
        elif choice == '4':
            city = input("Enter new city: ").strip()
            country = input("Enter new country: ").strip()
            scheduler = PrayerTimesScheduler(city, country)
            print("Location updated!")
            
        elif choice == '5':
            print("Thank you for using Prayer Times Scheduler!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
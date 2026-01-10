import requests
from datetime import datetime

class PrayerTimesScheduler:
    def __init__(self, zone_code):
        """
        Initialize with a Malaysian zone code
        Examples: SGR01 (Selangor), WLY01 (Kuala Lumpur), JHR01 (Johor)
        """
        self.zone_code = zone_code.upper()
        self.base_url = "https://api.waktusolat.app/v2/solat"
        
    def get_prayer_times(self):
        """Fetch prayer times from Waktu Solat API"""
        try:
            # Build the API URL with zone code
            url = f"{self.base_url}/{self.zone_code}"
            
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # The API returns the whole month, so we need to find today's data
            today_day = datetime.now().day
            prayers_list = data.get('prayers', [])
            
            # Find today's prayer time from the list
            for prayer in prayers_list:
                if prayer.get('day') == today_day:
                    return prayer
            
            return None
                
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except (KeyError, IndexError) as e:
            print(f"Error processing data: {e}")
            return None
    
    def format_hijri_date(self, hijri_str):
        """Convert Hijri date to readable format with month name"""
        hijri_months = {
            '01': 'Muharram', '02': 'Safar', '03': "Rabi' al-Awwal",
            '04': "Rabi' al-Thani", '05': 'Jumada al-Awwal', '06': 'Jumada al-Thani',
            '07': 'Rajab', '08': "Sha'ban", '09': 'Ramadan',
            '10': 'Shawwal', '11': 'Dhul-Qadah', '12': 'Dhul-Hijjah'
        }
        
        try:
            # Split hijri string like "1447-07-20"
            parts = hijri_str.split('-')
            year = parts[0]
            month = parts[1]
            day = parts[2]
            
            month_name = hijri_months.get(month, month)
            return f"{day} {month_name} {year}H"
        except:
            return hijri_str
    
    def format_time(self, timestamp):
        """Convert Unix timestamp to readable time format"""
        try:
            # Convert timestamp to datetime object
            time_obj = datetime.fromtimestamp(int(timestamp))
            # Format as 12-hour time with AM/PM
            return time_obj.strftime("%I:%M %p")
        except:
            return timestamp
    
    def display_prayer_times(self, prayer_data):
        """Display prayer times in a formatted way"""
        if not prayer_data:
            print("No prayer times available")
            return
        
        # Prayer names mapping
        prayer_names = [
            ('imsak', 'Imsak'),
            ('fajr', 'Fajr'),
            ('syuruk', 'Sunrise'),
            ('dhuhr', 'Dhuhr'),
            ('asr', 'Asr'),
            ('maghrib', 'Maghrib'),
            ('isha', 'Isha')
        ]
        
        # Get current date info
        now = datetime.now()
        current_month = now.strftime("%B")  # Full month name
        current_year = now.year
        current_day = prayer_data.get('day', now.day)
        
        print("\n" + "="*50)
        print(f"Prayer Times - Zone {self.zone_code}")
        print(f"Date: {current_day} {current_month} {current_year}")
        
        # Format Hijri date
        hijri_raw = prayer_data.get('hijri', 'N/A')
        hijri_formatted = self.format_hijri_date(hijri_raw)
        print(f"Hijri: {hijri_formatted}")
        print("="*50)
        
        for key, name in prayer_names:
            time = prayer_data.get(key, "N/A")
            # Format the timestamp to readable time
            if time != "N/A":
                time = self.format_time(time)
            print(f"{name:15} {time}")
        
        print("="*50 + "\n")
    
    def get_next_prayer(self, prayer_data):
        """Find the next upcoming prayer"""
        if not prayer_data:
            return None, None
        
        prayer_order = [
            ('fajr', 'Fajr'),
            ('syuruk', 'Sunrise'),
            ('dhuhr', 'Dhuhr'),
            ('asr', 'Asr'),
            ('maghrib', 'Maghrib'),
            ('isha', 'Isha')
        ]
        
        current_timestamp = int(datetime.now().timestamp())
        
        for key, name in prayer_order:
            prayer_time = prayer_data.get(key)
            if prayer_time:
                try:
                    prayer_timestamp = int(prayer_time)
                    if prayer_timestamp > current_timestamp:
                        time_formatted = self.format_time(prayer_time)
                        return name, time_formatted
                except:
                    continue
        
        # If no prayer left today, next is Subuh tomorrow
        return "Fajr (Tomorrow)", "N/A"
    
    def save_to_file(self, prayer_data, filename="waktu_solat.txt"):
        """Save prayer times to a text file"""
        if not prayer_data:
            print("No data to save")
            return
        
        prayer_names = [
            ('imsak', 'Imsak'),
            ('fajr', 'Fajr'),
            ('syuruk', 'Sunrise'),
            ('dhuhr', 'Dhuhr'),
            ('asr', 'Asr'),
            ('maghrib', 'Maghrib'),
            ('isha', 'Isha')
        ]
        
        # Get current date info
        now = datetime.now()
        current_month = now.strftime("%B")
        current_year = now.year
        current_day = prayer_data.get('day', now.day)
        
        # Format Hijri date
        hijri_raw = prayer_data.get('hijri', 'N/A')
        hijri_formatted = self.format_hijri_date(hijri_raw)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Prayer Times - Zone {self.zone_code}\n")
            f.write(f"Date: {current_day} {current_month} {current_year}\n")
            f.write(f"Hijri: {hijri_formatted}\n")
            f.write("="*50 + "\n")
            
            for key, name in prayer_names:
                time = prayer_data.get(key, "N/A")
                if time != "N/A":
                    time = self.format_time(time)
                f.write(f"{name}: {time}\n")
        
        print(f"✅ Prayer times saved to {filename}")

def display_zone_help():
    """Display common zone codes"""
    print("\n📍 Popular Zone Codes:")
    print("="*50)
    print("WLY01 - Kuala Lumpur")
    print("SGR01 - Gombak, Petaling, Sepang, Hulu Langat")
    print("SGR02 - Kuala Selangor, Sabak Bernam")
    print("JHR01 - Johor Bahru, Kota Tinggi, Mersing")
    print("PNG01 - Penang")
    print("MLK01 - Malacca")
    print("NSN01 - Negeri Sembilan")
    print("PHG01 - Pahang (Central)")
    print("KTN01 - Kelantan (Kota Bharu)")
    print("TRG01 - Terengganu (Kuala Terengganu)")
    print("="*50)
    print("💡 For complete list, visit:")
    print("   https://api.waktusolat.app/locations\n")

def main():
    print("🕌 Islamic Prayer Times Scheduler - Malaysia")
    print("="*50)
    
    # Show zone help
    display_zone_help()
    
    # Get zone code from user
    zone_code = input("Enter your zone code (example: WLY01): ").strip()
    
    # Create scheduler instance
    scheduler = PrayerTimesScheduler(zone_code)
    
    # Main menu loop
    while True:
        print("\nMenu:")
        print("1. View today's prayer times")
        print("2. Check next prayer time")
        print("3. Save prayer times to file")
        print("4. Change zone")
        print("5. View zone codes")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            prayer_data = scheduler.get_prayer_times()
            scheduler.display_prayer_times(prayer_data)
            
        elif choice == '2':
            prayer_data = scheduler.get_prayer_times()
            next_prayer, next_time = scheduler.get_next_prayer(prayer_data)
            if next_prayer:
                print(f"\n⏰ Next Prayer: {next_prayer} at {next_time}")
            
        elif choice == '3':
            prayer_data = scheduler.get_prayer_times()
            scheduler.save_to_file(prayer_data)
            
        elif choice == '4':
            zone_code = input("Enter new zone code: ").strip()
            scheduler = PrayerTimesScheduler(zone_code)
            print("✅ Zone updated!")
            
        elif choice == '5':
            display_zone_help()
            
        elif choice == '6':
            print("\n✨ Thank you for using Prayer Times Scheduler!")
            print("May your prayers be accepted.")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
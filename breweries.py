import requests
from collections import Counter

class BreweryData:
    def __init__(self, states):
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.states = states
        self.data = []

    def fetch_data(self):
        """Fetches brewery data for the specified states."""
        for state in self.states:
            response = requests.get(f"{self.base_url}?by_state={state}")
            if response.status_code == 200:
                self.data.extend(response.json())
            else:
                print(f"Failed to fetch data for {state}")

    def list_breweries(self):
        """Lists all breweries in the specified states."""
        for brewery in self.data:
            print(f"Name: {brewery['name']}, State: {brewery['state']}, City: {brewery['city']}")

    def count_breweries_by_state(self):
        """Counts the number of breweries in each specified state."""
        state_count = Counter(brewery['state'] for brewery in self.data)
        for state in self.states:
            print(f"{state}: {state_count[state]} breweries")

    def count_brewery_types_by_city(self):
        """Counts the number of types of breweries in individual cities of the specified states."""
        for state in self.states:
            city_type_count = {}
            for brewery in self.data:
                if brewery['state'] == state:
                    city = brewery['city']
                    brewery_type = brewery['brewery_type']
                    if city not in city_type_count:
                        city_type_count[city] = Counter()
                    city_type_count[city][brewery_type] += 1

            print(f"\nBrewery types in {state} by city:")
            for city, types in city_type_count.items():
                print(f"City: {city}")
                for brewery_type, count in types.items():
                    print(f"  {brewery_type}: {count}")

    def count_breweries_with_websites(self):
        """Counts and lists the number of breweries with websites in the specified states."""
        website_count = Counter()
        for brewery in self.data:
            if brewery['website_url']:
                website_count[brewery['state']] += 1

        print("\nNumber of breweries with websites:")
        for state in self.states:
            print(f"{state}: {website_count[state]} breweries with websites")


# Usage
states = ['Alaska', 'Maine', 'New York']
brewery_data = BreweryData(states)

# Fetch data for the specified states
brewery_data.fetch_data()

# 1. List all breweries in the states of Alaska, Maine, and New York
print("Listing all breweries:")
brewery_data.list_breweries()

# 2. Count the number of breweries in each state
print("\nCounting breweries by state:")
brewery_data.count_breweries_by_state()

# 3. Count the number of types of breweries in individual cities of the states
brewery_data.count_brewery_types_by_city()

# 4. Count and list how many breweries have websites in the states
brewery_data.count_breweries_with_websites()

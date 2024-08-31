import requests
import folium

def get_location_from_ip(ip):
    url = f"http://ipinfo.io/{ip}/json"
    
    response = requests.get(url)
    data = response.json()
    # print(data)
    return data

def display_map(latitude, longitude):
    location_map = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup='Your Location').add_to(location_map)
    return location_map

if __name__ == "__main__":
    user_ip = input("Enter IP address: ")
    location_data = get_location_from_ip(user_ip)
    if (location_data['country']== 'IN'):
        print("City : "+location_data['city'])
        print("State : "+location_data['region'])
        print("Country : INDIA")

    if 'loc' in location_data:
        latitude, longitude = location_data['loc'].split(',')
        map_view = display_map(float(latitude), float(longitude))
        map_view.save("user_location.html")
        print("Map generated and saved as user_location.html")
    else:
        print("Could not fetch location details.")

import requests

# URL of the webpage
url = 'https://www.ufc.com/event/ufc-fight-night-june-22-2024'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Write the HTML content to a local file
    with open('ufc_event.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
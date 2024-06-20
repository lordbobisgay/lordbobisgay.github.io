import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_fighter_country(name, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Split the name into first and last names
    first_name, last_name = name.split()
    print(f"Searching for fighter: {first_name} {last_name}")

    # Find all blocks potentially containing fighter details
    fight_blocks = soup.find_all('div', class_='c-listing-fight__details-content')
    
    for block in fight_blocks:
        # Debugging the extraction of names and check in both corners
        names_red = block.find('div', class_='details-content__name--red')
        names_blue = block.find('div', class_='details-content__name--blue')
        
        # Check red corner
        print("Checking red corner...")
        if names_red:
            given_name_red = names_red.find('span', class_='details-content__corner-given-name')
            family_name_red = names_red.find('span', class_='details-content__corner-family-name')
            if given_name_red and family_name_red:
                print(f"Found names in red corner: {given_name_red.text.strip()} {family_name_red.text.strip()}")
                if given_name_red.text.strip() == first_name and family_name_red.text.strip() == last_name:
                    print("Match found in red corner.")
                    # Navigate to find country info
                    country_div = block.parent.find('div', class_='c-listing-fight__country--red')
                    if country_div:
                        country_text_div = country_div.find('div', class_='c-listing-fight__country-text')
                        if country_text_div:
                            country = country_text_div.text.strip()
                            print(f"Country found: {country}")
                            return country
                        else:
                            print("Country text div not found in red corner.")
                    else:
                        print("Country div not found in red corner.")
            else:
                print("No valid names found in red corner.")
        
        # Check blue corner
        print("Checking blue corner...")
        if names_blue:
            given_name_blue = names_blue.find('span', class_='c-listing-fight__corner-given-name')
            family_name_blue = names_blue.find('span', class_='c-listing-fight__corner-family-name')
            if given_name_blue and family_name_blue:
                print(f"Found names in blue corner: {given_name_blue.text.strip()} {family_name_blue.text.strip()}")
                if given_name_blue.text.strip() == first_name and family_name_blue.text.strip() == last_name:
                    print("Match found in blue corner.")
                    # Navigate to find country info
                    country_div = block.parent.find('div', class_='c-listing-fight__country--blue')
                    if country_div:
                        country_text_div = country_div.find('div', class_='c-listing-fight__country-text')
                        if country_text_div:
                            country = country_text_div.text.strip()
                            print(f"Country found: {country}")
                            return country
                        else:
                            print("Country text div not found in blue corner.")
                    else:
                        print("Country div not found in blue corner.")
            else:
                print("No valid names found in blue corner.")
    
    print("Country not found for the given fighter.")
    return "Country not found for the given fighter."

def fetch_fighter_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    country_to_code = {
        "Afghanistan": "af",
        "Albania": "al",
        "Algeria": "dz",
        "Andorra": "ad",
        "Angola": "ao",
        "Antigua and Barbuda": "ag",
        "Argentina": "ar",
        "Armenia": "am",
        "Australia": "au",
        "Austria": "at",
        "Azerbaijan": "az",
        "Bahamas": "bs",
        "Bahrain": "bh",
        "Bangladesh": "bd",
        "Barbados": "bb",
        "Belarus": "by",
        "Belgium": "be",
        "Belize": "bz",
        "Benin": "bj",
        "Bhutan": "bt",
        "Bolivia": "bo",
        "Bosnia and Herzegovina": "ba",
        "Botswana": "bw",
        "Brazil": "br",
        "Brunei": "bn",
        "Bulgaria": "bg",
        "Burkina Faso": "bf",
        "Burundi": "bi",
        "Cabo Verde": "cv",
        "Cambodia": "kh",
        "Cameroon": "cm",
        "Canada": "ca",
        "Central African Republic": "cf",
        "Chad": "td",
        "Chile": "cl",
        "China": "cn",
        "Colombia": "co",
        "Comoros": "km",
        "Congo, Democratic Republic of the": "cd",
        "Congo, Republic of the": "cg",
        "Costa Rica": "cr",
        "Cote d'Ivoire": "ci",
        "Croatia": "hr",
        "Cuba": "cu",
        "Cyprus": "cy",
        "Czech Republic": "cz",
        "Denmark": "dk",
        "Djibouti": "dj",
        "Dominica": "dm",
        "Dominican Republic": "do",
        "Ecuador": "ec",
        "Egypt": "eg",
        "El Salvador": "sv",
        "Equatorial Guinea": "gq",
        "Eritrea": "er",
        "Estonia": "ee",
        "Eswatini": "sz",
        "Ethiopia": "et",
        "Fiji": "fj",
        "Finland": "fi",
        "France": "fr",
        "Gabon": "ga",
        "Gambia": "gm",
        "Georgia": "ge",
        "Germany": "de",
        "Ghana": "gh",
        "Greece": "gr",
        "Grenada": "gd",
        "Guatemala": "gt",
        "Guinea": "gn",
        "Guinea-Bissau": "gw",
        "Guyana": "gy",
        "Haiti": "ht",
        "Honduras": "hn",
        "Hungary": "hu",
        "Iceland": "is",
        "India": "in",
        "Indonesia": "id",
        "Iran": "ir",
        "Iraq": "iq",
        "Ireland": "ie",
        "Israel": "il",
        "Italy": "it",
        "Jamaica": "jm",
        "Japan": "jp",
        "Jordan": "jo",
        "Kazakhstan": "kz",
        "Kenya": "ke",
        "Kiribati": "ki",
        "Korea, North": "kp",
        "Korea, South": "kr",
        "Kuwait": "kw",
        "Kyrgyzstan": "kg",
        "Laos": "la",
        "Latvia": "lv",
        "Lebanon": "lb",
        "Lesotho": "ls",
        "Liberia": "lr",
        "Libya": "ly",
        "Liechtenstein": "li",
        "Lithuania": "lt",
        "Luxembourg": "lu",
        "Madagascar": "mg",
        "Malawi": "mw",
        "Malaysia": "my",
        "Maldives": "mv",
        "Mali": "ml",
        "Malta": "mt",
        "Marshall Islands": "mh",
        "Mauritania": "mr",
        "Mauritius": "mu",
        "Mexico": "mx",
        "Micronesia": "fm",
        "Moldova": "md",
        "Monaco": "mc",
        "Mongolia": "mn",
        "Montenegro": "me",
        "Morocco": "ma",
        "Mozambique": "mz",
        "Myanmar": "mm",
        "Namibia": "na",
        "Nauru": "nr",
        "Nepal": "np",
        "Netherlands": "nl",
        "New Zealand": "nz",
        "Nicaragua": "ni",
        "Niger": "ne",
        "Nigeria": "ng",
        "North Macedonia": "mk",
        "Norway": "no",
        "Oman": "om",
        "Pakistan": "pk",
        "Palau": "pw",
        "Palestine": "ps",
        "Panama": "pa",
        "Papua New Guinea": "pg",
        "Paraguay": "py",
        "Peru": "pe",
        "Philippines": "ph",
        "Poland": "pl",
        "Portugal": "pt",
        "Qatar": "qa",
        "Romania": "ro",
        "Russia": "ru",
        "Rwanda": "rw",
        "Saint Kitts and Nevis": "kn",
        "Saint Lucia": "lc",
        "Saint Vincent and the Grenadines": "vc",
        "Samoa": "ws",
        "San Marino": "sm",
        "Sao Tome and Principe": "st",
        "Saudi Arabia": "sa",
        "Senegal": "sn",
        "Serbia": "rs",
        "Seychelles": "sc",
        "Sierra Leone": "sl",
        "Singapore": "sg",
        "Slovakia": "sk",
        "Slovenia": "si",
        "Solomon Islands": "sb",
        "Somalia": "so",
        "South Africa": "za",
        "South Sudan": "ss",
        "Spain": "es",
        "Sri Lanka": "lk",
        "Sudan": "sd",
        "Suriname": "sr",
        "Sweden": "se",
        "Switzerland": "ch",
        "Syria": "sy",
        "Taiwan": "tw",
        "Tajikistan": "tj",
        "Tanzania": "tz",
        "Thailand": "th",
        "Timor-Leste": "tl",
        "Togo": "tg",
        "Tonga": "to",
        "Trinidad and Tobago": "tt",
        "Tunisia": "tn",
        "Turkey": "tr",
        "Turkmenistan": "tm",
        "Tuvalu": "tv",
        "Uganda": "ug",
        "Ukraine": "ua",
        "United Arab Emirates": "ae",
        "United Kingdom": "gb",
        "United States": "us",
        "Uruguay": "uy",
        "Uzbekistan": "uz",
        "Vanuatu": "vu",
        "Vatican City": "va",
        "Venezuela": "ve",
        "Vietnam": "vn",
        "Yemen": "ye",
        "Zambia": "zm",
        "Zimbabwe": "zw"
    }

    # Extract fighter name and record
    name = soup.find('span', class_='b-content__title-highlight').text.strip()
    record = soup.find('span', class_='b-content__title-record').text.replace('Record:', '').strip()

    country = fetch_fighter_country(name, 'https://www.ufc.com/event/ufc-fight-night-june-22-2024')
    country_code = country_to_code.get(country, 'Unknown')
    # Extract fighter details
    details = {}
    for item in soup.find_all('li', class_='b-list__box-list-item_type_block'):
        title_element = item.find('i', class_='b-list__box-item-title')
        if title_element:
            key = title_element.text.strip(':').strip()
            value = item.text.replace(key + ':', '').strip()  # Strip here to remove leading/trailing spaces
            if key == "Weight:":
                # Process weight to remove text and keep only the numerical part
                value = ' '.join(value.split())  # Remove extra spaces between words
                value = value.replace('Weight:', '').replace('lbs', '').strip()  # Remove 'Weight:' and 'lbs'
                original_value = value  # Store the original value for debugging
                value = value.split(' ')[0]  # Extract the first part which should be the weight number
                weight_num = int(value)
                weight_classes = [125, 135, 145, 155, 170, 185, 205, 265]
                if weight_num > 207:
                    rounded_weight = 265
                else:
                    rounded_weight = min(weight_classes, key=lambda x: abs(x - weight_num))
                value = rounded_weight  # Update the value to the rounded weight
                print(f"Rounded weight to nearest class: {rounded_weight}")
                print(f"Transformed {key}: from '{original_value}' to '{value}'")  # Debug print for transformation
            if key == "Height:":
                # Process weight to remove text and keep only the numerical part
                value = ' '.join(value.split())  # Remove extra spaces between words
                value = value.replace('Height:', '').strip()  # Remove 'Weight:' and 'lbs'
                original_value = value  # Store the original value for debugging
                value = value.replace('"', r'\"')  # Escape double quotes by adding a backslash before them
                print(f"Transformed {key}: from '{original_value}' to '{value}'")  # Debug print for transformation
            if key == "Reach:":
                # Process weight to remove text and keep only the numerical part
                value = ' '.join(value.split())  # Remove extra spaces between words
                value = value.replace('Reach:', '').replace('"', '').strip()  # Remove 'Weight:' and 'lbs'
                original_value = value  # Store the original value for debugging
                print(f"Transformed {key}: from '{original_value}' to '{value}'")  # Debug print for transformation
            if key == "DOB:":
                # Process weight to remove text and keep only the numerical part
                value = ' '.join(value.split())  # Remove extra spaces between words
                value = value.replace('DOB:', '').strip()  # Remove 'Weight:' and 'lbs'
                original_value = value  # Store the original value for debugging
                print(f"Transformed {key}: from '{original_value}' to '{value}'")  # Debug print for transformation
            details[key] = value
            print(f"Key: {key}, Value: {value}")  # Debug print to verify each key-value pair

    # Convert date if DOB is available
    dob = details.get('DOB:', 'Unknown')
    dob_formatted = 'Unknown'
    if dob != 'Unknown':
        try:
            dob_datetime = datetime.strptime(dob, '%b %d, %Y')
            dob_formatted = dob_datetime.strftime('%m/%d/%Y')
        except ValueError:
            print("Date format is incorrect:", dob)  # Error handling for date parsing

    # Format output
    output = f"{name.replace(' ', '_')} = Fighter("
    output += f'\n    name="{name}",'
    output += f'\n    picture="assets/img/portfolio/{name.replace(" ", "_")}.png",'
    output += f'\n    country="{country}",'
    output += f'\n    country_image="assets/img/portfolio/flags/{country_code}.png",'
    output += f'\n    weight={int(details.get("Weight:", "0"))},'
    output += '\n    rank="",'
    output += f'\n    record="{record}",'
    output += f'\n    height="{details.get("Height:", "Unknown")}",'
    reach = details.get("Reach:", "0\"").replace('"', "").strip()
    output += f'\n    reach={int(reach) if reach.isdigit() else 0},'
    output += f'\n    dob="{dob_formatted}"'
    output += '\n)'
    
    print(output)

# URL of the webpage
url = 'http://www.ufcstats.com/fighter-details/8c0580d4fff106c1'
fetch_fighter_details(url)

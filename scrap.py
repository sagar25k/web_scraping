import requests
from lxml import html

# URL of the website
url = "https://www.adityatekkali.edu.in/csefaculty.php"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    parsed_html = html.fromstring(response.content)

    # Extract faculty information
    faculty_divs = parsed_html.xpath("//div[@class='main']")

    # Iterate over each faculty div
    for faculty_div in faculty_divs:
        # Extract faculty name
        faculty_name = faculty_div.xpath(".//span[1]/text()")[0].strip()

        # Extract faculty details
        faculty_details = [detail.strip() for detail in
                           faculty_div.xpath(".//span[position() > 1 and not(contains(text(), 'Employee Id'))]/text()")]

        # Extract faculty profile link
        profile_link = faculty_div.xpath(".//button/@onclick")[0].split("'")[1]

        # Print faculty information
        print('Faculty Name:', faculty_name)
        print('Faculty Details:')
        for detail in faculty_details:
            print('-', detail)
        print('Faculty Profile Link:', profile_link)
        print()
else:
    print("Failed to retrieve data from the URL. Status code:", response.status_code)

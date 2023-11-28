# Python pseudocode for a Web Scraper using BeautifulSoup

# Step 1: Import necessary libraries/modules
import requests
from bs4 import BeautifulSoup

# Step 2: Function to fetch and parse HTML content from a website
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML content: {e}")
        return None

# Step 3: Function to extract and display information from the parsed HTML
def scrape_website(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Replace 'your-selector' with the appropriate CSS selector for the information you want to scrape
        scraped_data = soup.select_one('your-selector').get_text(strip=True)
        print(f"Scraped Data: {scraped_data}")
    else:
        print("No HTML content to scrape.")

# Step 4: Main function
def main():
    url = input("Enter the URL of the website to scrape: ")
    html_content = get_html_content(url)
    
    if html_content:
        scrape_website(html_content)

# Step 5: Call the main function
if __name__ == "__main__":
    main()

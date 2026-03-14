import requests
from bs4 import BeautifulSoup
import os


def scrape_gce():

    urls = [
        "https://gcebodi.ac.in/",
        "https://gcebodi.ac.in/content/hods",
        "https://gcebodi.ac.in/22/department-computer-science-engineering-faculty",
        "https://gcebodi.ac.in/content/about-institute-0",
        "https://gcebodi.ac.in/content/college-fee-structure-0",
        "https://gcebodi.ac.in/content/courses-offered-0",
        "https://gcebodi.ac.in/content/placements"
    ]

    knowledge_base = ""

    for url in urls:

        try:
            response = requests.get(url, timeout=10)

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract visible text
            text = soup.get_text(separator=" ", strip=True)

            knowledge_base += f"\n\nSOURCE: {url}\n{text}\n"

            print(f"✔ Scraped: {url}")

        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")

    # Get project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create data folder if not exists
    data_folder = os.path.join(BASE_DIR, "data")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # File path
    file_path = os.path.join(data_folder, "gce_bodi_data.txt")

    # Save file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(knowledge_base)

    print("✅ Website data saved successfully!")


if __name__ == "__main__":
    scrape_gce()
#!/usr/bin/python3
#
# AUTHOR :  Armand CORBEAUX
#           armand.corbeaux@gmail.com
#
# DATE :    2023.11.06
#
# GOALS : retrieve all the links with data
#         keep the ones with *egional
#         sort URL with import / export
#         get and extract the file on targeted OUTPUT directory tree
#         tree :
#         /import/{year}/
#         /export/{year}/
#
# INPUT :   URL with links to OpenData files from douanes.gouv.fr
#
# OUTPUT :  /{import or export}/{1 folder per year}/{contained files in zip archive}
#
MAIN_URL = "https://www.douane.gouv.fr/"
TARGET_URL = f"{MAIN_URL}/la-douane/opendata?op=&recherche_opendata=&f%5B0%5D=categorie_opendata_facet%3A458"

# used libraries
import requests
from bs4 import BeautifulSoup

def retrieve_links_in_url(TARGET_URL):
    """retrieve all the links in the targeted URL

    Args:
        TARGET_URL (string): URL to website which contains the relevant informations

    Returns:
        zip_links: links which contains "egional" inside
    """    
    page_number = 1
    zip_links = []

    while True:
        # Send a GET request to the target URL with the page number as a parameter
        response = requests.get(TARGET_URL + f"&page={page_number}")

        # Check if the response was successful
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}")
            break

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the links to zip files on the page
        links = soup.find_all("a", href=lambda href: href and href.endswith(".zip"))

        # Add the links which contains "egional" to the list of zip links
        zip_links.extend(link["href"] for link in links if "egional" in link["href"])

        # Check if there are more pages to retrieve
        next_button = soup.find("a", string="Suivant")
        if not next_button:
            break

        # Increment the page number
        page_number += 1
        print(f"page number: {page_number}")

    return zip_links

def sort_url(zip_links):
    """sort links if they contains "export" or "import"

    Args:
        zip_links: links which contains "egional" inside

    Returns:
        export_links : links which contains "export" inside
        import_links : links which contains "import" inside
    """    
    export_links = []
    import_links = []
    for link in zip_links:
        if "export" in link:
            export_links.append(link)
        elif "import" in link:
            import_links.append(link)
    return export_links, import_links

if __name__ == "__main__":
    
    zip_links = retrieve_links_in_url(TARGET_URL)
    export_links,import_links = sort_url(zip_links)
    
    print(zip_links)
    print(export_links)
    print(import_links)
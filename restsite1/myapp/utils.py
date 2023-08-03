#
# def download_image(html_string):
#     soup = BeautifulSoup(html_string, 'html.parser')
#     img_tags = soup.find_all('img')
#     urls = [urljoin(html_string, img['src']) for img in img_tags]
#     for url in urls:
#         response = requests.get(url)
#         filename = url.split("/")[-1]
#         print(filename)
#         with open(filename, "wb") as f:
#             f.write(response.content)
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from django.conf import settings


# output_dir = Path(settings.MEDIA_ROOT + '/images')
#
# print(output_dir)


def parse_and_download_images(html):
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Find all <img> tags
    img_tags = soup.find_all('img')
    # Iterate through each <img> tag
    for img in img_tags:
        # Get the source URL of the image
        src_url = img['src']
        match_obj = re.match(r'^(?:http)s?://', src_url, re.I | re.M)
        if match_obj:
            # Download the image and save it locally
            response = requests.get(src_url)
            file = src_url.split("/")[-1]
            save_path = str(Path(settings.MEDIA_ROOT) / Path('uploads') / file)

            with open(save_path, 'wb+') as destination:
                destination.write(response.content)
            img['src'] = "/" + "/".join(Path(save_path).parts[-3:])

    modified_html = str(soup)

    # Return the modified HTML as a response
    return modified_html

# print(parse_and_download_images())

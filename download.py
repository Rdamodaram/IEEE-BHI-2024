import os
import requests
from bs4 import BeautifulSoup

# Function to download images from a given URL
def download_images(url, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    image_tags = soup.find_all('img')
    
    # Download each image
    for i, img_tag in enumerate(image_tags):
        img_url = img_tag.get('src')
        if img_url:
            img_response = requests.get(img_url)
            with open(os.path.join(output_dir, f'image_{i}.jpg'), 'wb') as f:
                f.write(img_response.content)
                print(f'Downloaded image_{i}.jpg')

# Main function
def main():
    # URL of the ISIC Archive
    isic_url = 'https://www.isic-archive.com/'
    
    # Output directory to save the images
    output_dir = 'isic_images'
    
    # Download images from the ISIC Archive
    download_images(isic_url, output_dir)

if __name__ == "__main__":
    main()

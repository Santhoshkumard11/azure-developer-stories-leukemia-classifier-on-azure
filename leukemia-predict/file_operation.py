import shutil  # to save it locally
import logging # logging module
import os # remove the file
import tempfile
import requests  # to get image from the web


def save_file(image_url: str):
    """Download the image from blob storage and save it in local system

    Args:
        image_url (str): blob storage location

    Returns:
        str : absolute path of the temp image
    """
    
    base_path = "https://leumemiastorageeus.blob.core.windows.net"
    full_image_path = base_path + image_url
    ## Set up the image URL and filename
    filename = get_file_name_from_image_url(image_url)

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(full_image_path, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # creating a temp file
        ff = tempfile.NamedTemporaryFile(mode ='wb+')
        
        shutil.copyfileobj(r.raw, ff)
        
        temp_file_name = ff.name
        
        logging.info(f'Image successfully Downloaded: {filename}')
        
        return ff,temp_file_name

    logging.error("Can't downloaded the image file..")

    return "f","9"

def get_file_name_from_image_url(image_url: str):
    """Return the file name

    Args:
        image_url (str): Storage Account Url

    Returns:
        (str) : image file name
    """
    
    #split and take out only the last part (file name)
    
    return image_url.split("/")[-1]

def remove_file(image_name):
    
    os.remove(image_name)

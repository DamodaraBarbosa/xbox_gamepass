import wget
import os
from time import sleep

class Manager:
    def __init__(self, link: str, directory: str) -> None:
        self.link = link
        self.directory = directory
    
    def download(self):
        """
        Download the file from the link and save it in the directory. Both nominated by the class.
        """
        file = wget.download(self.link, out= self.directory)
        
        return file
    
    def download_waits(self, file: str):
        """
        Detects when the download is finished so the script can continue from there.
        
        file: file that is downloaded.
        """
        while not os.path.exists(os.path.join(self.directory, file)):
            sleep(1)

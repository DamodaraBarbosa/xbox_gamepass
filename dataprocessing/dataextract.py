import zipfile

class Extract:
    """
    To extract files that are compressed. 
    """
    def __init__(self, zipfile: str) -> None:
        self.zipfile = zipfile

    def zipfiles_list(self):
        """
        Show all files names in zipfile.
        """
        with zipfile.ZipFile(self.zipfile, 'r') as zip_ref:
            files_names = zip_ref.namelist()
            return files_names

    def extract_file(self, file_name: str, path: str):
        """
        Extracts a specific file from the zip file.
        
        file_name: the name of the file you want to extract.
        path: the path to which you want to extract the file.
        """
        with zipfile.ZipFile(self.zipfile, 'r') as zip_ref:
            zip_ref.extract(
                member= file_name,
                path= path
            )
    
    def extract_files(self, path: str):
        """
        Extracts all files from the zip file.
        
        path: the path to which you want to extract all files.
        """
        with zipfile.ZipFile(self.zipfile, 'r') as zip_ref:
            zip_ref.extractall(
                path= path
            )

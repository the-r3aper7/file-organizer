import os
import shutil
from typing import List

text_docs = {'txt', 'doc', 'docx', 'rtf', 'odt', 'pages', 'pdf'}
presentation_docs = {'ppt', 'pptx', 'odp', 'key'}
spreadsheet_docs = {'xls', 'xlsx', 'ods', 'numbers', 'csv'}
publishing_docs = {'indd', 'pub', 'eps'}
technical_docs = {'md', 'tex', 'html', 'htm', 'xml'}
compressed_files = {'zip', 'rar', '7z', 'tar', 'gz', 'gzip', 'bz2', 'tar gz', 'tgz', 'tar bz2', 'tbz2', 'cab', 'iso'}
all_document_extensions = text_docs | presentation_docs | spreadsheet_docs | publishing_docs | technical_docs | compressed_files

lossless_audio = {'wav', 'aiff', 'flac', 'alac', 'aif', 'pcm', 'dsd', 'dxd', 'dsf', 'dff'}
lossy_audio = {'mp3', 'aac', 'ogg', 'wma', 'm4a', 'opus', 'webm'}
professional_audio = {'mid', 'midi', 'stems', 'multitrack', 'ptx', 'logic', 'als', 'fip', 'reason', 'cpr', 'npf'}
playlist_formats = {'m3u', 'm3u8', 'pls', 'wpl', 'zpl'}
all_music_extensions = lossless_audio | lossy_audio | professional_audio | playlist_formats

common_video = {'mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', 'mpg', 'mpeg', '3gp', '3g2', 'gif'}
professional_video = {'prproj', 'fcpx', 'dav', 'veg', 'imovieproj'}
high_end_video = {'raw', 'r3d', 'braw', 'ari', 'dpx'}
streaming_video = {'ts', 'm2ts', 'vob', 'm3u8', 'dash'}
all_video_extensions = common_video | professional_video | high_end_video | streaming_video

all_picture_extensions = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg', 'ico', 'heic', 'raw', 'psd', 'ai', 'eps', 'indd'}

class Organizer:
    def __init__(self) -> None:
        self.home_path = os.path.expanduser("~")
        self.music_path = os.path.join(self.home_path, "Music")
        self.picture_path = os.path.join(self.home_path, "Pictures")
        self.videos_path = os.path.join(self.home_path, "Videos")
        self.document_path = os.path.join(self.home_path, "Documents")
        self.download_path = os.path.join(self.home_path, "Downloads")
        self.total_files_moved = 0
        self.dry_run = False
    
    def check_for_all_directory(self) -> None:
        """Check if all required directories exist."""
        for path in [self.music_path, self.download_path, self.picture_path, 
                    self.videos_path, self.document_path]:
            if not os.path.exists(path):
                print(f"Directory {path} does not exist")
                exit(1)

    def get_files_in_download(self) -> List[str]:
        """Get list of files in download directory."""
        return [file.path for file in os.scandir(self.download_path) if file.is_file()]

    def get_file_extension(self, filename: str) -> str:
        """Get file extension from filename."""
        return filename.split(".")[-1].lower()

    def create_directory_if_not_exists(self, path: str) -> None:
        """Create directory if it doesn't exist."""
        if not os.path.exists(path):
            if not self.dry_run:
                os.makedirs(path)
            print(f"Creating directory: {path}")

    def move_file(self, source: str, destination_dir: str, ext: str) -> None:
        """Move file to destination directory."""
        ext_path = os.path.join(destination_dir, ext)
        self.create_directory_if_not_exists(ext_path)
        
        if self.dry_run:
            print(f"Would move {source} to {ext_path}")
        else:
            shutil.move(source, ext_path)
        self.total_files_moved += 1

    def move_files(self) -> None:
        """Main function to move files to their respective directories."""
        self.check_for_all_directory()
        files = self.get_files_in_download()
        
        for file in files:
            ext = self.get_file_extension(file)
            
            if ext in all_document_extensions:
                self.move_file(file, self.document_path, ext)
            elif ext in all_music_extensions:
                self.move_file(file, self.music_path, ext)
            elif ext in all_video_extensions:
                self.move_file(file, self.videos_path, ext)
            elif ext in all_picture_extensions:
                self.move_file(file, self.picture_path, ext)
        
        action = "Would move" if self.dry_run else "Organized"
        print(f"{action} {self.total_files_moved} {'files' if self.total_files_moved > 1 else 'file'} "
              f"out of {len(files)}.")
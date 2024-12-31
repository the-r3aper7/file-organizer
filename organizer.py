# !/usr/bin/python
import os
import shutil

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
    self.music_path = f"{self.home_path}/Music"
    self.picture_path = f"{self.home_path}/Pictures"
    self.videos_path = f"{self.home_path}/Videos"
    self.document_path = f"{self.home_path}/Documents"
    self.download_path = f"{self.home_path}/Downloads"
    self.total_files_moved = 0
  
  def check_for_all_directory(self):
    if not os.path.exists(self.music_path):
      print(f"Directory named Music does not exists")
      exit(1)
    if not os.path.exists(self.download_path):
      print(f"Directory named Downloads does not exists")
      exit(1)
    if not os.path.exists(self.picture_path):
      print(f"Directory named Pictures does not exists")
      exit(1)
    if not os.path.exists(self.videos_path):
      print(f"Directory named Videos does not exists")
      exit(1)
    if not os.path.exists(self.document_path):
      print(f"Directory named Document does not exists")
      exit(1)

  def get_files_in_download(self) -> list:
    files = []
    for file in os.scandir(self.download_path):
      if file.is_file():
        files.append(file.path)
    return files

  def move_files(self):
    self.check_for_all_directory()
    files = self.get_files_in_download()
    for file in files:
      if (ext := self.get_file_extension(file)) in all_document_extensions:
        ext_path = f"{self.document_path}/{ext}"
        if not os.path.exists(ext_path):
          os.mkdir(ext_path)
        shutil.move(file, ext_path)
        self.total_files_moved += 1

      if (ext := self.get_file_extension(file)) in all_music_extensions:
        ext_path = f"{self.music_path}/{ext}"
        if not os.path.exists(ext_path):
          os.mkdir(ext_path)
        shutil.move(file, ext_path)
        self.total_files_moved += 1

      if (ext := self.get_file_extension(file)) in all_video_extensions:
        ext_path = f"{self.videos_path}/{ext}"
        if not os.path.exists(ext_path):
          os.mkdir(ext_path)
        shutil.move(file, ext_path)
        self.total_files_moved += 1

      if (ext := self.get_file_extension(file)) in all_picture_extensions:
        ext_path = f"{self.picture_path}/{ext}"
        if not os.path.exists(ext_path):
          os.mkdir(ext_path)
        shutil.move(file, ext_path)
        self.total_files_moved += 1
    print(f"Organized {self.total_files_moved} {"files" if self.total_files_moved > 1 else "file"} out of {len(files)}.")

  def get_file_extension(self, filename):
    return filename.split(".")[-1]


if __name__ == "__main__":
  org = Organizer()
  org.move_files()

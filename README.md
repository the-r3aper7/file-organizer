# File Organizer

A Python script that automatically organizes files from your Downloads folder into appropriate directories based on file types. The script categorizes files into Documents, Music, Pictures, and Videos folders, creating subdirectories for specific file extensions.

## Features

- Automatically sorts files from Downloads folder into appropriate categories
- Creates extension-specific subdirectories (e.g., `/Documents/pdf/`, `/Pictures/jpg/`)
- Supports a wide range of file formats including:
  - Documents (txt, pdf, doc, docx, etc.)
  - Images (jpg, png, gif, etc.)
  - Audio (mp3, wav, flac, etc.)
  - Video (mp4, avi, mkv, etc.)
  - Compressed files (zip, rar, 7z, etc.)
- Provides a summary of moved files after completion

## Prerequisites

- Python 3.x
- Standard Python libraries (os, shutil)
- Required directory structure:
  ```
  ~/Documents
  ~/Downloads
  ~/Music
  ~/Pictures
  ~/Videos
  ```

## Installation

### For Debian-based Systems (Ubuntu, etc.)

1. Install pipx if you haven't already:
   ```bash
   sudo apt update
   sudo apt install pipx
   pipx ensurepath
   ```

2. Restart your terminal or run:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc if you use zsh
   ```

3. Install the package:
   ```bash
   pipx install -e .
   ```

### For Other Systems

Install directly using pip:
```bash
pip install -e .
```

Note: If you get an "externally-managed-environment" error on Debian-based systems, use the pipx installation method above instead.

## Usage

After installation, you can use the command `fileorganizer` from anywhere in your terminal:

```bash
# Basic usage - organize Downloads folder
fileorganizer

# See what would happen without making changes
fileorganizer --dry-run

# Organize a different directory
fileorganizer --source "/path/to/directory"
```

## Example

Before:
```
~/Downloads/
├── document.pdf
├── presentation.pptx
├── image.jpg
├── song.mp3
└── video.mp4
```

After:
```
~/Documents/
├── pdf/
│   └── document.pdf
└── pptx/
    └── presentation.pptx

~/Pictures/
└── jpg/
    └── image.jpg

~/Music/
└── mp3/
    └── song.mp3

~/Videos/
└── mp4/
    └── video.mp4
```

## Supported File Types

### Documents
- Text Documents: txt, doc, docx, rtf, odt, pages, pdf
- Presentations: ppt, pptx, odp, key
- Spreadsheets: xls, xlsx, ods, numbers, csv
- Publishing: indd, pub, eps
- Technical: md, tex, html, htm, xml
- Compressed: zip, rar, 7z, tar, gz, and more

### Audio
- Lossless: wav, aiff, flac, alac, aif, pcm, dsd, dxd
- Lossy: mp3, aac, ogg, wma, m4a, opus, webm
- Professional: mid, midi, stems, multitrack, ptx, logic
- Playlists: m3u, m3u8, pls, wpl, zpl

### Video
- Common: mp4, avi, mkv, mov, wmv, flv, webm
- Professional: prproj, fcpx, dav, veg, imovieproj
- High-end: raw, r3d, braw, ari, dpx
- Streaming: ts, m2ts, vob, m3u8, dash

### Images
jpg, jpeg, png, gif, bmp, tiff, webp, svg, ico, heic, raw, psd, ai, eps, indd

## Error Handling

The script will:
- Check for the existence of required directories
- Exit with an error message if any required directory is missing
- Report the total number of files moved versus total files present

## Notes

- Files are moved, not copied
- Subdirectories are created automatically for each file extension
- The script only processes files in the Downloads directory, not subdirectories
- Files with extensions not matching any category will remain in the Downloads folder

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Development

If you want to modify the code:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fileorganizer.git
   cd fileorganizer
   ```

2. Install in development mode:
   ```bash
   # For Debian-based systems
   pipx install -e .
   
   # For other systems
   pip install -e .
   ```

3. Make your changes and test them:
   ```bash
   fileorganizer --dry-run  # Test without making actual changes
   ```
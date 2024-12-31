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

## Usage

1. Save the script to your computer
2. Run the script using Python:
   ```bash
   python3 file_organizer.py
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
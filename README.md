# File Organizer

A Python script to organize and clean up files in a specified directory by sorting files into categories (e.g., Documents, Pictures, Music, etc.) and removing files that haven't been modified within a specified number of years.

## Features

- Organizes files by moving them to predefined folders in the user’s home directory based on file type.
- Automatically deletes files older than a specified time limit.
- Handles errors gracefully, including permissions errors.
- Categorizes files into `Documents`, `Pictures`, `Music`, `Videos`, `Applications`, and `Others`.

## Installation

Clone this repository or download the script file to your local machine. Ensure you have Python 3 installed.

## Usage

To use the script, run it from the command line with the following options:

```bash
python file_organizer.py [OPTIONS]
```

## Options

- `-dp` or `--dir_path`: Specify the directory path you want to organize. If not specified, it defaults to the Downloads directory in the user's home folder.
- `-tl` or `--time_limit`: Specify the number of years after which files will be deleted if they haven’t been modified. Default is 2 years.

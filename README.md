# vim2vsc_json Snippet Converter
## About

This repository contains a Python script that converts .snippet files (commonly used in Vim or UltiSnips) into Visual Studio Code (VS Code) compatible JSON snippets. It is designed to simplify the process for students and developers who want to migrate their snippets quickly.

## Features

Bulk Conversion: Converts multiple .snippet files at once.
Command-Line Usage: Easy to use from the terminal.
Automatic Directory Creation: Automatically creates the output folder if it doesn't exist.
Clean JSON Output: The converted files are properly formatted for VS Code.

## Requirements

Python 3.6+

## How to Use

1. Clone the Repository

https://github.com/arpitkumar2004/vim2vsc_json.git
cd vim2vsc_json


2. Place Your .snippet Files

Add your .snippet files into a folder (e.g., snippets).

3. Run the Script

python snippet_converter.py <input_directory> <output_directory>

Example: If your .snippet files are in a folder named snippets and you want the converted JSON files in a folder named converted_snippets:

    python snippet_converter.py snippets converted_snippets

4. Import the JSON Files into VS Code

    1. Open VS Code.
    2. Go to File -> Preferences -> User Snippets.
    3. Choose the language you want (e.g., python.json).
    4. Copy the content of the converted JSON file into the opened snippet file.

### Example
Input (example.snippet):

    snippet temp_date "Template with Date and Author"
    #  author: violist
    #  created: `date +%d.%m.%Y" "%R:%S`
    import sys
    input = sys.stdin.readline
    endsnippet

Output (converted_snippets/example.json):

    {
        "Template with Date and Author": {
            "prefix": "temp_date",
            "body": [
                "#  author: violist",
                "#  created: `date +%d.%m.%Y\" \"%R:%S`",
                "",
                "import sys",
                "input = sys.stdin.readline"
            ],
            "description": "Template with Date and Author"
        }
    }

## Directory Structure

    .
    ├── snippet_converter.py       # Python script
    ├── snippets/                  # Input directory (contains .snippet files)
    │   ├── example.snippet
    │   └── another_example.snippet
    ├── converted_snippets/        # Output directory (created automatically)
    │   ├── example.json
    │   └── another_example.json
    ├── README.md                  # Documentation

## License

This project is licensed under the MIT License. See the LICENSE file for details.
## Contributing

Contributions are welcome! If you encounter issues or have suggestions, feel free to open an issue or create a pull request.
Contact

For questions or feedback, please reach out at: [kumararpit17773@gmail.com] or via GitHub issues.
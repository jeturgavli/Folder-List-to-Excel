# Folder List to Excel

This Python script lists all folder names within a specified directory and saves them into an Excel file. Each time the script is run, it creates a new Excel file with a series number in the `output` folder of the project.

## Features

- Lists all folder names within a specified directory.
- Saves folder names into an Excel file.
- Automatically creates a new Excel file with a series number each time the script is run.
- Automatically creates an `output` folder if it doesn't exist.

## Getting Started

### Prerequisites

- Python 3.x
- `pandas` library
- `openpyxl` library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/folder-list-to-excel.git
    cd folder-list-to-excel
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the script:

    ```bash
    python script.py
    ```

2. Enter the directory path when prompted. For example:

    ```plaintext
    Enter the directory path: /path/to/your/directory
    ```

3. The script will generate an Excel file in the `output` folder with a series number in the filename, such as `folder_list_00001.xlsx`.

### Example

If you have a directory structure like this:

    /example_directory
    ├── folder1
    ├── folder2
    └── folder3

And you run the script with `/example_directory` as the input, the `output` folder will contain an Excel file named `folder_list_00001.xlsx` with the following content:

    | Folder Names |
    |--------------|
    | folder1      |
    | folder2      |
    | folder3      |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

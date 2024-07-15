# 📂 Directory to JSON Converter

This project provides a tool to generate a JSON representation of a directory structure. The output can optionally include the contents of the files. It offers both a command-line interface (CLI) and a graphical user interface (GUI) using Tkinter.

## 🌟 Features

- Generate a JSON representation of a directory structure.
- Optionally include the contents of the files.
- Easy-to-use CLI and GUI options.

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/directory-to-json.git
    cd directory-to-json
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### Command-Line Interface

You can use the script directly from the command line.

```bash
python your_script.py /path/to/directory --include-content
```

- `directory`: The directory to analyze (default is the current directory).
- `--include-content`: Include file contents in the JSON output.

### Graphical User Interface

For a user-friendly GUI, simply run the script without any arguments:

```bash
python your_script.py
```

1. Click on "Select Directory" to choose the directory.
2. Check "Include file content" if you want to include the contents of the files.
3. The JSON file will be saved in the selected directory.

## 📦 Requirements

- Python 3.x
- Required packages are listed in `requirements.txt`.

## 📜 License

This project is licensed under the MIT License.

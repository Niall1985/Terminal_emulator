# Terminal Emulator
This is a simple terminal emulator application built using Python and Tkinter. It supports basic terminal commands such as ls, pwd, mkdir, cd, rmdir, and clear. The terminal provides a text interface for interacting with the file system and executing basic commands.

## Features
1. List Directories (ls): Lists the contents of a specified directory.
2. Print Working Directory (pwd): Displays the current working directory.
3. Make Directory (mkdir): Creates a new directory.
4. Change Directory (cd): Changes the current working directory.
5. Remove Directory (rmdir): Deletes a specified directory.
6. Clear Terminal (clear): Clears the terminal output.
Quit Application (:q!): Exits the terminal emulator.

## Installation
To run the terminal emulator, ensure you have Python installed on your system. You can download Python from python.org.

1. Clone the repository or download the source code:
``` bash
git clone <repository-url>
cd terminal-emulator
``` 

2. Install the required dependencies:
``` bash
pip install tk
```

## Usage
To start the terminal emulator, run the following command:
```bash
python terminal_emulator.py
```

### Commands
1. ls [path]: Lists the contents of the specified directory. If no path is specified, lists the contents of the current directory.
2. pwd: Prints the current working directory.
3. mkdir <directory_name>: Creates a new directory with the specified name.
4. cd <path>: Changes the current working directory to the specified path.
5. rmdir <directory_name>: Deletes the specified directory.
6. clear: Clears the terminal output.
7. :q!: Exits the terminal emulator.

### Example
1. List directories:
```bash
ls
```

2. Print working directory:
```bash
pwd
```
3. Make a new directory:
```bash
mkdir new_directory
```

4. Change directory:

```bash
cd new_directory
```

5. Remove directory:
```bash
rmdir new_directory
```

6. Clear terminal:
```bash
clear
```

7. Quit application:

```bash
:q!
```

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
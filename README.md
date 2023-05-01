# SHIRT: SHIRT Handles Intense Renaming Tasks

![shirt readme banner](https://i.imgur.com/nSp2wcK.png)

SHIRT is a command-line tool for renaming files by replacing strings in their filenames. It provides a convenient and efficient way to handle bulk renaming tasks, with support for file patterns, recursion, and optional backup of the original files.

## Features

- Replace one or multiple strings in filenames
- Match files by file pattern
- Invert file pattern matching
- Recurse through subdirectories
- Dry-run mode to preview changes before renaming
- Backup original files before renaming

## Installation

1. Ensure you have Python 3.6 or later installed.
2. Install the required libraries: `pip install click rich`
3. Download the `shirt.py` script and make it executable: `chmod +x shirt.py`
4. Rename the script to `shirt` without the `.py` extension: `mv shirt.py shirt`
5. Move the `shirt` script to a directory in your `PATH` (e.g., `/usr/local/bin` or `~/.local/bin`):

```bash
sudo mv shirt /usr/local/bin/  # or
mv shirt ~/.local/bin/
```

Ensure that the chosen directory is in your `PATH`. You can check your `PATH` by running `echo $PATH`.

You can now use the `shirt` command from anywhere in your filesystem without needing to prepend it with `python`.

## Usage

```bash

shirt [OPTIONS] STRINGS... REPLACEMENT

```

### Options

- `-r, --recursive`: Search for files recursively in subdirectories.
- `-p, --pattern PATTERN`: A file pattern to match against filenames (e.g., `*.txt`). (default: `*`)
- `-i, --invert-match`: Act on files that do not match the given pattern.
- `-d, --dry-run`: Show the changes that would be made, without renaming any files.
- `-b, --backup`: Backup files before renaming.

### Examples

- Replace "old" with "new" in all filenames:

```bash

shirt "old" "new"

```

- Replace "old1" and "old2" with "new" in all `.txt` files:

```bash

shirt "old1" "old2" "new" -p "*.txt"

```

- Replace "old" with "new" in filenames that do not match the pattern `*123*`:

```bash

shirt "old" "new" -p "*123*" -i

```

- Replace "old" with "new" in filenames, recursing through subdirectories:

```bash

shirt "old" "new" -r

```

- Preview changes without renaming any files:

```bash

shirt "old" "new" -d

```

- Backup original files before renaming:

```bash

shirt "old" "new" -b

```

## Roadmap

- [x] One-click installation script.
- [x] Dry-run mode to preview the changes without actually renaming the files.
- [ ] Auto-detection and handling of character encoding in filenames (e.g., UTF-8, UTF-16, ISO-8859-1) to ensure proper renaming across different systems and platforms.
- [ ] Logging support, including a log file with detailed information about the renaming process and any encountered issues.
- [ ] Undo functionality to revert the last renaming operation.
- [ ] Case sensitivity option for matching file patterns and replacing strings.
- [ ] Regular expression support for more advanced search and replace patterns.
- [ ] Ability to rename directories as well as files.
- [ ] Integration with version control systems like Git, to automatically stage changes or create a commit after renaming.
- [ ] File attribute preservation (e.g., timestamps, permissions) during the renaming process.
- [ ] Rename confirmation prompt before applying changes, especially for large numbers of files or when using complex patterns.

## License

MIT License. See the [LICENSE](LICENSE) file for details.

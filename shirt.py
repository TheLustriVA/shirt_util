#!/usr/bin/env python3

import os
import glob
import fnmatch
import shutil
import sys
import click
from rich.console import Console
from rich.table import Table
from rich.traceback import install

install(show_locals=True)
console = Console()

def get_files_recursive(base_dir, file_pattern, invert_match=False):
    matched_files = []
    for root, _, filenames in os.walk(base_dir):
        for filename in fnmatch.filter(filenames, file_pattern):
            if invert_match:
                if not fnmatch.fnmatch(filename, file_pattern):
                    matched_files.append(os.path.join(root, filename))
            else:
                matched_files.append(os.path.join(root, filename))
    return matched_files

def strip_punctuation(string, characters="?.'\";:,<>[]{}\\|+\'=-)(*&^%$#@!~`+ _", space_to_underscore=False):    
    print(f"Original string: {string}")
    string, extension = os.path.splitext(string)
    print(f"Without extension: {string}")
    print(f"Characters: {characters}")
    to_remove = [char for char in characters]
    for char in to_remove:
        if space_to_underscore and char == " ":
            string = string.replace(char, "_")
        elif space_to_underscore and char =="_":
            string = string
        else:
            string = string.replace(char, "")
    return f"{string}{extension}"
    
        
    

def replace_strings_in_filenames(strings, replacements, file_pattern='*', recursive=False, invert_match=False, dry_run=False, remove_punctuation=False, space_to_underscore=False):
    base_dir = '.'
    if recursive:
        files = get_files_recursive(base_dir, file_pattern, invert_match)
    else:
        files = glob.glob(file_pattern)
        print(files)
        if invert_match:
            files = [f for f in files if not fnmatch.fnmatch(f, file_pattern)]

    renamed_files = []

    for filename in files:
        new_filename = filename
        if remove_punctuation:
            new_filename = strip_punctuation(new_filename, space_to_underscore=space_to_underscore)
            print(f"Existing: {filename}\nNew filename: {new_filename}\n")
        else:
            for old_string, new_string in zip(strings, replacements):
                new_filename = new_filename.replace(old_string, new_string)
        if filename != new_filename:
            if not dry_run:
                os.rename(filename, new_filename)
            renamed_files.append((filename, new_filename))

    return renamed_files


@click.command()
@click.option('-r', '--recursive', is_flag=True, help='Search for files recursively in subdirectories.')
@click.option('-p', '--pattern', default='*', help='A file pattern to match against filenames (e.g., "*.txt").')
@click.option('-i', '--invert-match', is_flag=True, help='Act on files that do not match the given pattern.')
@click.option('-b', '--backup', is_flag=True, help='Backup files before renaming.')
@click.option('-d', '--dry-run', is_flag=True, help='Show the changes that would be made, without renaming any files.')
@click.option('-g', '--remove-punctuation', is_flag=True, help='Replaces need for pair of strings. Remove punctuation from filenames.')
@click.option('-s', '--space-to-underscore', is_flag=True, help='Only works with --remove-punctuation. Replace spaces with underscores.')
@click.argument('strings', nargs=-1)
def main(recursive, pattern, invert_match, backup, dry_run, remove_punctuation, space_to_underscore, strings):
    """
    SHIRT: SHIRT Handles Intense Renaming Tasks

    A command-line tool to replace strings in filenames.

    Example:

    \b
        shirt "old string" "new string"
    """

    if len(strings) < 2 and not remove_punctuation:
        click.echo("Error: At least two strings must be provided (one or more old strings, and one new string).", err=True)
        sys.exit(1)
    if remove_punctuation:
        strings = ["placeholder", "placeholder"]
    old_strings = strings[:-1]
    new_string = strings[-1]

    if backup:
        backup_dir = os.path.join(os.getcwd(), "backup")
        os.makedirs(backup_dir, exist_ok=True)
        files_to_backup = get_files_recursive('.', pattern, invert_match) if recursive else glob.glob(pattern)
        for f in files_to_backup:
            shutil.copy2(f, backup_dir)

    renamed_files = replace_strings_in_filenames(old_strings, [new_string] * len(old_strings), pattern, recursive, invert_match, dry_run, remove_punctuation, space_to_underscore)

    table = Table(title="Renamed Files", show_lines=True)
    table.add_column("Original Filename", style="cyan")
    table.add_column("New Filename", style="green")

    for old_name, new_name in renamed_files:
        table.add_row(old_name, new_name)

    console.print(table)


if __name__ == '__main__':
    main()

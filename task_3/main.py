import sys
from pathlib import Path
from colorama import Fore

def print_folder_structure(path: Path, level: int = 0) -> None:
    """
    Prints folder structure recursively
    path: Path - folder to print
    level: int - current level of folder
    """

    for item in path.iterdir():
        # skip hidden folders
        if item.is_dir() and item.name.startswith("."):
            continue
        # create prefix for each level
        prefix = ' ' * 4 * level
        if item.is_dir():
            # print folder name in blue color
            print(f"{prefix}{Fore.BLUE}{item.name}/")
            # recursively call function to print folder structure
            print_folder_structure(item, level + 1)
        else:
            # print file name in green color
            print(f"{prefix}{Fore.GREEN}{item.name}")


def main():
    if len(sys.argv) == 2:
        directory = Path(sys.argv[1])

        if directory.exists():
            print_folder_structure(directory)
        else:
            print(f"Directory {directory} not found")
    else:
        raise Exception("Invalid number of arguments")

if __name__ == "__main__":
    main()
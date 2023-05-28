import argparse
import logging
from datetime import datetime
from pathlib import Path
from shutil import copyfile
from threading import Thread

"""
--source [-s] 
--output [-o] default folder = dist
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="sort")

args = vars(parser.parse_args())

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_folder = output / ext
            try:
                new_folder.mkdir(parents=True, exist_ok=True)
                copyfile(el, new_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    start_time = datetime.now()

    print(f"Process is started at {start_time}")
    folders.append(source)
    folder_for_sorting = Path(source)
    folder_to_save = Path(output)
    folders.append(folder_for_sorting)
    grabs_folder(folder_for_sorting)
    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder, ))
        th.start()

    [th.join() for th in threads]

    end_time = datetime.now()
    total_time = end_time - start_time

    print(f"Files was sorted and copied into new folder '{output}'\n"
          f"Old folder '{source}' with garbage-files could be deleted.")
    print(f"Process is finished at {end_time}")
    print(f"Total time for sorting: {total_time.total_seconds()} seconds")




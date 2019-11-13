import argparse
import logging
import magic
import os

import core


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('class_title', help='The name of the class, example: sec504')
    parser.add_argument('--files', help='The location where the mp3s are located.', default='.')
    parser.add_argument('--debug', action="store_true", help='Enable debugging messages.')
    parser.add_argument('--dry', action="store_true", help='Do a dry run, do not modify files.')
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug logging enabled.")
    else:
        logging.basicConfig(level=logging.ERROR)
    potential_mp3_files = ["{}/{}".format(args.files, _) for _ in os.listdir(args.files) if os.path.isfile("{}/{}".format(args.files, _)) and not _.endswith('.py')]
    actual_mp3_files = []
    for potential_mp3_file in potential_mp3_files:
        if magic.from_file(potential_mp3_file).startswith('Audio file'):
            actual_mp3_files.append(potential_mp3_file)
            logging.debug(f"Found file {potential_mp3_file}")
    if len(actual_mp3_files) > 0:
        if not args.dry:
            for mp3_file in actual_mp3_files:
                core.update_file(mp3_file, args.class_title)
        else:
            logging.debug(f"Would have changed {len(actual_mp3_files)} files!")
    else:
        print(f"Couldn't find any mp3 files in the directory \"{args.files}\"")
        

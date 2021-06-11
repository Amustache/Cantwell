import argparse
from PIL import Image
import json
from .helpers import *


def process(content, filename='letter.pdf', verbatim=False):
    a4im = Image.new('RGB', PAGE_SIZE, PAGE_COLOR)

    line = 1
    for part, content in content.items():
        if verbatim:
            print("Generating part {}...".format(part))
        if not content['text']:
            line += 1
            continue
        if not content['cut']:
            line += add_cut_text_to_image(content['text'], a4im, off=(content['offset'], MARGIN * line), size=content['limit'])
        else:
            add_text_to_image(content['text'], a4im, off=(content['offset'], MARGIN * line), size=content['limit'])
        line += 1

    a4im.save(filename, 'PDF', quality=100)
    if verbatim:
        print("Letter saved under {}.".format(filename))


def interactive(verbatim=False):
    dict = EXAMPLE.copy()

    print("Write your own letter!\nIf you leave something blank, the line will be skipped.")

    address1 = input("Adress line 1: ")
    if address1:
        dict['address1']['text'] = address1
    else:
        del dict['address1']
    address2 = input("Adress line 2: ")
    if address2:
        dict['address2']['text'] = address2
    else:
        del dict['address2']
    address3 = input("Adress line 3: ")
    if address3:
        dict['address3']['text'] = address3
    else:
        del dict['address3']

    if not address1 and not address2 and not address3:
        del dict['space1']

    dear = input("Introduction (\"Dear something\"): ")
    if dear:
        dict['dear']['text'] = dear
    else:
        del dict['dear']

    if not dear:
        del dict['space2']

    text = input("Text (if too long, will be cropped): ")
    if text:
        dict['text']['text'] = text
    else:
        del dict['text']

    if not text:
        del dict['space3']

    conclusion = input("Conclusion (\"Best regards,\"): ")
    if dear:
        dict['conclusion']['text'] = conclusion
    else:
        del dict['conclusion']
    signature = input("Signature: ")
    if signature:
        dict['signature']['text'] = signature
    else:
        del dict['signature']

    process(dict, verbatim=verbatim)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a little sound letter.")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-e", "--example", action="store_true", help='Generate an example letter.')
    group.add_argument("-f", "--file", action="store", help='Use a JSON file for generation.')
    group.add_argument("-i", "--interactive", action="store_true", dest="interactive", help="Create a letter in the command line!")

    parser.add_argument("-v", "--verbatim", action="store_true", help="State what the program is doing.")

    args = parser.parse_args()

    if args.interactive:
        interactive(verbatim=args.verbatim)
        exit(0)
    elif args.file:
        with open(args.file, 'r') as file:
            if args.verbatim:
                print("Using file {}:".format(args.file))
            data = json.load(file)
            process(data, verbatim=args.verbatim)
        exit(0)
    elif args.example:
        if args.verbatim:
            print("Using example:")
        process(EXAMPLE, verbatim=args.verbatim)
        exit(0)
    else:
        parser.print_help()
        exit(1)

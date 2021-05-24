# Cantwell
Visual sound waves letters generator.

## Why?
First, couldn't sleep.

Then, I was inspired by this image:

![Visual sound waves,  Letter Home, Jennifer Cantwell 2011](https://i.imgur.com/ukX8IS0.jpg)

I thus decided to do my own version, but with arbitrarily inputs.

[More on the original art!](#more-infos)

## What?
Basically, you will enter text that will be converted into a PDF file containing the soundwaves of the text.

The result looks a bit like:

![Built-in example](./example.png)

You can get the previous example by running `soundletter.py -e`.

## How?
### Prerequisites and installation
- `git clone git@github.com:Amustache/Cantwell.git`
- `pip install -Ur ./reqs.txt`
- You may encounter some librairies issues, just install what is needed.
    - Feel free to open an issue so I can document what to install!

### Usage
```
usage: soundletter.py [-h] [-e | -f FILE | -i] [-v]

Generate a little sound letter.

optional arguments:
  -h, --help            show this help message and exit
  -e, --example         Generate an example letter.
  -f FILE, --file FILE  Use a JSON file for generation.
  -i, --interactive     Create a letter in the command line!
  -v, --verbatim        State what the program is doing.
```

#### JSon file
If you wish to use a custom file, here is the format:

```
{
    "unique_identifier1": {
        "text": "What is the text to write?",
        "offset": 1800,
        "limit": 50000,
        "cut": 1
    },
    "unique_identifier2": {
        "text": "",
        "offset": 0,
        "limit": 0,
        "cut": 1
    },
    "unique_identifier3": {
        "text": "Another text to write!",
        "offset": 200,
        "limit": 200000,
        "cut": 1
    },
    ...
}
```

- Each entry is roughly a single line, and shall have a unique identifier.
- `text` is pretty explicit. It can be the length that you want.
    - If `text` is empty, it will simply be considered as a new line.
- `offset` is the offset in regards to the left of the page.
    - For instance, you can use `1800` for the top-right address.
    - For instance, you can use `200` for a little margin for a normal text.
- `limit` is the size to use before truncating the signal.
    - For instance, you can use `50000` for the top-right address.
    - For instance, you can use `200000` for a text that should be full-length.
- `cut` is whether the text should be truncated if too long, or if it shall rather use carriage return.
    - Put `1` to savagely butcher your signal, `0` to still savagely butcher it but without throwing the rest away.

## More infos!
For a bit of context, the original picture has been shared on [Telegram](https://t.me/paspublique/12345), and a discussion emerged in [another channel](https://t.me/ChaoticEvilMobster/2799).
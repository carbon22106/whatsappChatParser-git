# WhatsApp Parser

A small Python command-line tool that processes exported WhatsApp chats and extracts images associated with a specific keyword (such as `Advance`, `Gas`, `Food`, etc.).

The tool filters images by date range, parses the chat export, and collects only the images related to the selected keyword.

## Features

* Filter images by date range
* Parse exported WhatsApp chats
* Search for custom keywords
* Match chat messages with image files
* Automatically organize matching images into a separate folder
* Uses only Python's standard library

## When to Use

This tool is useful when you have exported a WhatsApp chat containing a large number of images and need to quickly locate images related to a specific topic, expense, or transaction.

Examples for common use cases:

* Finding some payment receipts from a chat.
* Collecting gas, food, or other expense screenshots.
* Extracting images associated with a particular date range.
* Organizing WhatsApp media before further processing by another tool.
* Reducing hundreds of exported images down to only the relevant ones.

NOTE : You must have written that keyword with the image or after it; otherwise, the tool won't be able to find all the images. I will be uploading a dummy WhatsApp export for you to test in the future.

Instead of manually searching through chat messages and finding images, the parser automatically identifies the relevant images and copies them into a separate folder for easy access.


## Usage

```bash
python whatsapp_parser.py <directory> <keyword> [options]
```

### Arguments

| Argument    | Description                                           |
| ----------- | ----------------------------------------------------- |
| `directory` | Root folder of the exported WhatsApp chat             |
| `keyword`   | Keyword to search for (e.g. `Advance`, `Gas`, `Food`) |

### Options

| Option               | Description                      |
| -------------------- | -------------------------------- |
| `-s`, `--start`      | Start date in format `YYYYMMDD`  |
| `-e`, `--end`        | End date in format `YYYYMMDD`    |
| `-f`, `--full-parse` | Run the complete parsing process |

## Examples

Parse all images related to "Advance":

```bash
python ./whatsapp_parser.py Advance
```

Parse images between two dates:

```bash
python ./whatsapp_parser.py Advance -s 20260601 -e 20260630
```

Run the complete parser:

```bash
python ./whatsapp_parser.py Advance -s 20260601 -e 20260630 -f
```

## How It Works

1. Moves all exported images into a working `Images` folder.
2. Parses the WhatsApp chat export.
3. Finds image references associated with the selected keyword.
4. Filters results by the provided date range.
5. Creates a folder inside `Images` named:

```text
<keyword>-<start>-<end>
```

6. Moves all matching images into that folder.

## Example Output

```text
Images/
├── Advance-20260601-20260630/
│   ├── IMG-20260607-WA0050.jpg
│   ├── IMG-20260614-WA0011.jpg
│   └── ...
```

## Future Plans

* OCR support for reading payment amounts
* Automatic calculation of totals
* CSV/Excel export

## Notes

This project was built as a personal learning project while learning:

* argparse
* os
* file handling

*This is a presonal project*

Expect Errors : Always keep a backup of your exported chat before running the parser.

*This README file was written by AI for now as I don't have the time to create one, I will be writing it myself in the future.*

*None of the code -Except this file- was written by AI but I did ask it for suggestions on how to do certain things. This is a learning project not a AI copy paste project.*
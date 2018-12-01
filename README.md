# py-abemails

This is a simple Python script to print a list of all of the e-mail addresses present in the Mac OS X Address Book.

Some export functionality is already built in to Address Book.  I wrote this script to be able to perform this conversion from the command line.

⚠️ **Notice:** This project is no longer maintained. It may have severe security or compatibility problems. Use it at your own risk!

## Usage

From the command line,

    python py-abemails.py [-f input-file] [output-file]

If no input file is specified, the script will use your Address Book database (~/Library/Application Support/AddressBook/AddressBook-v22.abcddb); this is almost certainly the file you want to use.

If no output file is specified, the script prints to stdout.

## Author

This script was written by [Benjamin Esham](https://esham.io).

This project is [hosted on GitHub](https://github.com/bdesham/py-abemails). It is **no longer being developed** and is left on GitHub only in the hope that someone will find the code interesting or useful.

## Version history

* 1.0.1 (2016-04-28)
    - You can now use “~” in the output filename to refer to your home directory.
* 1.0 (2011-06-18)
    - Initial release.

## License

Copyright © 2011, 2016 Benjamin D. Esham. This program is released under the ISC license, which you can find in the file LICENSE.md.

# py-abemails

This is a simple Python script to print a list of all of the e-mail addresses present in the Mac OS X Address Book.

Some export functionality is already built in to Address Book.  I wrote this script to be able to perform this conversion from the command line.

This script was written by [Benjamin Esham](http://www.bdesham.info) ([e-mail](mailto:bdesham@gmail.com)). The project page is [hosted on GitHub](https://github.com/bdesham/py-abemails).

## Usage

From the command line,

    python py-abemails.py [-f input-file] [output-file]

If no input file is specified, the script will use your Address Book database (~/Library/Application Support/AddressBook/AddressBook-v22.abcddb); this is almost certainly the file you want to use.

If no output file is specified, the script prints to stdout.

## Version history

* 1.0 (2011-06-18): Initial release.

## License

Copyright © 2011, Benjamin Esham.  This software is released under the following version of the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following condition: the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.**

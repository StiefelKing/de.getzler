#  MIT License
#
#  Copyright (c) 2020 Stefan Kätzlmeier
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of
#  the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
#  THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import configparser
import os
from shutil import copy


def changevalues():
    config["NAMEN"]["ABBILDSCANPFAD"] = "G:\\Notarstelle_Sonthofen\\_Gwg\\Scans_Ausweise\\"
    config["NAMEN"]["ABBILDSCANAKTION"] = "3"
    config["NAMEN"]["DOCIMPORTPFAD"] = "G:\\Notarstelle_Sonthofen\\_Gwg\\Scan_Transparenzregister_etc\\"
    config["NAMEN"]["DOCIMPORTAKTION"] = "3"


# read file
config = configparser.RawConfigParser()
config.optionxform = lambda option: option  # case sensitive
config.read(os.environ["Appdata"] + "\\Arnotop\\Arnotop.ini")
copy(os.environ["Appdata"] + "\\Arnotop\\Arnotop.ini",
     os.environ["Appdata"] + "\\Arnotop\\Arnotop - BU.ini")  # make backup

# change values
if config.remove_section("NAMEN"):
    config.add_section("NAMEN")
    changevalues()
else:
    config.add_section("NAMEN")
    changevalues()

# write file
with open(os.environ["Appdata"] + "\\Arnotop\\Arnotop.ini", 'w') as configfile:
    config.write(configfile)

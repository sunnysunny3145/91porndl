# Porndl

[![Build Status](https://travis-ci.org/iliul/porndl.svg?branch=dev)](https://travis-ci.org/iliul/porndl)

[Porndl](https://github.com/iliul/porndl) is a tiny command-line utility to download videos from the **91porn  site**(🔞). Personal use, fully script. u need to run it semi-auto.

Only support few of the website page based download due to the coding format. If it failed please go to https://weibomiaopai.com/online-video-download-helper/91porn to get all sub-files link and save it as a *.links input file. Then use it. Still under testing. 


# Getting Start

## Prerequisites

* [lxml](https://pypi.python.org/pypi/lxml/3.6.0)
* [requests](https://pypi.python.org/pypi/requests/)
* [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)
* ffmpeg

## Install via pip

```
$ git clone git@github.com:iliul/porndl.git
$ cd porndl
$ pip install -r requirements.txt
```

## Example

```
python porndl.py -f somelinks.links 
python porndl.py 'the video website page link(http://www.***.com/view_video.php?viewkey=********))'
```

# Usage

```
Usage: porndl [OPTION]... [URL]...

Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
  
Download options:
    -o | --output-dir <PATH>            Set output directory.
    -l | --ling-file <FILE>.               Set the *.link file as the download input
    -d | --debug                        Show traceback and other debug info.
```

# TODO

- [ ] support more coding format
- [ ] support more site
- [ ] support download progress bar

# References

1. **you-get** -- [https://github.com/soimort/you-get](https://github.com/soimort/you-get)
2. **proxy module** -- [https://github.com/soimort/you-get/pull/1063](https://github.com/soimort/you-get/pull/1063)
3. 91pron_python -- https://github.com/guobaby/91pron_python

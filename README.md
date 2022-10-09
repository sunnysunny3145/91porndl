# 91Porndl

[![Build Status](https://travis-ci.org/iliul/porndl.svg?branch=dev)](https://travis-ci.org/iliul/porndl)

[91Porndl](git@github.com:sunnysunny3145/91porndl.git) is a tiny command-line utility to download videos from the **91porn  site**(🔞). Personal use, fully script. u need to run it semi-auto.

Only support few of the website page based download due to the coding format. If it failed please refer to the method of getting playlist or m3u8.

# Getting Start

# Method of getting playlist or m3u8 link:

For getting the playlist:

go to https://weibomiaopai.com/online-video-download-helper/91porn to get all sub-files link and save it as a *.links input file. Then use it.

For getting the m3u8 link:

Using chrome browser, use F12 to enter the console. click the 'network' when video is playing. After applying the filter of 'ts', you will see few xxxxx.ts file with the header information of:

Request URL: https://la2.killcovid2021.com/m3u8/xxxxxx/ooooooo.ts

Then the corresponding m3u8 link would be like:

https://la2.killcovid2021.com/m3u8/xxxxxx/xxxxxx.m3u8

Use it as the input.

## Prerequisites

* [lxml](https://pypi.python.org/pypi/lxml/3.6.0)
* [requests](https://pypi.python.org/pypi/requests/)
* [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)
* ffmpeg

## Install via pip

```
$ git clone git@github.com:sunnysunny3145/91porndl.git
$ cd 91porndl
$ pip install -r requirements.txt
```

## Example

```
python porndl.py -f somelinks.links 
python porndl.py -p 'the video website page link(http://www.***.com/view_video.php?viewkey=********))'
python porndl.py -m wwww.https://la2.killcovid2021.com/m3u8/xxxx/xxxx.m3u8
```

# Usage

```
Usage: porndl [OPTION]... [URL]...

Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
  
Download options:
    -o | --output-dir <PATH>            Set output directory.
    -l | --link-file <FILE>             Set *.link file as input.
    -m | --m3u8 <ADDRESS>               Set m3u8 link as input. 
    -p | --play-site <ADDRESS>          Set play site link as input.  
```

# TODO

- [ ] support more coding format
- [ ] support more site
- [ ] support download progress bar

# References

1. **you-get** -- [https://github.com/soimort/you-get](https://github.com/soimort/you-get)
2. **proxy module** -- [https://github.com/soimort/you-get/pull/1063](https://github.com/soimort/you-get/pull/1063)
3. 91pron_python -- https://github.com/guobaby/91pron_python
4. [0x33e](https://github.com/0x33e)/**[porndl](https://github.com/0x33e/porndl)** -- https://github.com/0x33e/porndl

#!/usr/bin/env python3
# go to :
# https://weibomiaopai.com/online-video-download-helper/91porn 
# first
#
import re
import os
import sys
import getopt
import requests
import urllib.request
import urllib.error
from contextlib import closing 
import subprocess
import shutil
import os
proxies = {}
__version__ ="V1.0.0"
script_name = "porndl"

class ProgressBar(object):
    """
    link：https://www.zhihu.com/question/41132103/answer/93438156
    source：zhihu
    """
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/', chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】     %s     %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        """【razorback】 download finished 3751.50 KB / 3751.50 KB """
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)

def download_video_by_url(url, path, title, ext):
    outfile = '{}/{}.{}'.format(path, title, ext)
    urllib.request.urlretrieve(url, outfile)
    print(f'{url}: {outfile}')
    return True

def get_html(link_file):
    ff = open('mylist.txt','w')
    ff.close()
    with open(link_file,'r') as f:
        download_url = f.readline()
        cnt = 0
        while((download_url!='')&(cnt < 1000)):
            cnt+=1
            print(download_url) 
            outfile = '{}/{}.{}'.format(output_dir, f'{cnt}', 'ts')
            try:
                if download_video_by_url(download_url, output_dir, f'{cnt}', 'ts'):    
                    print('Processing download successful !!! Enjoy it !!!')
                    with open('mylist.txt','a') as ff:
                        ff.write(f'file \'{outfile}\'\n')
            except KeyboardInterrupt:
                raise
            except urllib.error.HTTPError:
                print(f'not valid link: {download_url}')
            download_url = f.readline()

def parse_args(script_name, **kwargs):

    help = 'Usage: %s [OPTION]... [URL]...\n\n' % script_name
    help += '''Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
    \n'''
    help += '''Download options:
    -o | --output-dir <PATH>            Set output directory.
    -a | --auto-proxy                   Auto choice an Chinese HTTP proxy.
    -c | --cookies <COOKIES_FILE>       Load cookies.txt or cookies.sqlite.
    -x | --http-proxy <HOST:PORT>       Use an HTTP proxy for downloading.
    -s | --socks-proxy <HOST:PORT>      Use an SOCKS proxy for downloading.
    -d | --debug                        Show traceback and other debug info.
    '''

    short_opts = 'Vhdac:o:x:s:'
    opts = ['version', 'help', 'debug', 'auto-proxy', 'cookies=', 'output-dir=', 'http-proxy=', 'socks-proxy=']

    # Get options and arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print("try 'porndl --help' for more options")
        sys.exit(2)

    global traceback
    global auto_proxy
    global output_dir

    output_dir = './downloads'
    traceback = False
    auto_proxy = False

    for o, a in opts:
        if o in ("-V", "--version"):
            print('porndl version : {}'.format(__version__))
            sys.exit()
        elif o in ("-h", "--help"):
            print(help)
            sys.exit()
        elif o in ('-c', '--cookies'):
            print('cookies is {}'.format(a))
        elif o in ('-d', '--debug'):
            traceback = True
        elif o in ('-a', '--auto-proxy'):
            auto_proxy = True
        elif o in ("-o", "--output-dir"):
            output_dir = a
        elif o in ("-x", "--http-proxy"):
            proxies['http'] = 'http://' + a
            proxies['https'] = 'https://' + a
        elif o in ("-s", "--socks-proxy"):
            proxies['http'] = 'socks5://' + a
            proxies['https'] = 'socks5://' + a
        else:
            print("try 'porndl --help' for more options")
            sys.exit(2)

    if not args:
        print(help)
        sys.exit()
    print(f'args: ${args}\n')
    get_html(args[0])
    #ffmpeg -f concat -safe 0 -i mylist.txt -c copy merged.mp4
    subprocess.call('ffmpeg -f concat -safe 0 -i mylist.txt -c copy merged.mp4', shell=True)
    #testmerge()

def testmerge():
    cwd = os.getcwd()
    TS_DIR = 'downloads'
    with open('merged.ts', 'wb') as merged:
        for ts_file in os.listdir(f'{cwd}/{TS_DIR}'):
            print(ts_file)
            with open(f'{cwd}/{TS_DIR}/{ts_file}', 'rb') as mergefile:
                shutil.copyfileobj(mergefile, merged)


def main(**kwargs):
    parse_args('porndl', **kwargs)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# go to :
# https://weibomiaopai.com/online-video-download-helper/91porn 
# first
#
from lib2to3.pgen2.pgen import generate_grammar
import re
import os
import sys
import getopt
import requests
import requests.packages.urllib3
import urllib.request
import urllib.error
from contextlib import closing 
import subprocess
import shutil
import os
import random
from bs4 import BeautifulSoup
import js2py
from urllib.parse import urlparse
import m3u8

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

class porndl:
    def __init__(self, download_loc) -> None: 
        self.proxies = {}
        requests.packages.urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
        self.s = requests.session()
        self.s.keep_alive = False # 关闭多余连接
        self.tmp_loc = './tmp'
        shutil.rmtree(self.tmp_loc)
        os.makedirs(self.tmp_loc)
        self.download_loc = download_loc
        if not os.path.exists(download_loc):
            os.makedirs(download_loc)

    def download_video_by_url(self, url, title, ext, loc = ''):
        if not loc:
            loc = self.download_loc
        outfile = '{}/{}.{}'.format(loc, title, ext)
        urllib.request.urlretrieve(url, outfile)
        print(f'{url}: {outfile}')
        return True

    def convert_ts2mp4(self, title):
        subprocess.call(f'ffmpeg -f concat -safe 0 -i mylist.txt -c copy {self.download_loc}/{title}.mp4', shell=True)

    def download_ts(self, ts_list): 
        f = open("mylist.txt", "w")
        f.close()
        for cnt, download_url in enumerate(ts_list): 
            outfile = '{}/{}.{}'.format(self.tmp_loc, f'{cnt}', 'ts')
            try:
                if self.download_video_by_url(download_url, f'{cnt}', 'ts', self.tmp_loc):    
                    print(f'Processing {cnt} and {download_url} download successful!')
                    with open('mylist.txt','a') as ff:
                        ff.write(f'file \'{outfile}\'\n')
            except KeyboardInterrupt:
                raise
            except urllib.error.HTTPError:
                print(f'not valid link: {download_url}')

    def get_video_by_ts_files(self, link_file):
        ff = open('mylist.txt','w')
        ff.close()
        ts_list = []
        with open(link_file,'r') as f:
            download_url = f.readline()
            ts_list.append(download_url)
        if ts_list:
            self.download_ts(ts_list)
            self.convert_ts2mp4(ts_list[0])
        else:
            print('empty file.')
            sys.exit(2)


    def get_url_from_listpage(self):
        page_url = 'http://www.91porn.com/index.php'
        #parse_args('porndl', **kwargs)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
                'Referer': 'http://91porn.com'}
        get_page=self.s.get(url=page_url, headers=headers)
        print(get_page.text)
        div = BeautifulSoup(get_page.text, "html.parser").find_all("div",class_="well well-sm videos-text-align")
        viewurl = []
        for i in div: 
            viewurl.append(i.a.attrs["href"])
            pass
        print(viewurl)

    def random_ip(self):
        a=random.randint(1, 255)
        b=random.randint(1, 255)
        c=random.randint(1, 255)
        d=random.randint(1, 255)
        return (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))

    def filter_str(self, desstr, restr=''):
        # filter all characters exculding chinese, english, and number. 
        res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
        title = res.sub(restr, desstr).replace("Chinesehomemadevideo","")
        return title 

    def download_m3u8_by_url(self, url, title):  
        playlist = m3u8.load(url)
        ts_list = []
        for i in playlist.segments: 
            print(i.base_uri + i.uri) 
            ts_list.append(i.base_uri + i.uri) 
        self.download_ts(ts_list)
        self.convert_ts2mp4(title)

    def download_video_from_playpage(self, page_url):
        headers={'Accept-Language':'zh-CN,zh;q=0.9',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
                        'X-Forwarded-For': self.random_ip(),
                        'referer': page_url,
                        'Content-Type': 'multipart/form-data; session_language=cn_CN',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        }
        base_req = self.s.get(url=page_url,headers=headers)
        encodedata2 = open("strencode2.js",'r',encoding= 'utf8').read()
        encodedata1 =  open("strencode.js",'r',encoding= 'utf8').read()
        strencode2 = js2py.eval_js(encodedata2)
        strencode = js2py.eval_js(encodedata1)  
        a = re.compile('document.write\(strencode2\("(.*)"').findall(base_req.content.decode('utf-8'))
        print(base_req.content.decode('utf-8'))
        if len(a)>0:
            a = a[0].split(',')
            text = a[0].replace('"', '')
            print(text)
            print('********************')
            print(strencode2(text))
            url = BeautifulSoup(strencode2(text), "html.parser").source.attrs['src']
        else:
            a= re.compile('document.write\(strencode\("(.*)"').findall(base_req.content.decode('utf-8'))
            text = a[0].split(',')
            url = BeautifulSoup(strencode(text[0].replace('"', ''),text[1].replace('"', ''),text[2].replace('"', '')), "html.parser").source.attrs['src']
        title = BeautifulSoup(base_req.text, "html.parser").title.text.replace(" ","").replace("\n","")
        title = self.filter_str(title)
        videotype = urlparse(url).path.split(".")[1]
        if videotype == "m3u8":
            self.download_m3u8_by_url(url, title)
        else:
            self.download_video_by_url(url, title, '.mp4')
        
def parse_args(script_name, **kwargs):

    help = 'Usage: %s [OPTION]... [URL]...\n\n' % script_name
    help += '''Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
    \n'''
    help += '''Download options:
    -o | --output-dir <PATH>            Set output directory.
    -l | --link-file <FILE>             Set *.link file as input.
    -m | --m3u8 <ADDRESS>               Set m3u8 link as input. 
    -p | --play-site <ADDRESS>          Set play site link as input.  
    '''

    short_opts = 'Vhdac:o:l:m:p'
    opts = ['version', 'help', 'output-dir=', 'link-file', 'm3u8', 'play-site']
    download_loc = './downloads'
    link_file = ''
    m3u8_link = ''
    play_site = '' 
    # Get options and arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print("try 'porndl --help' for more options")
        sys.exit(2)

    for o, a in opts:
        if o in ("-V", "--version"):
            print('porndl version : {}'.format(__version__))
            sys.exit()
        elif o in ("-h", "--help"):
            print(help)
            sys.exit()
        elif o in ('-c', '--cookies'):
            print('cookies is {}'.format(a))
        elif o in ("-o", "--output-dir"):
            download_loc = a 
        elif o in ("-l", "--link-file"):
            link_file = a  
        elif o in ("-m", "--m3u8"):
            m3u8_link = a   
        elif o in ("-p", "--playsite"):
            play_site = a   
        else:
            print("try 'porndl --help' for more options")
            sys.exit(2)

    if (not link_file) & (not m3u8_link) & (not play_site):
        print(help)
        sys.exit()
    
    pl = porndl(download_loc)
    if play_site:
        pl.download_video_from_playpage(play_site)
    elif m3u8_link:
        pl.download_m3u8_by_url(m3u8_link, m3u8_link.split('/')[-1])
    elif link_file:
        pl.get_video_by_ts_files(link_file)  

def main(**kwargs):
    parse_args('porndl', **kwargs)

if __name__ == "__main__":
    main()

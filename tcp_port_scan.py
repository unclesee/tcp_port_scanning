#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import threading
from queue import Queue

lock = threading.Lock()
q = Queue()
NUM_WORKERS = 1024
socket.setdefaulttimeout(1)

class Deep_port(threading.Thread):
    def __init__(self, num, ip, port):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.thread_stop = False
        self.ip = ip
        self.port = port

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            child = s.connect_ex((self.ip, self.port))
            if child == 0:
                lock.acquire()
                pt_list.append(self.port)
                lock.release()
            s.close()
        except Exception as e:
            print(e)


def main(ip):
    global  pt_list
    pt_list = []
    for p in range(1, 1024):
        q.put(p)
    while not q.empty():
        res = threading.enumerate()
        for i in range(NUM_WORKERS):
            port = q.get()
            if port:
                thread = Deep_port(i, ip, port)
                thread.start()
            if q.empty():
                break
    return pt_list




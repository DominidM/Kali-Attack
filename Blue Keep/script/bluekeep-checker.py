#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: David Espejo (Fortytwo Security)
import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_bluekeep_vuln(target_ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target_ip, 3389))
        pre_auth_pkt = b"\x03\x00\x00\x13\x0e\xe0\x00\x00\x00\x00\x00\x00\x00\x01\x00\x08\x00\x03\x00\x00\x00"
        sock.send(pre_auth_pkt)
        data = sock.recv(1024)
        if b"\x03\x00\x00\x0c" in data:
            return f"[+] {target_ip} is likely VULNERABLE to BlueKeep!"
        else:
            return f"[-] {target_ip} is likely patched :("
    except:
        return f"[-] {target_ip} is either not up or not vulnerable"

def scan_ips(targets):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_bluekeep_vuln, target) for target in targets]

        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targets", required=True, nargs='+', help="List of target IP addresses separated by space")
    args = parser.parse_args()
    scan_ips(args.targets)

#!/usr/bin/env python3
"""BUNNY RAMDISK - Passcode/Activation RESTORE (standalone CLI).

Restores activation files from a backup zip onto the SSH ramdisk (device must
be booted to ramdisk with filesystems mounted), runs restore.sh + skip_setup,
then reboots the device to normal iOS.

Usage:
  python3 bunny_restore.py /path/to/0x<ECID>.zip
"""
import importlib.util
import os
import sys
import time

CORE = '/Users/bunny.cia/Documents/BUNNY RAMDISK/BUNNY RAMDISK 2.app/Contents/Resources/core.py'
spec = importlib.util.spec_from_file_location('bunnycore', CORE)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def log(kind, msg):
    ts = time.strftime('%H:%M:%S')
    tag = {'ok': 'OK  ', 'error': 'ERR ', 'warn': 'WARN', 'info': 'INFO',
           'big': 'BIG ', 'bypass': 'BYP ', 'mount': 'MNT '}.get(kind, '    ')
    print('%s [%s] %s' % (ts, tag, msg), flush=True)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 bunny_restore.py /path/to/0x<ECID>.zip', flush=True)
        sys.exit(2)
    zip_path = sys.argv[1]
    print('=== BUNNY RAMDISK - RESTORE ===', flush=True)
    ok = core.do_restore(zip_path, log)
    log('big', 'RESULT: %s' % ('RESTORE OK' if ok else 'RESTORE FAILED'))
    sys.exit(0 if ok else 1)

#!/usr/bin/env python3
"""BUNNY RAMDISK - Passcode/Activation BACKUP (standalone CLI).

Pulls activation files from the SSH ramdisk (device must be booted to ramdisk
with filesystems mounted) and saves a backup zip:
  ~/Library/Application Support/BUNNY RAMDISK/Backup/0x<ECID>.zip

Usage:
  python3 bunny_backup.py
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
    print('=== BUNNY RAMDISK - BACKUP ===', flush=True)
    path = core.pull_backup(log)
    if not path:
        log('error', 'BACKUP FAILED')
        sys.exit(1)
    log('big', 'BACKUP OK: %s' % path)
    sys.exit(0)

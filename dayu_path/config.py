#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

import re

# 用于判断frame 的正则表达式
FRAME_REGEX = re.compile(r'.*?(?<![\dvV])(\d{2,})$')
# 用于判断系列化类型文件名的正则表达式
PATTERN_REGEX = re.compile(r'.*(\%(\d*)d).*|.*?(#+)|.*(\$F(\d*))')
# 用于小写化 windows 盘符的正则表达式
WIN32_DRIVE_REGEX = re.compile(r'^(\w:).*')

VERSION_REGEX = re.compile(r'.*([vV]\d+).*')

EXT_SINGLE_MEDIA = {'.mov': {},
                    '.mp4': {},
                    '.avi': {},
                    '.r3d': {},
                    }

SCAN_IGNORE = {'start': ('.', '..', 'Thumb'),
               'end'  : ('.tmp')}

NETWORK_FILE_SYSTEM = ('nfs', 'smbfs', 'remote', 'afp', 'ftp', 'snfs')
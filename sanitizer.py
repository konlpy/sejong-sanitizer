#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from codecs import open
from glob import glob
import re

from lxml import html


def _sanitize(filename, pos=True):
    with open(filename, 'r', encoding='utf-16') as f:
        text = f.read()

    if pos:
        pattern = '(.+?/\w+)\+?'
    else:
        pattern = '(.+?)/\w+\+?'

    root = html.fromstring(text)
    sentences = root.xpath('//text/u/s/text()')

    for sentence in sentences:
        for line in sentence.split('\n'):
            items = line.split('\t')  # id + word + morphemes
            if len(items) == 3:
                word = items[1]
                morphs = re.findall(pattern, items[2])
                yield [word, ' '.join(morphs)]


def sanitize(input_files, output_file, pos=True):
    with open(output_file, 'w', encoding='utf8') as f:
        for filename in input_files:
            print filename
            for row in _sanitize(filename, pos=pos):
                if len(row) == 2:
                    f.write('\t'.join(row))
                    f.write('\n')


if __name__ == '__main__':
    basedir = './sejong/cd1/02_말뭉치/현대/구어/현대구어_말뭉치/형태분석_말뭉치'
    input_files = glob(basedir + '/*')
    print len(input_files)

    sanitize(input_files, 'output/word_to_morph.txt', pos=False)
    sanitize(input_files, 'output/word_to_morphpos.txt', pos=True)

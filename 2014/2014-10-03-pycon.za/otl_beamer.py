#!/usr/bin/env python

import fileinput
import re


def e(text):
    text = re.sub(r'([&[\]_%])', r'\\\1', text)
    text = re.sub(r'~', r'$\\sim$', text)
    text = re.sub(r'([<>])', r'$\1$', text)
    text = re.sub(r'(http:[^ ,]*)', r'\\url{\1}', text)
    return text


def output_beamer(frame, level):
    text = frame['text']
    children = frame['children']
    parent = frame['parent']

    if level == 0:
        print
        print r'\section{%s}' % e(text)
        if not children:
            print
            print r'\begin{frame}{%s}' % e(text)
            print '  \[VAMP\]'
            print r'\end{frame}'
    elif level == 1:
        print
        print r'\begin{frame}{%s}' % e(parent['text'])
        print r'  \Huge %s' % e(text)
        print r'\end{frame}'
    elif level == 2:
        if not children:
            print
            print r'\begin{frame}{%s}' % e(parent['text'])
            print r'  \huge %s' % e(text)
            print r'\end{frame}'
    elif level == 3:
        print
        print r'\begin{frame}{%s}' % e(parent['text'])
        print r'  \Large %s' % e(text)
        if children:
            print r'  \begin{itemize}'
            for child in children:
                print r'    \item<1> %s' % e(child['text'])
            print r'  \end{itemize}'
        print r'\end{frame}'

    if level < 3 and children:
        for child in children:
            output_beamer(child, level + 1)


def main():
    stack = {
        'children': [],
    }
    for line in fileinput.input():
        line = line.rstrip()
        if line == 'END':
            break
        indent, text = re.match(r'^(\t*)(.*)', line).groups()
        indent = len(indent)
        parent = stack
        for i in range(indent):
            parent = parent['children'][-1]
        frame = {
            'text': text,
            'children': [],
            'parent': parent,
        }
        parent['children'].append(frame)

    for section in stack['children']:
        output_beamer(section, 0)

if __name__ == '__main__':
    main()

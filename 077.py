#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import Counter


def main():
    c = Counter()
    for line in sys.stdin:
        label, prediction, _ = line.split('\t')
        pair = (label, prediction)
        if pair == ('+1', '+1'):
            c['TP'] += 1
        elif pair == ('+1', '-1'):
            c['FN'] += 1
        elif pair == ('-1', '+1'):
            c['FP'] += 1
        elif pair == ('-1', '-1'):
            c['TN'] += 1

    TPTN = c['TP'] + c['TN']
    TPFPFNTN = sum(c.itervalues())
    print 'Accuracy: {:.4} ({}/{})'.format(float(TPTN) / TPFPFNTN, TPTN, TPFPFNTN)
    TPFP = c['TP'] + c['FP']
    TPFN = c['TP'] + c['FN']
    P = float(c['TP']) / TPFP
    R = float(c['TP']) / TPFN
    print 'Micro P, R, F1: {:.4} ({}/{}), {:.4} ({}/{}), {:.4}'.format(
        P, c['TP'], TPFP, R, c['TP'], TPFN, 2 * P * R / (P + R))

# Accuracy: 0.915 (9754/10660)
# Micro P, R, F1: 0.9174 (4862/5300), 0.9122 (4862/5330), 0.9148

if __name__ == '__main__':
    main()

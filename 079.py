#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve


def main():
    probabilities = np.loadtxt('076.txt')
    precision, recall, threshold = precision_recall_curve(
        probabilities[:, 0], probabilities[:, 2])
    plt.plot(recall, precision)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.savefig('079.png')

# http://www.cl.ecei.tohoku.ac.jp/~ryo-t/nlp100/079.png


if __name__ == '__main__':
    main()

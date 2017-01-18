#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

    「パトカー」＋「タクシー」の文字を先頭から交互に連結して
    文字列「パタトクカシーー」を得よ．
    """
    print ''.join([''.join(v) for v in zip(u'パトカー', u'タクシー')])


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Sekunden-zu-HH:MM:SS" data-toc-modified-id="Sekunden-zu-HH:MM:SS-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Sekunden zu HH:MM:SS</a></span></li></ul></div>
# ### Sekunden zu HH:MM:SS
def secToHHMMSS(seconds):
    """
    takes seconds and prints them in HH:MM:SS format.
    
    :param seconds: int
    """
    seconds = int(seconds)
    H = seconds // (60*60)
    seconds = seconds % (60*60)
    M = seconds // 60
    seconds = seconds % 60
    S = seconds
    print("{:02d}:{:02d}:{:02d}".format(H,M,S))
# Alternatively:
def secToHHMMSS(seconds):
    """
    takes seconds and prints them in HH:MM:SS format.
    
    :param seconds: int
    """
    seconds = int(seconds)
    H = seconds // (60*60)
    M = seconds // 60 - H*60
    seconds = seconds % 60
    S = seconds
    print("{:02d}:{:02d}:{:02d}".format(H,M,S))
secToHHMMSS(1)
secToHHMMSS(70)
secToHHMMSS(60)
secToHHMMSS(60*60)
secToHHMMSS(60*60*24)

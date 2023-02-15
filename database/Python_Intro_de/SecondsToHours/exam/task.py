def secToHHMMSS(seconds):
    """
    Wandelt eine Eingabe seconds in das Format HH:MM:SS um und gibt dieses zurueck.
    
    Examples
    --------
    >>> secToHHMMSS(150)
    "00:02:30"
    
    """
    seconds = int(seconds)
    H = seconds // (60*60)
    M = seconds // 60
    S = seconds
    return "{:02d}:{:02d}:{:02d}".format(H,M,S)
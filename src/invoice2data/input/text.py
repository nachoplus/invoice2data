# -*- coding: utf-8 -*-
def to_text(path):
    """Null input wrapper. Processe TXT files instead of PDF ones.

    Parameters
    ----------
    path : str
        path of electronic invoice in txt

    Returns
    -------
    out : str
        returns extracted text from txt

    """
    import subprocess
    from distutils import spawn  # py2 compat

    out, err = subprocess.Popen(
            ["cat", path], stdout=subprocess.PIPE
    ).communicate()
    return out

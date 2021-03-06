#!/usr/bin/env python3

version_ = '2020SEP29T1026  v0.08'  # check_mkpy3_v5.py

# Kenneth John Mighell
# Kepler Support Scientist
# Kepler / K2 Science Office
# NASA Ames Research Center / SETI Institute


if (__name__ == '__main__'):
    """
Purpose: Unit tests for mkpy3  (https://github.com/KenMighell/mkpy3)

# Kenneth John Mighell
# Kepler Support Scientist
# Kepler / K2 Science Office
# NASA Ames Research Center / SETI Institute
    """
    import os
    import glob
    import subprocess
    #
    # ASCII color codes
    CEND = '\33[0m'
    CRED = '\33[31m'
    #
    cwd = os.getcwd()
    print(cwd, ' =$PWD')
    good = 0
    bad = 0
    filel = sorted(glob.glob('./mkpy3*.py'))
    sz = len(filel)
    print()
    print(sz, 'files to check')
    print()
    for k, name in enumerate(filel, start=1):
        print('[%d] %s : ' % (k, name.strip()), end='')
        result = subprocess.run(['python3', name], capture_output=True)
        returncode = result.returncode
        if (returncode != 0):
            bad += 1
            print(CRED + '***** ERROR FOUND *****' + CEND)
            print()
        else:
            good += 1
            print('OK')
        # pass:if
    # pass:for
    print()
    if (good == sz):
        print('\nAll %d files PASS  :-)' % good)
    else:
        print('%d of %d files FAIL  8=X' % (bad, sz))
    # pass:if
    print()
# pass:if
# EOF

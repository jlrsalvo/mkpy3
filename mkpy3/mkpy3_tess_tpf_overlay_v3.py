#!/usr/bin/env python3

# file://mkpy3_tess_tpf_overlay_v3.py

__version__ = '2020AUG22T0744 0.37'

# Kenneth John Mighell
# Kepler Support Scientist
# Kepler / K2 Science Office
# NASA Ames Research Center / SETI Institute


# PEP8:OK


# check local setup ===========================================================
import sys
pyver = (sys.version_info.major*10) + (sys.version_info.minor)
if (pyver < 27):
    print('*** ERROR *** Needs Python 2.7 or higher.')
    sys.exit(1)
# pass:if
try:
    import lightkurve as lk
except Exception:
    print('\n***** ERROR *****\n')
    print('The Python package lightkurve needs to be installed.\n')
    print('This is the installation command for lightkurve using pip:\n')
    print('pip install lightkurve --upgrade\n')
    print('For further installation details see the lightkurve homepage:\n')
    print('https://docs.lightkurve.org/about/install.html\n')
    sys.exit(1)
# pass:try
del sys
del lk

###############################################################################


def mkpy3_tess_tpf_overlay_v3(
    tpf=None,
    frame=0,
    survey='2MASS-J',
    width_height_arcmin=6.0,
    shrink=1.0,
    show_plot=True,
    plot_file='mkpy3_plot.png',
    overwrite=False,
    figsize_str='[9,9]',
    title=None,
    percentile=99.5,
    cmap='gray_r',
    colors_str="[None,'dodgerblue','red']",
    lws_str='[0,3,4]',
    zorders_str='[0,1,2]',
    marker_kwargs_str="{'edgecolor':'yellow', 's':600, 'facecolor':'None', "
    "'lw':3, 'zorder':10}",  # or 'None'
    print_gaia_dr2=True,
    gaia_dr2_kwargs_str="{'edgecolor':'cyan', 's':150, 'facecolor':'None', "
    "'lw':3, 'zorder':20}",  # or 'None'
    print_vsx=True,
    vsx_kwargs_str="{'s':900, 'color':'lawngreen', 'marker':'x', 'lw':5, "
    "'zorder':30}",  # or 'None'
    sexagesimal=False,
    verbose=False
):
    """
Function: mkpy3_tess_tpf_overlay_v3()

Purpose: Plot a TESS TargetPixelFile (TPF) overlay on a sky survey image.

Parameters
----------
tpf : (lightkurve TargetPixelFile object) (optional)
    A lightkurve TargetPixelFile (TPF) object.
    [default: None]
frame : (int) (optional)
    Frame number to use.
    [range: 0 to number of cadences in the TPF minus 1]
    [default: 0]
survey : (str) (optional)
    A sky survey name.
    [default: '2MASS-J'] [verified: '2MASS-J', 'DSS2 Red']
width_height_arcmin : (float) (optional)
    Width and height of the survey image [arcmin].
    [default: 6.0]
shrink : (float) (optional)
    Survey search radius shrink factor.
    [range: 0.0 to 1.0]
    [default: 1.0]
show_plot : (bool) (optional)
    If True, show the plot.
    [default=True]
plot_file : (str) (optional)
    Filename of the output plot.
    [default: 'mkpy3_plot.png']
overwrite : (bool) (optional)
    If True, overwrite ("clobber") an existing output file.
    If False, do *not* create output file when plot_file != 'mkpy3_plot.png'.
    [default: False]
figsize_str : (str) (optional)
    A string of a 2-time list of figure widht and height [Matplotlib].
    [default: '[9,9]']
title : (str) (optional)
    Title of the plot.
    If None, a title will be created.
    An empty string ('') will produce a blank title.
    [default: None]
percentile : (float) (optional)
    Percentile [percentage of pixels to keep] used to set the colorbar.
    [range: 0.0 to 100.0]
    [default: 99.5]
cmap : (str) (optional)
    Colormap name [Matplotlib].
    [default: 'gray_r']
colors_str : (str) (optional)
    A string of a 3-item list of overlay color names [Matplotlib].
    [default: "['None','dodgerblue','red']"]
lws_str : (str) (optional)
    A string of a 3-item list of overlay line widths [Matplotlib].
    [default: '[0,3,4]']
zorders_str : (str) (optional)
    A string of a 3-item list of overlay zorder values [Matplotlib].
    [default: '[0,1,2]']
marker_kwargs_str : (str) (optional)
    A string of a dictionary of arguments for ax.scatter() [Matplotlib].
    The target is marked according to the kwarg values.
    If set to None, the target is *not* marked.
    [default: "{'edgecolor':'yellow', 's':600, 'facecolor':'None', 'lw':3,
    'zorder':10}"]
print_gaia_dr2 : (bool) (optional)
    If True, print the GAIA DR2 catalog results.
    [default=True]
gaia_dr2_kwargs_str : (str) (optional)
    A string of a dictionary of arguments for ax.scatter() [Matplotlib].
    GAIA DR2 stars are marked accordinbg to the kwarg values.
    If set to None, no GAIA DR2 data are shown and plotted.
    [default: "{'edgecolor':'cyan', 's':150, 'facecolor':'None', 'lw':3,
    'zorder':20}"]
print_vsx : (bool) (optional)
    If True, print the VSX catalog results.
    [default=True]
vsx_kwargs_str : (str) (optional)
    A string of a dictionary of arguments for ax.scatter() [Matplotlib].
    VSX varaible stars are marked accordinbg to the kwarg values.
    If set to None, no VSX data are shown and plotted.
    [default: "{'s':900, 'color':'lawngreen', 'marker':'x', 'lw':5,
    'zorder':30}"]
sexagesimal : (bool) (optional)
    If True, print catalog positions as sexagesimal [hms dms].
    [default=False]
verbose : (bool) (optional)
    If True, print extra information.
    [default: False]

Returns
-------
ax : (matplotlib axes object) or (None)
    A matplotlib axes object *if* show_plot is False *else* None .

# Kenneth John Mighell
# Kepler Support Scientist
# Kepler / K2 Science Office
# NASA Ames Research Center / SETI Institute
    """
    import mkpy3_tpf_overlay_v4 as km1

    ax = km1.mkpy3_tpf_overlay_v4(
        tpf=tpf,
        frame=frame,
        survey=survey,
        width_height_arcmin=width_height_arcmin,
        shrink=shrink,
        show_plot=show_plot,
        plot_file=plot_file,
        overwrite=overwrite,
        figsize_str=figsize_str,
        title=title,
        percentile=percentile,
        cmap=cmap,
        colors_str=colors_str,
        lws_str=lws_str,
        zorders_str=zorders_str,
        marker_kwargs_str=marker_kwargs_str,
        print_gaia_dr2=print_gaia_dr2,
        gaia_dr2_kwargs_str=gaia_dr2_kwargs_str,
        print_vsx=print_vsx,
        vsx_kwargs_str=vsx_kwargs_str,
        sexagesimal=sexagesimal,
        verbose=verbose)

    return ax
# pass:def

###############################################################################


def str2bool(v):
    import argparse
    """
Utility function for argparse.
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    # pass:if
# pass:def

###############################################################################


def check_file_exists(filename, overwrite):
    """
Utility function.
    """
    assert(isinstance(filename, str))
    assert(isinstance(overwrite, bool))
    msg = 'Requested output file already exists (overwrite=False):\n'
    if (not overwrite):
        if (os.path.isfile(filename)):
            print('\n***** ERROR *****\n\n%s' % (msg))
            print("new_filename='%s'\n" % filename)
            sys.exit(1)
        # pass:if
    # pass:if
# pass:def

###############################################################################


if (__name__ == '__main__'):
    import os
    import sys
    import ntpath
    import argparse
    import ast
    import lightkurve as lk
    #
    #
    # ===== argparse:BEGIN ====================================================
    #
    parser = argparse.ArgumentParser()
    #
    parser.add_argument(
        '--tpf_filename', action="store", type=str, default=None,
        help="Filename of the Target Pixel File (TPF) [default: None]")
    parser.add_argument(
        '--frame', action="store", type=int, default=0,
        help='Frame number (integer) [default: 0]')
    parser.add_argument(
        '--survey', action="store", type=str, default='2MASS-J',
        help="Survey name (str) [default: '2MASS-J']")
    parser.add_argument(
        '--width_height_arcmin', action="store", type=float, default=6.0,
        help='Width and height size in arcmin (float) [default: 6.0]')
    parser.add_argument(
        '--shrink', type=float, default=1.0,
        help='Survey search radius shrink factor (float) [default: 1.0]')
    parser.add_argument(
        '--show_plot', type=str2bool, default=True,
        help='If True, show the plot [default=True]')
    parser.add_argument(
        '--plot_file', action="store", type=str, default='mkpy3_plot.png',
        help='Filename of the output plot [default: "mkpy3_plot.png"]')
    parser.add_argument(
        '--overwrite', type=str2bool, default=False,
        help='If True, overwrite ("clobber") an existing output file '
        '[default: False]')
    parser.add_argument(
        '--figsize_str', action="store",
        type=ast.literal_eval, default="[9,9]",
        help="string of a 2-item list of figure width and height [Matplotlib] "
        "(str) [default: '[9,9]'")
    parser.add_argument(
        '--title', action="store", type=str, default=None,
        help='Title of the finder chart (str) [default: None]')
    parser.add_argument(
        '--percentile', action="store", type=float, default=99.5,
        help='Percentile [percentage of pixels to keep: 0.0 to 100.0] '
        '(float) [default: 99.5]')
    parser.add_argument(
        '--cmap', action="store", type=str, default=None,
        help="Colormap name [Matplotlib] (str) [default: 'gray_r']")
    parser.add_argument(
        '--colors_str', action="store",
        type=ast.literal_eval, default="[None,'dodgerblue','red']",
        help="string of a 3-item list of overlay color names [Matplotlib] "
        "(str) [default: \"['None','dodgerblue','red']\"")
    parser.add_argument(
        '--lws_str', action="store",
        type=ast.literal_eval, default="[0,3,4]",
        help="string of a 3-item list of overlay line widths [Matplotlib] "
        "(str) [default: \"[0,3,4]\"")
    parser.add_argument(
        '--zorders_str', action="store",
        type=ast.literal_eval, default="[0,1,2]",
        help="string of a 3-item list of overlay zorder values [Matplotlib] "
        "(str) [default: \"[0,1,2]\"")
    kwargs_ = "{'edgecolor':'yellow', 's':600, 'facecolor':'None', 'lw':3, "\
        "'zorder':10}"
    parser.add_argument(
        '--marker_kwargs_str', action="store",
        type=ast.literal_eval, default=kwargs_,
        help="marker kwargs (string of a dictonary) for ax.scatter() "
        "[Matplotlib] "+'(str) [default: "' + kwargs_ + '"')
    kwargs_ = "{'edgecolor':'cyan', 's':150, 'facecolor':'None', 'lw':3, "\
        "'zorder':20}"
    parser.add_argument(
        '--print_gaia_dr2', type=str2bool, default=True,
        help='If True, print the GAIA DR2 catalog results [default=True]')
    parser.add_argument(
        '--gaia_dr2_kwargs_str', action="store",
        type=ast.literal_eval, default=kwargs_,
        help="GAIA DR2 marker kwargs (string of a dictonary) for ax.scatter() "
        "[Matplotlib] "'(str) [default: "' + kwargs_ + '"')
    kwargs_ = "{'s':900, 'color':'lawngreen', 'marker':'x', 'lw':5, "\
        "'zorder':30}"
    parser.add_argument(
        '--print_vsx', type=str2bool, default=True,
        help='If True, print the VSX catalog results [default=True]')
    parser.add_argument(
        '--vsx_kwargs_str', action="store",
        type=ast.literal_eval, default=kwargs_,
        help="VSX marker kwargs (string of a dictonary) for ax.scatter() "
        "[Matplotlib] (str) [default: '" + kwargs_ + "'")
    parser.add_argument(
        '--sexagesimal', type=str2bool, default=False,
        help='Print catalog positions as sexagesimal [hms dms] if True (bool) '
        '[default=False]')
    parser.add_argument(
        '--verbose', type=str2bool, default=False,
        help='Print extra information if True (bool) [default=False]')
    #
    args = parser.parse_args()
    #
    # ===== argparse:END ======================================================
    #

    tpf_filename = args.tpf_filename
    frame = args.frame
    survey = args.survey
    width_height_arcmin = args.width_height_arcmin
    shrink = args.shrink
    show_plot = args.show_plot
    plot_file = args.plot_file
    overwrite = args.overwrite
    figsize_str = str(args.figsize_str)
    title = args.title
    percentile = args.percentile
    cmap = args.cmap
    colors_str = str(args.colors_str)
    lws_str = str(args.lws_str)
    zorders_str = str(args.zorders_str)
    marker_kwargs_str = str(args.marker_kwargs_str)
    print_gaia_dr2 = args.print_gaia_dr2
    gaia_dr2_kwargs_str = str(args.gaia_dr2_kwargs_str)
    print_vsx = args.print_vsx
    vsx_kwargs_str = str(args.vsx_kwargs_str)
    sexagesimal = args.sexagesimal
    verbose = args.verbose

    print()
    if (tpf_filename is not None):
        check_file_exists(tpf_filename, True)
        tpf = lk.open(tpf_filename)
    else:
        print('No TargetPixelFile (TPF) filename given.\n')
        search_result = lk.search_tesscut('XZ Cyg', sector=14)
        # print(search_result,'\n^--- search_result')
        tpf = search_result.download(cutout_size=10, quality_bitmask=0)
        # ^--- RR Lryae variable star XZ Cyg
        print()
        print(
            'Using default 10x10 TPF cutout of TESS Sector 14 '
            'observations of XZ Cyg.')
        print()
        shrink *= 0.8
        title = 'XZ Cyg : TESS : Sector 14'
    # pass:if
    try:
        print('TPF filename:', ntpath.basename(tpf.path))
        print('TPF dirname: ', os.path.dirname(tpf.path))
        assert(tpf.mission == 'TESS')
        print()
    except Exception:
        print(tpf_filename, '=tpf_filename')
        print('^--- *** ERROR *** This file does not appear to be a TESS '
              'TargetPixelFile')
        print()
        print('Bye...\n', flush=True)
        sys.exit(1)
    # pass:try

    ax = mkpy3_tess_tpf_overlay_v3(
      tpf=tpf,
      frame=frame,
      survey=survey,
      width_height_arcmin=width_height_arcmin,
      shrink=shrink,
      show_plot=show_plot,
      plot_file=plot_file,
      overwrite=overwrite,
      figsize_str=figsize_str,
      title=title,
      percentile=percentile,
      cmap=cmap,
      colors_str=colors_str,
      lws_str=lws_str,
      zorders_str=zorders_str,
      marker_kwargs_str=marker_kwargs_str,
      print_gaia_dr2=print_gaia_dr2,
      gaia_dr2_kwargs_str=gaia_dr2_kwargs_str,
      print_vsx=print_vsx,
      vsx_kwargs_str=vsx_kwargs_str,
      sexagesimal=sexagesimal,
      verbose=verbose
    )

# pass:if (__name__ == '__main__'):
# EOF

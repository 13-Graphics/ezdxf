#!/usr/bin/env python
#coding:utf-8
# Author:  mozman -- <mozman@gmx.at>
# Purpose: print object directory
# Created: 21.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License

import sys, os

import ezdxf


def main(filename):
    dwg = ezdxf.readfile(filename)
    msp = dwg.modelspace()
    hatches = msp.query("HATCH[solid_fill==0]")
    name, ext = os.path.splitext(filename)
    dump_pattern(name+'.py', hatches)


def dump_pattern(filename, hatches):
    with open(filename, 'wt') as f:
        f.write(FILE_HEADER)
        for hatch in hatches:
            f.write(get_pattern_definition_string(hatch))
        f.write(FILE_TAIL)

FILE_HEADER = """# DXF pattern definition file
# Do not edit this file, because this file was generated by 'dump_hatch_pattern.py'
# 'dump_hatch_pattern.py' is part of the Python package 'ezdxf'

Pattern = {
"""

FILE_TAIL = "}\n"

def get_pattern_definition_string(hatch):
    name = hatch.dxf.pattern_name
    with hatch.edit_pattern() as p:
        pattern = str(p)
    return "'{}': {},\n".format(name, pattern)

if __name__ == '__main__':
    main(sys.argv[1])
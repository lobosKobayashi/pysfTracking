# -*- coding:cp932 -*-

import svgwrite as svg

mm=3.543307 # pixel/mm
dwg=None

class RowContainor(object):
    """' Manage row sequence of shaped text instances.
    '"""
    def __str__(self):
        """' Return a svg text instance.
        '"""
        pass

class Group(svg.container.Group):
    """' A group of shape and text or a group of text, shape and theother text.
    '"""
    def __init__(self, shapeAg, svTxtAg): 
        svg.container.Group.__init__(self)
        self.add(shapeAg)
        self.add(svTxtAg)

    def __add__(self, ag):
        """' You can manage to lay out nested shaped-texts.
        '"""
        pass

    def __radd__(self, strAg):
        pass

    def __getattr__(self, chAg):
        pass


class SvTxt(svg.text.Text):
    """' text type which has 4 point positions:up,right,down,left.
    '"""
    inDefaultUnitStt=mm
    def __init__(self, strAg, font_size=5, font_family='sans'):
        """' font_size is interpreted by the mm size
        '"""
        fs=font_size*mm
        # just only 1 sentence for the time being
        svg.text.Text.__init__(self, strAg, insert=(1  *fs, 1*fs),
                               font_size=fs, font_family=font_family)

        # four corners:[[(1.2*fs, 0.1*fs), ((2+len(strAG))*fs, 0.1*fs)],
        #               [(1.2*fs, 1.2*fs), ((2+len(strAG))*fs,1.2*fs)]]
        import numpy as np
        mt=np.zeros([2,2,2],dtype=object)

        mt[0,0] = (0, 0.1*fs); mt[0,1] = (fs*(2+len(strAg)/2.0) , 0.1*fs)
        mt[1,0] = (0, 1.2*fs); mt[1,1] = (fs*(2+len(strAg)/2.0) , 1.2*fs)
        self.m_aryFourCorners = mt
    
    def __getattr__(self, name):
        mt = self.m_aryFourCorners

        if name == "N":                         # North
            return (mt[0,0]+mt[0,1])/2
        elif name == "E":                       # East
            return (mt[0,1]+mt[1,1])/2
        elif name == "S":                       # South
            return (mt[1,0]+mt[1,1])/2
        elif name == "W":                       # West
            return (mt[0,0]+mt[1,0])/2
        elif name == "NW":                      # North West
            return mt[0,0]
        elif name == "NE":                      # North East
            return mt[0,1]
        elif name == "SE":                      # South East
            return mt[1,1]
        elif name == "SW":                      # South West
            return mt[1,0]
        elif name == "C":                       # Center
            return sum(mt[0,0]+mt[0,1]+mt[1,0]+mt[1,1])/4

        elif name == "mt":
            return mt

        else:
            raise AttributeError

    def rect(self, *sqAg, **kwdAg):
        if len(sqAg) == 0:
            if not('size' in kwdAg):
                kwdAg['size'] = self.SE
        elif len(sqAg) == 1:
            assert not('size' in kwdAg)
            assert len(sqAg[0]) == 2
            kwdAg['size'] = self.SE
        else:
            assert False, "In SvTxt.rect, you set unexpected parameters:"+str(sqAg)

        if not('fill' in kwdAg):
            kwdAg['fill'] = 'none'

        if not('stroke' in kwdAg):
            kwdAg['stroke'] = 'black'

        return Group(svg.shapes.Rect([0,0], **kwdAg), self)

    def circle(self, options=None):
        pass


def show():
    """'save and start'"""
    import os
    dwg.save()
    os.system("start test.svg")

def ksv():
    global dwg
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170 130'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170mm 130mm'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'))
    dwg = svg.Drawing('test.svg', size=(170*mm, 130*mm))

    import sfFnctns as sf
    sf.__getDctGlobals()['svg']=svg
    sf.__getDctGlobals()['dwg']=dwg
    sf.__getDctGlobals()['mm']=mm

    import kSvgTxt as ksv
    sf.__getDctGlobals()['ksv']=ksv
    return dwg


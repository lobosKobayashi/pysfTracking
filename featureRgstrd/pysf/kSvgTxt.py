# -*- coding:cp932 -*-
import svgwrite as svg
import numpy as np

class SvSize(object):
    def __init__(self, strAg, flAg=1.0):
        """' data member:m_strUnit, m_flUnit, m_flValue
        '"""
        self.m_strUnit = strAg
        self.m_flUnit = flAg
        if strAg == 'px':
            self.m_flUnit = 1
            self.m_flValue=flAg
        elif strAg == 'mm':
            self.m_flUnit = 1/0.282222229121    # px pixel == 0.282222229121mm
            self.m_flValse = flAg * self.m_flUnit
        elif strAg == 'cm':
            self.m_flUnit = 10/2.82222229121
            self.m_flValse = flAg * self.m_flUnit
        else:
            assert False, "In SvSize.__init__(..) we don't yet implement unit:"+strAg


    def __rmul__(self, flAg):
        assert( isinstance(flAg,(int, float)) ), (
            "In SvSize.__rmul__, you set unexpected value:"+ str(flAg))
        return SvSize(self.m_strUnit, flAg)
    #def __mul__(self,ag): #pass      # detect right multiplyer

    def __float__(self):
        return self.m_flPxValue

    def __int__(self):
        return int(self.m_flPxValue)


    def __str__(self):
        return str(self)+'px'

class P_C_(object):
    """' percent unit class
    '"""
    def __init__(self):
        self.m_fl=1.0

    def __rmul__(self, flAg):
        assert isinstance(flAg,(int, float))
        self.m_fl=flAg
        return self

    def __mul__(self,ag): #pass      # detect right multiplyer
        return float(self)*ag

    def __float__(self):
        return self.m_fl/100.0

    def __str__(self):
        pass

px=SvSize('px')
mm=SvSize('mm')
cm=SvSize('cm')

#p_c_ = P_C_()
p_c_ = 0.01 # %:p_c_ は単なる数値の方が分かりやすそう。

class Enclosure(object):
    """' Primitive null shape type 
    '"""
    def __init__(sel, size=0, insert=np.array([0,0])):
        """' size=0 means there is no element
        '""" 
        assert np.all(insert==np.array([0,0])) if size==0 else True
        self.m_arSize = size
        self.m_arInsert = insert

    def __getattr__(self, name):
        mt = self.m_arFourCorners

        # North  East South West, North West, North East, South East, South West
        if self.m_arSize==0:
            if name in ('N',"E","S","W","NW","NE","SE","SW","C"):
                return array([0,0]) + self.m_arInsert
            elif name == "mt":
                return np.array([[[0,0],[0,0]],[[0,0],[0,0]]]) + self.m_arInsert


        if name == "N":                         # North
            return np.array([ self.m_arInsert[0]+self.m_arSize[0]/2,
                              self.m_arInsert[0]                    ])
        elif name == "E":                       # East
            return np.array([self.m_arInsert[0]+self.m_arSize[0]  ,
                             self.m_arInsert[1]+self.m_arSize[1]/2])
        elif name == "S":                       # South
            return np.array([self.m_arInsert[0]+self.m_arSize[0]/2,
                             self.m_arInsert[1]+self.m_arSize[1]  ])
        elif name == "W":                       # West
            return np.array([self.m_arInsert[0]                   ,
                             self.m_arInsert[1]+self.m_arSize[1]/2])
        elif name == "NW":                      # North West
            return np.array([self.m_arInsert[0]                   ,
                             self.m_arInsert[1]                   ])
        elif name == "NE":                      # North East
            return np.array([self.m_arInsert[0]+self.m_arSize[0]  ,
                             self.m_arInsert[1]                   ])
        elif name == "SE":                      # South East
            return mt[1,1]
            return np.array([self.m_arInsert[0]+self.m_arSize[0]  ,
                             self.m_arInsert[1]+self.m_arSize[1]  ])
        elif name == "SW":                      # South West
            return np.array([self.m_arInsert[0]                   ,
                             self.m_arInsert[1]+self.m_arSize[1]  ])
        elif name == "C":                       # Center
            return np.array([self.m_arInsert[0]+self.m_arSize[0]/2,
                             self.m_arInsert[1]+self.m_arSize[1]/2])

        elif name == "mt":
            return np.array([[self.NW, self.NE],
                             [self.SW, self.SE]])

        else:
            raise AttributeError


    class Line(object):
        def __init__(self, ch='U', pos=1/3*p_c_):
                self.m_tplCh_p_c_=(ch,pos)

class NestedEnclosure(Enclosure):
    """' Yet implemented
    '"""
    def __init__(self):pass

dwg=None

class Group(svg.container.Group):
    """' A group of shape and text or a group of text, shape and theother text.
    '"""
    def __init__(self, shapeAg, svTxtAg): 
        """' Yet implemented
        '"""
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


class Text(svg.text.Text, Enclosure):
    """' text type which has 4 point positions:up,right,down,left.
    '"""
    def __init__(self, strAg,
                 insert=np.array([0,0]), font_size=5*mm, 
                 font_family='MSgothic', **kwd):
        """' font_size is interpreted by the mm size
        '"""
        #Enclosure.__init__(self

        # four corners:[[(1.2*fs, 0.1*fs), ((2+len(strAG))*fs, 0.1*fs)],
        #               [(1.2*fs, 1.2*fs), ((2+len(strAG))*fs,1.2*fs)]]
        
        fs=float(font_size)
        #mt[0,0] = (0, 0.1*fs); mt[0,1] = (fs*(2+len(strAg)/2.0) , 0.1*fs)
        #mt[1,0] = (0, 1.2*fs); mt[1,1] = (fs*(2+len(strAg)/2.0) , 1.2*fs)
        arSize = __getSize(strAg,fs, font_family)
        En.closure.__init__(self, size=arSize)
    
        # just only 1 sentence for the time being
        svg.text.Text.__init__(self, strAg, insert=np.arry([np.insert[0],
                                                   insert[1]+self.m_arSize[1]]),
                               font_size=fs, font_family=font_family,**kwd)

    def __getSize(strAg, fs, font_family):
        """' text sizes shoud be determined for eahch font_family.
        But we don't know how to get them
        '"""
        return np.array(fs, fs*len(strAg)/2)

    def rect(self, *sqAg, **kwdAg):
        if len(sqAg) == 0:
            if not('size' in kwdAg):
                kwdAg['size'] = self.SE
        elif len(sqAg) == 1:
            assert not('size' in kwdAg)
            assert len(sqAg[0]) == 2
            kwdAg['size'] = self.SE
        else:
            assert False, "In Text.rect, you set unexpected parameters:"+str(sqAg)

        if not('fill' in kwdAg):
            kwdAg['fill'] = 'none'

        if not('stroke' in kwdAg):
            kwdAg['stroke'] = 'black'

        return Group(svg.shapes.Rect([0,0], **kwdAg), self)

    def circle(self, options=None):
        pass

class Rect(svg.shapes.Rect, Enclosure):
    def __init__(self, enclosure, margin=[5*p_c_, 10*p_c_, 5*p_c_, 10*p_c_], 
                 size=None, insert=np.array([0,0]),**kwd):
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


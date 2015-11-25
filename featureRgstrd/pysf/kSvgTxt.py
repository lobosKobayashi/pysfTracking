# -*- coding:cp932 -*-
"""' Text and Arrow SVG generator.
'"""
import sfFnctns as sf
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
            self.m_flValue = flAg * self.m_flUnit
        elif strAg == 'cm':
            self.m_flUnit = 10/2.82222229121
            self.m_flValue = flAg * self.m_flUnit
        else:
            assert False, "In SvSize.__init__(..) we don't yet implement unit:"+strAg


    def __rmul__(self, flAg):
        assert( isinstance(flAg,(int, float)) ), (
            "In SvSize.__rmul__, you set unexpected value:"+ str(flAg))
        return SvSize(self.m_strUnit, flAg)

    def __mul__(self,ag): #pass      # detect right multiplyer e.g. 17mm*'abc'
        if isinstance(ag, (str,unicode)):
            return Text(ag, float(self))
            #pass
        elif isinstance(ag, Text):
            # not figure out usages yet
            assert False
        else:
            import pdb; pdb.set_trace()
            assert(False)

    def __float__(self):
        return self.m_flValue

    def __int__(self):
        return int(self.m_flValue)


    def __str__(self):
        return str(self.m_flValue)+'px'
        #return str(int(self.m_flValue))

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
    def __init__(self, enclosure=None, insert=None, margin=None):
        """' enclosure==None means there is no element
        enclosre may be lenght 2 nemerical tuple,list, ndarray that define size ndarray
        enclosre may be a pare of size and enclosure object:([1,2], scalable svg instance)
        enclosre may be a enclosured instance which has the data member:m_arSize

        margin may be [left margin, top margin, right margin, bottom margin]
        margin may be [left margin, top margin] # [right margin, bottom margin] is same
        margin may be [value                    # [value,value,value] 

        # できたらいいな:I wish I could
            Enclosure can contain external SVG instance
        '""" 
        def __getNW_SE():
            if margin==None:
                arNW = np.array([0,0])
                arSE = np.array([0,0])
            elif hasattr(__len__, margin) and len(margin)==2:
                x,y=float(margin[0]), float(margin[1])
                
                arNW = np.array([x,y])
                arSE = np.array([x,y])
            else:
                assert len(margin) == 4

                x,y=float(margin[0]), float(margin[1])
                arNW = np.array([x,y])

                x,y=float(margin[1]), float(margin[2])
                arSE = np.array([x,y])

            return (arNW,arSE)
        #if  insert != None:
        #    assert np.all(insert==np.array([0,0])) if size==0 else True
        # self.m_arInsert == None means that this has not been deployed yet.
        self.m_arInsert = insert
        self.m_lstMargin=margin
        assert margin==None, 'not implemented m_margin yet'

        if isinstance(enclosure,Enclosure) and hasattr(enclosure,'m_svwObj'):
            # example 17mm"abc" : Text.__init__ has set self.m_arSize, m_svwObje
            arNW,arSE=__getNW_SE()
            self.m_arSize = arNW+enclosure.m_arSize+arSE
            return
        elif isinstance(enclosure,(tuple,list,np.ndarray)) and len(enclosure)==2:
            if isinstance(enclosure[0],(tuple,list,np.ndarray)) and len(enclosure[0])==2:
                assert isinstance(enclosure[1], (Enclosure, svg.text.Text))
                if margin==None:
                    arNW = np.array([0,0])
                    arSE = np.array([0,0])
                elif hasattr(__len__, margin) and len(margin)==2:
                    x,y=float(margin[0]), float(margin[1])
                    
                    arNW = np.array([x,y])
                    arSE = np.array([x,y])

                self.m_arSize = np.array(enclosure[0])
                self.m_svwObj = enclosure[1]
                self.m_svwObj.m_arSize=np.array(enclosure[0])
            else:
                # there is no enclosured object. just reserve an arear
                # example: Enclosure([15mm,20mm]), Enclosure(100,200) -- pixel
                arSize=np.array([float(enclosure[0]), float(enclosure[1])])
                arNW,arSE=__getNW_SE()
                self.m_arSize = arNW+arSize+arSE
                self.m_svwObj = None
        elif isinstance(enclosure, Enclosure): 
            #examples: Text(17mm'abc')
            #
            #assert False, "Recursive Enclosure is not implemented yet."
            arNW,arSE=__getNW_SE()
            self.m_arSize = arNW+self.m_arSize+arSE
            self.m_svwObj = self

        else:
            # Empty enclosure which keeps just only an arear.
            assert False

    def __getattr__(self, name):
        # North  East South West, North West, North East, South East, South West
        arInsert = np.array([0,0]) if self.m_arInsert==None else self.m_arInsert
        if np.all(self.m_arSize==[0,0]):
            if name in ('N',"E","S","W","NW","NE","SE","SW","C"):
                return array([0,0]) + arInsert
            elif name == "mt":
                return np.array([[[0,0],[0,0]],[[0,0],[0,0]]]) + arInsert


        if name == "N":                         # North
            return np.array([ arInsert[0]+self.m_arSize[0]/2,
                              arInsert[0]                    ])
        elif name == "E":                       # East
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]+self.m_arSize[1]/2])
        elif name == "S":                       # South
            return np.array([arInsert[0]+self.m_arSize[0]/2,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "W":                       # West
            return np.array([arInsert[0]                   ,
                             arInsert[1]+self.m_arSize[1]/2])
        elif name == "NW":                      # North West
            return np.array([arInsert[0]                   ,
                             arInsert[1]                   ])
        elif name == "NE":                      # North East
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]                   ])
        elif name == "SE":                      # South East
            return mt[1,1]
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "SW":                      # South West
            return np.array([arInsert[0]                   ,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "C":                       # Center
            return np.array([arInsert[0]+self.m_arSize[0]/2,
                             arInsert[1]+self.m_arSize[1]/2])

        elif name == "mt":
            return np.array([[self.NW, self.NE],
                             [self.SW, self.SE]])

        else:
            raise AttributeError


    class Edge(object):
        """'UDLR:Up,Down,Left,Right line is Enclosure inner class instance
        which  return np.ndarray posiion on T B L R lines
        example L:start ~[1,1], L:end ~[3,1] then 25p_c_ self.L == ~[1.5,1]
        '""" 
        def __init__(self, ch='U', pos=1/3*p_c_):
                self.m_tplCh_p_c_=(ch,pos)


class Text(Enclosure):
    """' text type which has 4 point positions:up,right,down,left.
    '"""
    @staticmethod
    def __getSize(strAg, fs, font_family):
        n=len(strAg)
        return np.array((fs, fs*n/2 if n%2==0 else fs*(0.5+n%2)))

    def __init__(self, strAg, font_size=5*mm, 
                 insert=np.array([0,0]),
                 font_family='monospace, MSgothic', **kwd):
        """' font_size is interpreted by the mm size
        '"""
        #Enclosure.__init__(self

        # four corners:[[(1.2*fs, 0.1*fs), ((2+len(strAG))*fs, 0.1*fs)],
        #               [(1.2*fs, 1.2*fs), ((2+len(strAG))*fs,1.2*fs)]]
        
        fs=float(font_size)
        #mt[0,0] = (0, 0.1*fs); mt[0,1] = (fs*(2+len(strAg)/2.0) , 0.1*fs)
        #mt[1,0] = (0, 1.2*fs); mt[1,1] = (fs*(2+len(strAg)/2.0) , 1.2*fs)
        arSize = Text.__getSize(strAg, fs, font_family)
        # just only 1 sentence for the time being
        self.m_arInsert=np.array([insert[0], insert[1]+arSize[1]])
        self.m_svwObj=svg.text.Text(strAg, font_size=fs,
                            insert=self.m_arInsert,
                            font_family=font_family,**kwd)
        self.m_flFontSize=fs
        self.m_arSize=arSize
        Enclosure.__init__(self, self)
        self.m_debug=1
    
    def tostring(self):
        #import pdb; pdb.set_trace()
        self.m_svwObj['x'],self.m_svwObj['y'] = (self.m_arInsert[0] + self.m_arSize[0],
                                                 self.m_arInsert[1]+self.m_flFontSize)
        return self.m_svwObj.tostring()

class AlndEclsAr(Enclosure):
    """'Aligned Enclosure Array

examples
    AlndEclsAr(10mm'ABC', 20mm'→', 10mm'abc').SVG
    '"""
    def __init__(self, mtEcls, lsRow_dx=0, lsCol_dy=0):
        """' mtEcls contains instances of Enclosre
        mtEncls may be np.array(...)

        yet implementted
                may be list or tuple
                may be dictionary with integer index
        '"""
        if isinstance(mtEcls, np.ndarray):
            pass
        else:
            assert False, "At AlndEclsAr.__init__, we presume mtEcls is numpy array for time being."

        tplShape = mtEcls.shape
        assert len(tplShape)==1
        if isinstance(lsRow_dx,(int, float)):
            lsRow_dx=[lsRow_dx]*tplShape[0]
        else:
            assert len(lsRow_dx)==tplShape[0],  ('You set a inappropreate paramter'
                                                + ' for lsRow_dx:'+str()
                                                )

        self.m_mtElements = mtEcls

        # for just only 1 row sequence
        fnWidth=lambda k: mtEcls[k].E[0]-mtEcls[k].W[0]
        lsMaxWidth = [fnWidth(k) for k in range(tplShape[0])]
        hrPos = 0   # initialize horizontal position
        for k in range(tplShape[0]):
           mtEcls[k].m_arInsert=np.array([hrPos + lsRow_dx[k],0])
           hrPos += lsMaxWidth[k]

        vtPos = max(mtEcls[k].S[1]-mtEcls[k].N[1] for k in range(tplShape[0]))
        self.m_arSize=np.array([hrPos, vtPos])
        Enclosure.__init__(self, self)

    def __getitem__(self,*ag):
        return self.m_mtElements.__getitem__(*ag)
        

    def tostring(self):
        mt = self.m_mtElements
        shape=mt.shape

        strAt=''
        import itertools as it
        for idx in it.product(range(shape[0]), range(shape[1])
                            ) if len(shape)==2 else range(shape[0]):
            if mt[idx] == 0:
                continue

            assert hasattr(mt[idx], 'tostring')

            strAt += mt[idx].tostring()+'\n'
        
        return strAt


class Rect(svg.shapes.Rect, Enclosure):
    def __init__(self, enclosure, margin=[5*p_c_, 10*p_c_, 5*p_c_, 10*p_c_], 
                 size=None, insert=np.array([0,0]),**kwd):
        pass

dwg=None
def show():
    """'save and start'"""
    import os
    dwg.save()
    os.system("start test.svg")

def ksv():
    global dwg, mm
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170 130'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170mm 130mm'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'))
    import sfFnctns as sf
    sf.__getDctGlobals()['mm']=mm

    mm=1/0.282222229121
    # print type(170*mm), 170*mm    # to debug
    dwg = svg.Drawing('test.svg', size=(170*mm, 130*mm))

    sf.__getDctGlobals()['svg']=svg
    sf.__getDctGlobals()['dwg']=dwg

    import kSvgTxt as ksv
    sf.__getDctGlobals()['ksv']=ksv
    return dwg


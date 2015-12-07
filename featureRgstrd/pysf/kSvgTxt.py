# -*- coding:cp932 -*-
"""' Text and Arrow SVG generator.
'"""
"""'
english:
Designed by kVerifierLab Kenji Kobayashi;;http://www.nasuinfo.or.jp/FreeSpace/kenji/index.htm

kVerifierLab Kobayashi has the all copyrights in this file. If you consider
comertial use of code(s) in this file, you must informe to kobayashi and
get Kobayshi's consent

kVerifierLab Kobayashi disclose this codes under below QPL license.

Granted Rights

1. You are granted the non-exclusive rights set forth in this license provided you agree to and comply with any and all conditions in this license. Whole or partial distribution of the Software, or software items that link with the Software, in any form signifies acceptance of this license.

2. You may copy and distribute the Software in unmodified form provided that the entire package, including - but not restricted to - copyright, trademark notices and disclaimers, as released by the initial developer of the Software, is distributed.

3. You may make modifications to the Software and distribute your modifications, in a form that is separate from the Software, such as patches. The following restrictions apply to modifications:

a. Modifications must not alter or remove any copyright notices in the Software.
b. When modifications to the Software are released under this license, a non-exclusive royalty-free right is granted to the initial developer of the Software to distribute your modification in future versions of the Software provided such versions remain available under these terms in addition to any other license(s) of the initial developer.

4. You may distribute machine-executable forms of the Software or machine-executable forms of modified versions of the Software, provided that you meet these restrictions:

a. You must include this license document in the distribution.
b. You must ensure that all recipients of the machine-executable forms are also able to receive the complete machine-readable source code to the distributed Software, including all modifications, without any charge beyond the costs of data transfer, and place prominent notices in the distribution explaining this.
c. You must ensure that all modifications included in the machine-executable forms are available under the terms of this license.

5. You may use the original or modified versions of the Software to compile, link and run application programs legally developed by you or by others.

6. You may develop application programs, reusable components and other software items that link with the original or modified versions of the Software. These items, when distributed, are subject to the following requirements:

a. You must ensure that all recipients of machine-executable forms of these items are also able to receive and use the complete machine-readable source code to the items without any charge beyond the costs of data transfer.
b. You must explicitly license all recipients of your items to use and re-distribute original and modified versions of the items in both machine-executable and source code forms. The recipients must be able to do so without any charges whatsoever, and they must be able to re-distribute to anyone they choose.
c. If the items are not available to the general public, and the initial developer of the Software requests a copy of the items, then you must supply one.

Limitations of Liability
In no event shall the initial developers or copyright holders be liable for any damages whatsoever, including - but not restricted to - lost revenue or profits or other direct, indirect, special, incidental or consequential damages, even if they have been advised of the possibility of such damages, except to the extent invariable law, if any, provides otherwise.

No Warranty
The Software and this license document are provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE��.

Choice of Law This license is governed by the Laws of Japan. Disputes shall be settled by Utzunomiya City Court.


japanese:
�쐬 kVerifierLab ����;;http://www.nasuinfo.or.jp/FreeSpace/kenji/index.htm

kVerifierLab ���т��A���̃t�@�C�����ɂ���v���O�����E�R�[�h�S�Ă̒��쌠��
�ۗL���܂��B���̃t�@�C�����̃R�[�h�����Ɨ��p����Ƃ��͏��тɘA�����A���т�
�����𓾂˂΂Ȃ�܂���B

kVerifierLab ���т́A���� QPL ���C�Z���X�̏����ł��̃R�[�h�����J���܂��B


�����ꂽ����

1. ���̃��C�Z���X�̂��ׂĂ̏����ɓ��ӂ��A�]���ꍇ�ɂ� ���̃��C�Z���X�ɂ���ĎY�ݏo������r���I�Ȉȉ��̌����� ���邱�Ƃ��ł��܂��B �u�\�t�g�E�F�A�v��u�\�t�g�E�F�A�v�������N�����\�t�g�E�F�A�� �S�̂������͈ꕔ�ɗ��p�����z�z���͂ǂ�Ȍ`���ł� ���̃��C�Z���X����������ƌ��Ȃ��܂��B

2. ���Ȃ��́u�\�t�g�E�F�A�v���A ���쌠�\���ȂǂŐ�������Ă��Ȃ��ꍇ�Ɍ���A �I���W�i���p�b�P�[�W���z�z���ꂽ�Ƃ��̂܂ܕύX���Ȃ��`�� �����A�z�z���邱�Ƃ��ł���B

3. ���Ȃ��́u�\�t�g�E�F�A�v�̕ύX���s�Ȃ��A���̕ύX�� �p�b�`�̂悤�Ɂu�\�t�g�E�F�A�v�Ƃ͓Ɨ��̌`���Ŕz�z���邱�Ƃ��ł��܂��B �������A���̂悤�Ȑ���������܂��B

a. �ύX�͒��쌠�ʒm�̕ύX��폜���s�Ȃ��Ă͍s���܂���B
b. ���̃��C�Z���X�ɉ����āu�\�t�g�E�F�A�v�ւ̕ύX�����J���ꂽ�ꍇ�A �u�\�t�g�E�F�A�v�̊J���҂́A ���Ȃ��̕ύX�𗘗p���Ȃ��ō���̃o�[�W�����Ŕz�z���邱�Ƃ��\�ł��B �������A�u�\�t�g�E�F�A�v�̃��C�Z���X��ύX���Ȃ��ꍇ�Ɍ���܂��B

4. �ȉ��̐����ɉ������ꍇ�ɂ� �u�\�t�g�E�F�A�v�̎��s�`���� �ύX���ꂽ�u�\�t�g�E�F�A�v�̎��s�`���̔z�z���\�ł��B
a. ���̃��C�Z���X���͂��܂߂Ĕz�z���Ȃ���΂Ȃ�܂���B
b. ���Ȃ��͎��s�`�����󂯎�������ׂĂ̐l�ɁA ���ׂĂ̕ύX���܂񂾋@�B�ǂݎ��\�Ȋ��S�ȃ\�[�X�R�[�h�� ����ȊO�̃R�X�g���������ɓ���ł���悤�ɕۏ؂��Ȃ���΂Ȃ�܂���B �����Ĕz�z���̖ڗ��ꏊ�ł��̂��Ƃ�������Ȃ���΂Ȃ�܂���B
c. ���s�`���Ɋ܂܂��ύX�����̃��C�Z���X�ɏ]�����Ƃ� �ۏ؂��Ȃ���΂Ȃ�܂���B

5. �I���W�i���A�������͕ύX���ꂽ�u�\�t�g�E�F�A�v�� ���Ȃ��⑼�̐l���J�������A�v���P�[�V�����v���O���������s���邽�߂ɃR���p�C���E�����N���邱�Ƃ��ł��܂��B

6. �I���W�i���A�������͕ύX���ꂽ�u�\�t�g�E�F�A�v�������N���� �A�v���P�[�V�����v���O������ė��p�\�ȕ��i�� ���̂ق��̃\�t�g�E�F�A���J���ł��܂��B �����̃\�t�g��z�z����ꍇ�ɂ͎��̗v���𖞂����Ă��Ȃ���΂����܂���B
a. �����̃\�t�g�E�F�A�̎��s�`�����󂯎�������ׂĂ̐l�ɁA �@�B�ǂݎ��\�Ȋ��S�ȃ\�[�X�R�[�h�� ����ȊO�̃R�X�g���������ɓ���ł���悤�ɕۏ؂��Ȃ���΂Ȃ�܂���B
b. ���Ȃ��̃\�t�g�E�F�A���󂯎�������ׂĂ̐l�ɁA �I���W�i���̃\�t�g�E�F�A��ύX���ꂽ�\�t�g�E�F�A�� ���s�`����\�[�X�R�[�h�̍Ĕz�z�◘�p���邽�߂̃��C�Z���X�� �������Ȃ���΂Ȃ�܂���B �󂯎�����l�͑��̂ǂ�ȗ������Ȃ��ɂ���炪�\�łȂ��Ă͂Ȃ�܂���B �܂��A���̂ǂ�Ȑl�ɂł��Ĕz�z�\�łȂ��Ă͂Ȃ�܂���B
c. ���������̃\�t�g�E�F�A�����O�����p�\�łȂ��ꍇ�ł��A �u�\�t�g�E�F�A�v�̊J���҂��\�t�g�E�F�A�̕�����v�������ꍇ�ɂ� ���̗v���ɓ����Ȃ��Ă͂����܂���B

�ӔC�̐���
�ǂ̂悤�ȏꍇ�ł��J���҂⒘�쌠�ێ��҂� ���Q�ɑ΂���ӔC�𕉂����Ƃ͂���܂���B

���ۏ�
�u�\�t�g�E�F�A�v�Ƃ��̃��C�Z���X�̕��͂́u���̂܂܁v�Łu���ۏ؁v�ł��B

���̃��C�Z���X�͓��{�̖@���ɂ���ĕی삳��Ă��܂��B ���c�͉F�s�{�n�قɂ���ĉ��������ł��傤�B 

'"""
#import sfFnctns as sf
import svgwrite as svg
import numpy as np

class SvSize(object):
    @staticmethod
    def __ConvertToUnicode(strAg):
        if isinstance(strAg, unicode):
            return strAg
        # try convert shift-jis to unicode
        try:
            rtnStr = strAg.decode('shift-jis')
            return rtnStr
        except:
            pass

        # try convert utf-8 to unicode
        try:
            rtnStr = strAg.decode('utf-8')
            return rtnStr
        except:
            pass

        assert False, ("In SvSize::__ConverToUnicodeStr(strAg), we come across "
                     + "unexpected parameter:" + strAg
                      )

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
        if isinstance(ag, unicode):
            return Text(ag, self)
            #pass
        elif isinstance(ag, Text):
            # not figure out usages yet
            assert False
        elif isinstance(ag, str):
            strAt = SvSize.__ConvertToUnicode(ag)
            return Text(strAt, self)
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

    def getFontPxSize(self):
        inAt = int(self)
        flSize= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        return flSize

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
p_c_ = 0.01 # %:p_c_ �͒P�Ȃ鐔�l�̕���������₷�����B

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

        # �ł����炢����:I wish I could
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
                # example Enclosure([arSize, 17mm'abc'])
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
    def getSize(ustrAg, fs, font_family):
        r"""' strAg �� ascii text or unicode text 
        We deal with only MS gothic font only because of equal width fonts"

        Cation! Yet not implemented multi lines by \n 
            Also, we should implement, left, middle, right aslignement oprtions
        '"""
        assert fs%2==0
        def __checkHalfSize(ch):
            c=ord(ch)
            if( ( c<=0x7e ) or     # �p����
                ( c==0xa5 ) or     # \�L��
                ( c==0x203e) or    # ~�L��
                ( c>=0xff61 and c<=0xff9f)   # ���p�J�i
            ):
                return True
            else:
                return False

        n=sum(1 if __checkHalfSize(c) else 2 for c in ustrAg)
        return np.array((fs/2*n, fs))


    def __init__(self, ustrAg, font_size=5*mm, 
                 insert=np.array([0,0]),
                 font_family='MS gothic', **kwd):
        """' font_size is interpreted by the mm size
        kwd are parameters for svgwrite.text.Text.
        '"""
        if isinstance(font_size, int):
            inAt = font_size
            fs= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        elif isinstance(font_size, float):
            inAt = int(font_size)
            fs= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        elif isinstance(font_size, SvSize):
            fs = font_size.getFontPxSize()
        else:
            assert False, ( 'In Text.__init__, you set a unexpected parameter '
                          + 'for font_size:'+str(font_size)
                          )

        lsUstr=ustrAg.split('\n')
        if len(lsUstr) >= 2:

            cl = InnerMultiLine(lsUstr, fs, insert, font_family, **kwd)
            self.m_arInsert = cl.m_arInsert
            self.m_arSize = cl.m_arSize
            self.m_flFontSize = fs
            self.m_svwObj = cl
        else:
            arSize = Text.getSize(ustrAg, fs, font_family)
            # just only 1 sentence for the time being
            self.m_arInsert=np.array([insert[0], insert[1]+arSize[1]])
            self.m_svwObj=svg.text.Text(ustrAg.encode('utf-8'), font_size=int(fs),
                                insert=self.m_arInsert,
                                font_family=font_family,**kwd)
            self.m_flFontSize=fs
            self.m_arSize=arSize
        
        Enclosure.__init__(self, self, self.m_arInsert)
        self.m_debug=1
    
    def tostring(self, bl_utf_jis=False):
        #import pdb; pdb.set_trace()
        if isinstance(self.m_svwObj, InnerMultiLine):
            return self.m_svwObj.toString(bl_utf_jis, self.m_arInsert)
        else:
            self.m_svwObj['x'],self.m_svwObj['y'] = (
                        int(self.m_arInsert[0]),
                        int(self.m_arInsert[1]+self.m_flFontSize)
                        )
            if bl_utf_jis == True:
                return self.m_svwObj.tostring().encode('utf-8')
            else:
                return self.m_svwObj.tostring().encode('shift-jis')

class InnerMultiLine(Text):
    def __init__(self, lsUstrAg, fs, insert, font_family, **kwd):
        widthMax =  0
        self.m_lsSvwObj=[]
        for j, ustrAt in enumerate(lsUstrAg):
            # just only left alignment sentences for the time being
            width = Text.getSize(ustrAt, fs, font_family)[0]
            if width > widthMax:
                widthMax = width

            self.m_lsSvwObj.append( svg.text.Text(ustrAt, font_size=fs,
                                        insert = (insert[0], insert[1]+j*fs ),
                                        font_family = font_family, **kwd)
                                  )

        arSize = np.array([widthMax, len(lsUstrAg) * fs])
        self.m_arInsert = np.array([insert[0], insert[1] + arSize[1]])
        self.m_svwObj = self
        self.m_flFontSize = fs
        self.m_arSize = arSize

    def toString(self, bl_utf_jis, insert):
        strAt=''
        for j,svwAt in enumerate(self.m_lsSvwObj):
            svwAt['x'], svwAt['y'] = (
                        int(insert[0]),
                        int(insert[1]+j*self.m_flFontSize)
                    )
            if bl_utf_jis == True:
                strAt += svwAt.tostring().encode('utf-8') + u'\n'
            else:
                strAt += svwAt.tostring().encode('shift-jis') + u'\n'

        #strAt = strAt[:-1]      # delete last \n

        return strAt

class AlndEclsAr(Enclosure):
    """'Aligned Enclosure Array

examples
    AlndEclsAr(10mm'ABC', 20mm'��', 10mm'abc').SVG
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


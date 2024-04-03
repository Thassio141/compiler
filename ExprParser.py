# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,170,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,
        1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,71,
        8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,84,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,93,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,127,
        8,14,1,15,1,15,3,15,131,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,3,17,142,8,17,1,18,1,18,1,18,1,18,1,18,3,18,149,8,18,1,
        19,1,19,1,19,1,19,1,19,3,19,156,8,19,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,168,8,20,1,20,0,0,21,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,1,2,0,3,4,29,29,168,
        0,42,1,0,0,0,2,52,1,0,0,0,4,59,1,0,0,0,6,61,1,0,0,0,8,70,1,0,0,0,
        10,72,1,0,0,0,12,74,1,0,0,0,14,83,1,0,0,0,16,92,1,0,0,0,18,94,1,
        0,0,0,20,99,1,0,0,0,22,106,1,0,0,0,24,111,1,0,0,0,26,116,1,0,0,0,
        28,126,1,0,0,0,30,130,1,0,0,0,32,132,1,0,0,0,34,141,1,0,0,0,36,148,
        1,0,0,0,38,155,1,0,0,0,40,167,1,0,0,0,42,43,5,2,0,0,43,44,5,31,0,
        0,44,45,5,22,0,0,45,46,3,2,1,0,46,47,3,12,6,0,47,48,5,23,0,0,48,
        1,1,0,0,0,49,50,5,10,0,0,50,53,3,4,2,0,51,53,1,0,0,0,52,49,1,0,0,
        0,52,51,1,0,0,0,53,3,1,0,0,0,54,60,3,6,3,0,55,56,3,6,3,0,56,57,5,
        25,0,0,57,58,3,4,2,0,58,60,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,60,
        5,1,0,0,0,61,62,3,8,4,0,62,63,5,24,0,0,63,64,3,10,5,0,64,65,5,22,
        0,0,65,7,1,0,0,0,66,71,5,31,0,0,67,68,5,31,0,0,68,69,5,25,0,0,69,
        71,3,8,4,0,70,66,1,0,0,0,70,67,1,0,0,0,71,9,1,0,0,0,72,73,7,0,0,
        0,73,11,1,0,0,0,74,75,5,5,0,0,75,76,3,14,7,0,76,77,5,6,0,0,77,13,
        1,0,0,0,78,84,3,16,8,0,79,80,3,16,8,0,80,81,5,22,0,0,81,82,3,14,
        7,0,82,84,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,84,15,1,0,0,0,85,93,
        3,18,9,0,86,93,3,22,11,0,87,93,3,24,12,0,88,93,3,26,13,0,89,93,3,
        32,16,0,90,93,3,12,6,0,91,93,3,20,10,0,92,85,1,0,0,0,92,86,1,0,0,
        0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,
        1,0,0,0,93,17,1,0,0,0,94,95,5,14,0,0,95,96,3,34,17,0,96,97,5,15,
        0,0,97,98,3,16,8,0,98,19,1,0,0,0,99,100,5,14,0,0,100,101,3,34,17,
        0,101,102,5,15,0,0,102,103,3,16,8,0,103,104,5,16,0,0,104,105,3,16,
        8,0,105,21,1,0,0,0,106,107,5,7,0,0,107,108,3,34,17,0,108,109,5,8,
        0,0,109,110,3,16,8,0,110,23,1,0,0,0,111,112,5,9,0,0,112,113,5,26,
        0,0,113,114,3,8,4,0,114,115,5,27,0,0,115,25,1,0,0,0,116,117,5,13,
        0,0,117,118,5,26,0,0,118,119,3,28,14,0,119,120,5,27,0,0,120,27,1,
        0,0,0,121,127,3,30,15,0,122,123,3,30,15,0,123,124,5,25,0,0,124,125,
        3,28,14,0,125,127,1,0,0,0,126,121,1,0,0,0,126,122,1,0,0,0,127,29,
        1,0,0,0,128,131,3,34,17,0,129,131,5,29,0,0,130,128,1,0,0,0,130,129,
        1,0,0,0,131,31,1,0,0,0,132,133,5,31,0,0,133,134,5,28,0,0,134,135,
        3,34,17,0,135,33,1,0,0,0,136,142,3,36,18,0,137,138,3,36,18,0,138,
        139,5,19,0,0,139,140,3,36,18,0,140,142,1,0,0,0,141,136,1,0,0,0,141,
        137,1,0,0,0,142,35,1,0,0,0,143,149,3,38,19,0,144,145,3,38,19,0,145,
        146,5,17,0,0,146,147,3,36,18,0,147,149,1,0,0,0,148,143,1,0,0,0,148,
        144,1,0,0,0,149,37,1,0,0,0,150,151,3,40,20,0,151,152,5,18,0,0,152,
        153,3,38,19,0,153,156,1,0,0,0,154,156,3,40,20,0,155,150,1,0,0,0,
        155,154,1,0,0,0,156,39,1,0,0,0,157,168,5,31,0,0,158,168,5,32,0,0,
        159,160,5,26,0,0,160,161,3,34,17,0,161,162,5,27,0,0,162,168,1,0,
        0,0,163,168,5,12,0,0,164,168,5,11,0,0,165,166,5,21,0,0,166,168,3,
        40,20,0,167,157,1,0,0,0,167,158,1,0,0,0,167,159,1,0,0,0,167,163,
        1,0,0,0,167,164,1,0,0,0,167,165,1,0,0,0,168,41,1,0,0,0,11,52,59,
        70,83,92,126,130,141,148,155,167
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'PROGRAM'", "'INTEGER'", 
                     "'BOOLEAN'", "'BEGIN'", "'END'", "'WHILE'", "'DO'", 
                     "'READ'", "'VAR'", "'FALSE'", "'TRUE'", "'WRITE'", 
                     "'IF'", "'THEN'", "'ELSE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'~'", "';'", "'.'", "':'", 
                     "','", "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "PROGRAM", "INTEGER", "BOOLEAN", 
                      "BEGIN", "END", "WHILE", "DO", "READ", "VAR", "FALSE", 
                      "TRUE", "WRITE", "IF", "THEN", "ELSE", "OPAD", "OPMULT", 
                      "OPREL", "OPLOG", "OPNEG", "PVIG", "PONTO", "DPONTOS", 
                      "VIG", "ABPAR", "FPAR", "ATRIB", "CADEIA", "WS", "ID", 
                      "CTE" ]

    RULE_prog = 0
    RULE_decls = 1
    RULE_listDecl = 2
    RULE_declTip = 3
    RULE_listId = 4
    RULE_tip = 5
    RULE_cmdComp = 6
    RULE_listCmd = 7
    RULE_cmd = 8
    RULE_cmdIf = 9
    RULE_cmdIfElse = 10
    RULE_cmdWhile = 11
    RULE_cmdRead = 12
    RULE_cmdWrite = 13
    RULE_listW = 14
    RULE_elemW = 15
    RULE_cmdAtrib = 16
    RULE_expr = 17
    RULE_exprAd = 18
    RULE_exprMult = 19
    RULE_exprDif = 20

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdIfElse", "cmdWhile", 
                   "cmdRead", "cmdWrite", "listW", "elemW", "cmdAtrib", 
                   "expr", "exprAd", "exprMult", "exprDif" ]

    EOF = Token.EOF
    COMMENT=1
    PROGRAM=2
    INTEGER=3
    BOOLEAN=4
    BEGIN=5
    END=6
    WHILE=7
    DO=8
    READ=9
    VAR=10
    FALSE=11
    TRUE=12
    WRITE=13
    IF=14
    THEN=15
    ELSE=16
    OPAD=17
    OPMULT=18
    OPREL=19
    OPLOG=20
    OPNEG=21
    PVIG=22
    PONTO=23
    DPONTOS=24
    VIG=25
    ABPAR=26
    FPAR=27
    ATRIB=28
    CADEIA=29
    WS=30
    ID=31
    CTE=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(ExprParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def PVIG(self):
            return self.getToken(ExprParser.PVIG, 0)

        def decls(self):
            return self.getTypedRuleContext(ExprParser.DeclsContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(ExprParser.CmdCompContext,0)


        def PONTO(self):
            return self.getToken(ExprParser.PONTO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ExprParser.PROGRAM)
            self.state = 43
            self.match(ExprParser.ID)
            self.state = 44
            self.match(ExprParser.PVIG)
            self.state = 45
            self.decls()
            self.state = 46
            self.cmdComp()
            self.state = 47
            self.match(ExprParser.PONTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def listDecl(self):
            return self.getTypedRuleContext(ExprParser.ListDeclContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = ExprParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(ExprParser.VAR)
                self.state = 50
                self.listDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declTip(self):
            return self.getTypedRuleContext(ExprParser.DeclTipContext,0)


        def VIG(self):
            return self.getToken(ExprParser.VIG, 0)

        def listDecl(self):
            return self.getTypedRuleContext(ExprParser.ListDeclContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDecl" ):
                listener.enterListDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDecl" ):
                listener.exitListDecl(self)




    def listDecl(self):

        localctx = ExprParser.ListDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listDecl)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.declTip()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.declTip()
                self.state = 56
                self.match(ExprParser.VIG)
                self.state = 57
                self.listDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclTipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listId(self):
            return self.getTypedRuleContext(ExprParser.ListIdContext,0)


        def DPONTOS(self):
            return self.getToken(ExprParser.DPONTOS, 0)

        def tip(self):
            return self.getTypedRuleContext(ExprParser.TipContext,0)


        def PVIG(self):
            return self.getToken(ExprParser.PVIG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declTip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTip" ):
                listener.enterDeclTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTip" ):
                listener.exitDeclTip(self)




    def declTip(self):

        localctx = ExprParser.DeclTipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declTip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.listId()
            self.state = 62
            self.match(ExprParser.DPONTOS)
            self.state = 63
            self.tip()
            self.state = 64
            self.match(ExprParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def VIG(self):
            return self.getToken(ExprParser.VIG, 0)

        def listId(self):
            return self.getTypedRuleContext(ExprParser.ListIdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListId" ):
                listener.enterListId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListId" ):
                listener.exitListId(self)




    def listId(self):

        localctx = ExprParser.ListIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listId)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(ExprParser.ID)
                self.state = 68
                self.match(ExprParser.VIG)
                self.state = 69
                self.listId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExprParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(ExprParser.BOOLEAN, 0)

        def CADEIA(self):
            return self.getToken(ExprParser.CADEIA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_tip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTip" ):
                listener.enterTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTip" ):
                listener.exitTip(self)




    def tip(self):

        localctx = ExprParser.TipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536870936) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ExprParser.BEGIN, 0)

        def listCmd(self):
            return self.getTypedRuleContext(ExprParser.ListCmdContext,0)


        def END(self):
            return self.getToken(ExprParser.END, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cmdComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdComp" ):
                listener.enterCmdComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdComp" ):
                listener.exitCmdComp(self)




    def cmdComp(self):

        localctx = ExprParser.CmdCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ExprParser.BEGIN)
            self.state = 75
            self.listCmd()
            self.state = 76
            self.match(ExprParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self):
            return self.getTypedRuleContext(ExprParser.CmdContext,0)


        def PVIG(self):
            return self.getToken(ExprParser.PVIG, 0)

        def listCmd(self):
            return self.getTypedRuleContext(ExprParser.ListCmdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCmd" ):
                listener.enterListCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCmd" ):
                listener.exitListCmd(self)




    def listCmd(self):

        localctx = ExprParser.ListCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listCmd)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.cmd()
                self.state = 80
                self.match(ExprParser.PVIG)
                self.state = 81
                self.listCmd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdIf(self):
            return self.getTypedRuleContext(ExprParser.CmdIfContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(ExprParser.CmdWhileContext,0)


        def cmdRead(self):
            return self.getTypedRuleContext(ExprParser.CmdReadContext,0)


        def cmdWrite(self):
            return self.getTypedRuleContext(ExprParser.CmdWriteContext,0)


        def cmdAtrib(self):
            return self.getTypedRuleContext(ExprParser.CmdAtribContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(ExprParser.CmdCompContext,0)


        def cmdIfElse(self):
            return self.getTypedRuleContext(ExprParser.CmdIfElseContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = ExprParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmd)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.cmdIf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.cmdWhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.cmdRead()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.cmdWrite()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.cmdAtrib()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.cmdComp()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.cmdIfElse()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)

        def cmd(self):
            return self.getTypedRuleContext(ExprParser.CmdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)




    def cmdIf(self):

        localctx = ExprParser.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ExprParser.IF)
            self.state = 95
            self.expr()
            self.state = 96
            self.match(ExprParser.THEN)
            self.state = 97
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CmdContext)
            else:
                return self.getTypedRuleContext(ExprParser.CmdContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cmdIfElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIfElse" ):
                listener.enterCmdIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIfElse" ):
                listener.exitCmdIfElse(self)




    def cmdIfElse(self):

        localctx = ExprParser.CmdIfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdIfElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ExprParser.IF)
            self.state = 100
            self.expr()
            self.state = 101
            self.match(ExprParser.THEN)
            self.state = 102
            self.cmd()
            self.state = 103
            self.match(ExprParser.ELSE)
            self.state = 104
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def DO(self):
            return self.getToken(ExprParser.DO, 0)

        def cmd(self):
            return self.getTypedRuleContext(ExprParser.CmdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)




    def cmdWhile(self):

        localctx = ExprParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ExprParser.WHILE)
            self.state = 107
            self.expr()
            self.state = 108
            self.match(ExprParser.DO)
            self.state = 109
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(ExprParser.READ, 0)

        def ABPAR(self):
            return self.getToken(ExprParser.ABPAR, 0)

        def listId(self):
            return self.getTypedRuleContext(ExprParser.ListIdContext,0)


        def FPAR(self):
            return self.getToken(ExprParser.FPAR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cmdRead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRead" ):
                listener.enterCmdRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRead" ):
                listener.exitCmdRead(self)




    def cmdRead(self):

        localctx = ExprParser.CmdReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ExprParser.READ)
            self.state = 112
            self.match(ExprParser.ABPAR)
            self.state = 113
            self.listId()
            self.state = 114
            self.match(ExprParser.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)

        def ABPAR(self):
            return self.getToken(ExprParser.ABPAR, 0)

        def listW(self):
            return self.getTypedRuleContext(ExprParser.ListWContext,0)


        def FPAR(self):
            return self.getToken(ExprParser.FPAR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cmdWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWrite" ):
                listener.enterCmdWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWrite" ):
                listener.exitCmdWrite(self)




    def cmdWrite(self):

        localctx = ExprParser.CmdWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ExprParser.WRITE)
            self.state = 117
            self.match(ExprParser.ABPAR)
            self.state = 118
            self.listW()
            self.state = 119
            self.match(ExprParser.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemW(self):
            return self.getTypedRuleContext(ExprParser.ElemWContext,0)


        def VIG(self):
            return self.getToken(ExprParser.VIG, 0)

        def listW(self):
            return self.getTypedRuleContext(ExprParser.ListWContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListW" ):
                listener.enterListW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListW" ):
                listener.exitListW(self)




    def listW(self):

        localctx = ExprParser.ListWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listW)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.elemW()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.elemW()
                self.state = 123
                self.match(ExprParser.VIG)
                self.state = 124
                self.listW()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def CADEIA(self):
            return self.getToken(ExprParser.CADEIA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_elemW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemW" ):
                listener.enterElemW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemW" ):
                listener.exitElemW(self)




    def elemW(self):

        localctx = ExprParser.ElemWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elemW)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 21, 26, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.expr()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(ExprParser.CADEIA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ATRIB(self):
            return self.getToken(ExprParser.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_cmdAtrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAtrib" ):
                listener.enterCmdAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAtrib" ):
                listener.exitCmdAtrib(self)




    def cmdAtrib(self):

        localctx = ExprParser.CmdAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ExprParser.ID)
            self.state = 133
            self.match(ExprParser.ATRIB)
            self.state = 134
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprAd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprAdContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprAdContext,i)


        def OPREL(self):
            return self.getToken(ExprParser.OPREL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.exprAd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.exprAd()

                self.state = 138
                self.match(ExprParser.OPREL)
                self.state = 139
                self.exprAd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprAdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprMult(self):
            return self.getTypedRuleContext(ExprParser.ExprMultContext,0)


        def exprAd(self):
            return self.getTypedRuleContext(ExprParser.ExprAdContext,0)


        def OPAD(self):
            return self.getToken(ExprParser.OPAD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exprAd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAd" ):
                listener.enterExprAd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAd" ):
                listener.exitExprAd(self)




    def exprAd(self):

        localctx = ExprParser.ExprAdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprAd)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.exprMult()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.exprMult()

                self.state = 145
                self.match(ExprParser.OPAD)
                self.state = 146
                self.exprAd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprMultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprDif(self):
            return self.getTypedRuleContext(ExprParser.ExprDifContext,0)


        def exprMult(self):
            return self.getTypedRuleContext(ExprParser.ExprMultContext,0)


        def OPMULT(self):
            return self.getToken(ExprParser.OPMULT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exprMult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMult" ):
                listener.enterExprMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMult" ):
                listener.exitExprMult(self)




    def exprMult(self):

        localctx = ExprParser.ExprMultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprMult)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.exprDif()

                self.state = 151
                self.match(ExprParser.OPMULT)
                self.state = 152
                self.exprMult()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.exprDif()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprDifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def CTE(self):
            return self.getToken(ExprParser.CTE, 0)

        def ABPAR(self):
            return self.getToken(ExprParser.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def FPAR(self):
            return self.getToken(ExprParser.FPAR, 0)

        def TRUE(self):
            return self.getToken(ExprParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ExprParser.FALSE, 0)

        def OPNEG(self):
            return self.getToken(ExprParser.OPNEG, 0)

        def exprDif(self):
            return self.getTypedRuleContext(ExprParser.ExprDifContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exprDif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprDif" ):
                listener.enterExprDif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprDif" ):
                listener.exitExprDif(self)




    def exprDif(self):

        localctx = ExprParser.ExprDifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exprDif)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(ExprParser.ID)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(ExprParser.CTE)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(ExprParser.ABPAR)
                self.state = 160
                self.expr()
                self.state = 161
                self.match(ExprParser.FPAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.match(ExprParser.TRUE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.match(ExprParser.FALSE)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.match(ExprParser.OPNEG)
                self.state = 166
                self.exprDif()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






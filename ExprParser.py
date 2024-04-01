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
        4,1,32,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,2,1,
        2,3,2,58,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,69,8,4,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,82,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,90,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,104,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,126,8,13,
        1,14,1,14,3,14,130,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,3,16,141,8,16,1,17,1,17,1,17,1,17,1,17,3,17,148,8,17,1,18,1,
        18,1,18,1,18,1,18,3,18,155,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,167,8,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,1,2,0,3,4,30,30,168,0,40,1,0,
        0,0,2,50,1,0,0,0,4,57,1,0,0,0,6,59,1,0,0,0,8,68,1,0,0,0,10,70,1,
        0,0,0,12,72,1,0,0,0,14,81,1,0,0,0,16,89,1,0,0,0,18,103,1,0,0,0,20,
        105,1,0,0,0,22,110,1,0,0,0,24,115,1,0,0,0,26,125,1,0,0,0,28,129,
        1,0,0,0,30,131,1,0,0,0,32,140,1,0,0,0,34,147,1,0,0,0,36,154,1,0,
        0,0,38,166,1,0,0,0,40,41,5,2,0,0,41,42,5,32,0,0,42,43,5,23,0,0,43,
        44,3,2,1,0,44,45,3,12,6,0,45,46,5,24,0,0,46,1,1,0,0,0,47,48,5,10,
        0,0,48,51,3,4,2,0,49,51,1,0,0,0,50,47,1,0,0,0,50,49,1,0,0,0,51,3,
        1,0,0,0,52,58,3,6,3,0,53,54,3,6,3,0,54,55,5,26,0,0,55,56,3,4,2,0,
        56,58,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,58,5,1,0,0,0,59,60,3,8,
        4,0,60,61,5,25,0,0,61,62,3,10,5,0,62,63,5,23,0,0,63,7,1,0,0,0,64,
        69,5,32,0,0,65,66,5,32,0,0,66,67,5,26,0,0,67,69,3,8,4,0,68,64,1,
        0,0,0,68,65,1,0,0,0,69,9,1,0,0,0,70,71,7,0,0,0,71,11,1,0,0,0,72,
        73,5,5,0,0,73,74,3,14,7,0,74,75,5,6,0,0,75,13,1,0,0,0,76,82,3,16,
        8,0,77,78,3,16,8,0,78,79,5,23,0,0,79,80,3,14,7,0,80,82,1,0,0,0,81,
        76,1,0,0,0,81,77,1,0,0,0,82,15,1,0,0,0,83,90,3,18,9,0,84,90,3,20,
        10,0,85,90,3,22,11,0,86,90,3,24,12,0,87,90,3,30,15,0,88,90,3,12,
        6,0,89,83,1,0,0,0,89,84,1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,
        1,0,0,0,89,88,1,0,0,0,90,17,1,0,0,0,91,92,5,14,0,0,92,93,3,32,16,
        0,93,94,5,15,0,0,94,95,3,16,8,0,95,104,1,0,0,0,96,97,5,14,0,0,97,
        98,3,32,16,0,98,99,5,15,0,0,99,100,3,16,8,0,100,101,5,16,0,0,101,
        102,3,16,8,0,102,104,1,0,0,0,103,91,1,0,0,0,103,96,1,0,0,0,104,19,
        1,0,0,0,105,106,5,7,0,0,106,107,3,32,16,0,107,108,5,8,0,0,108,109,
        3,16,8,0,109,21,1,0,0,0,110,111,5,9,0,0,111,112,5,27,0,0,112,113,
        3,8,4,0,113,114,5,28,0,0,114,23,1,0,0,0,115,116,5,13,0,0,116,117,
        5,27,0,0,117,118,3,26,13,0,118,119,5,28,0,0,119,25,1,0,0,0,120,126,
        3,28,14,0,121,122,3,28,14,0,122,123,5,26,0,0,123,124,3,26,13,0,124,
        126,1,0,0,0,125,120,1,0,0,0,125,121,1,0,0,0,126,27,1,0,0,0,127,130,
        3,32,16,0,128,130,5,30,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,29,
        1,0,0,0,131,132,5,32,0,0,132,133,5,29,0,0,133,134,3,32,16,0,134,
        31,1,0,0,0,135,141,3,34,17,0,136,137,3,34,17,0,137,138,5,20,0,0,
        138,139,3,34,17,0,139,141,1,0,0,0,140,135,1,0,0,0,140,136,1,0,0,
        0,141,33,1,0,0,0,142,148,3,36,18,0,143,144,3,36,18,0,144,145,5,18,
        0,0,145,146,3,34,17,0,146,148,1,0,0,0,147,142,1,0,0,0,147,143,1,
        0,0,0,148,35,1,0,0,0,149,150,3,38,19,0,150,151,5,19,0,0,151,152,
        3,36,18,0,152,155,1,0,0,0,153,155,3,38,19,0,154,149,1,0,0,0,154,
        153,1,0,0,0,155,37,1,0,0,0,156,167,5,32,0,0,157,167,5,17,0,0,158,
        159,5,27,0,0,159,160,3,32,16,0,160,161,5,28,0,0,161,167,1,0,0,0,
        162,167,5,12,0,0,163,167,5,11,0,0,164,165,5,22,0,0,165,167,3,38,
        19,0,166,156,1,0,0,0,166,157,1,0,0,0,166,158,1,0,0,0,166,162,1,0,
        0,0,166,163,1,0,0,0,166,164,1,0,0,0,167,39,1,0,0,0,12,50,57,68,81,
        89,103,125,129,140,147,154,166
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'~'", "';'", 
                     "'.'", "':'", "','", "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "PROGRAM", "INTEGER", "BOOLEAN", 
                      "BEGIN", "END", "WHILE", "DO", "READ", "VAR", "FALSE", 
                      "TRUE", "WRITE", "IF", "THEN", "ELSE", "INT", "OPAD", 
                      "OPMULT", "OPREL", "OPLOG", "OPNEG", "PVIG", "PONTO", 
                      "DPONTOS", "VIG", "ABPAR", "FPAR", "ATRIB", "CADEIA", 
                      "WS", "ID" ]

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
    RULE_cmdWhile = 10
    RULE_cmdRead = 11
    RULE_cmdWrite = 12
    RULE_listW = 13
    RULE_elemW = 14
    RULE_cmdAtrib = 15
    RULE_expr = 16
    RULE_minExpr = 17
    RULE_term = 18
    RULE_fat = 19

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdWhile", "cmdRead", 
                   "cmdWrite", "listW", "elemW", "cmdAtrib", "expr", "minExpr", 
                   "term", "fat" ]

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
    INT=17
    OPAD=18
    OPMULT=19
    OPREL=20
    OPLOG=21
    OPNEG=22
    PVIG=23
    PONTO=24
    DPONTOS=25
    VIG=26
    ABPAR=27
    FPAR=28
    ATRIB=29
    CADEIA=30
    WS=31
    ID=32

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
            self.state = 40
            self.match(ExprParser.PROGRAM)
            self.state = 41
            self.match(ExprParser.ID)
            self.state = 42
            self.match(ExprParser.PVIG)
            self.state = 43
            self.decls()
            self.state = 44
            self.cmdComp()
            self.state = 45
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(ExprParser.VAR)
                self.state = 48
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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.declTip()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.declTip()
                self.state = 54
                self.match(ExprParser.VIG)
                self.state = 55
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
            self.state = 59
            self.listId()
            self.state = 60
            self.match(ExprParser.DPONTOS)
            self.state = 61
            self.tip()
            self.state = 62
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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ExprParser.ID)
                self.state = 66
                self.match(ExprParser.VIG)
                self.state = 67
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
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073741848) != 0)):
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
            self.state = 72
            self.match(ExprParser.BEGIN)
            self.state = 73
            self.listCmd()
            self.state = 74
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.cmd()
                self.state = 78
                self.match(ExprParser.PVIG)
                self.state = 79
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.cmdIf()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.cmdWhile()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.cmdRead()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.cmdWrite()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.cmdAtrib()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.cmdComp()
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

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CmdContext)
            else:
                return self.getTypedRuleContext(ExprParser.CmdContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(ExprParser.IF)
                self.state = 92
                self.expr()
                self.state = 93
                self.match(ExprParser.THEN)
                self.state = 94
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(ExprParser.IF)
                self.state = 97
                self.expr()
                self.state = 98
                self.match(ExprParser.THEN)
                self.state = 99
                self.cmd()
                self.state = 100
                self.match(ExprParser.ELSE)
                self.state = 101
                self.cmd()
                pass


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
        self.enterRule(localctx, 20, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ExprParser.WHILE)
            self.state = 106
            self.expr()
            self.state = 107
            self.match(ExprParser.DO)
            self.state = 108
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
        self.enterRule(localctx, 22, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ExprParser.READ)
            self.state = 111
            self.match(ExprParser.ABPAR)
            self.state = 112
            self.listId()
            self.state = 113
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
        self.enterRule(localctx, 24, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(ExprParser.WRITE)
            self.state = 116
            self.match(ExprParser.ABPAR)
            self.state = 117
            self.listW()
            self.state = 118
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
        self.enterRule(localctx, 26, self.RULE_listW)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.elemW()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.elemW()
                self.state = 122
                self.match(ExprParser.VIG)
                self.state = 123
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
        self.enterRule(localctx, 28, self.RULE_elemW)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 17, 22, 27, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expr()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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
        self.enterRule(localctx, 30, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ExprParser.ID)
            self.state = 132
            self.match(ExprParser.ATRIB)
            self.state = 133
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

        def minExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MinExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.MinExprContext,i)


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
        self.enterRule(localctx, 32, self.RULE_expr)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.minExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.minExpr()

                self.state = 137
                self.match(ExprParser.OPREL)
                self.state = 138
                self.minExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def minExpr(self):
            return self.getTypedRuleContext(ExprParser.MinExprContext,0)


        def OPAD(self):
            return self.getToken(ExprParser.OPAD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_minExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinExpr" ):
                listener.enterMinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinExpr" ):
                listener.exitMinExpr(self)




    def minExpr(self):

        localctx = ExprParser.MinExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_minExpr)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.term()

                self.state = 144
                self.match(ExprParser.OPAD)
                self.state = 145
                self.minExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fat(self):
            return self.getTypedRuleContext(ExprParser.FatContext,0)


        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def OPMULT(self):
            return self.getToken(ExprParser.OPMULT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.fat()

                self.state = 150
                self.match(ExprParser.OPMULT)
                self.state = 151
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.fat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

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

        def fat(self):
            return self.getTypedRuleContext(ExprParser.FatContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_fat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFat" ):
                listener.enterFat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFat" ):
                listener.exitFat(self)




    def fat(self):

        localctx = ExprParser.FatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_fat)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(ExprParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(ExprParser.INT)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(ExprParser.ABPAR)
                self.state = 159
                self.expr()
                self.state = 160
                self.match(ExprParser.FPAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.match(ExprParser.TRUE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.match(ExprParser.FALSE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.match(ExprParser.OPNEG)
                self.state = 165
                self.fat()
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






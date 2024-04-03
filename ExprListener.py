# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#decls.
    def enterDecls(self, ctx:ExprParser.DeclsContext):
        pass

    # Exit a parse tree produced by ExprParser#decls.
    def exitDecls(self, ctx:ExprParser.DeclsContext):
        pass


    # Enter a parse tree produced by ExprParser#listDecl.
    def enterListDecl(self, ctx:ExprParser.ListDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#listDecl.
    def exitListDecl(self, ctx:ExprParser.ListDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#declTip.
    def enterDeclTip(self, ctx:ExprParser.DeclTipContext):
        pass

    # Exit a parse tree produced by ExprParser#declTip.
    def exitDeclTip(self, ctx:ExprParser.DeclTipContext):
        pass


    # Enter a parse tree produced by ExprParser#listId.
    def enterListId(self, ctx:ExprParser.ListIdContext):
        pass

    # Exit a parse tree produced by ExprParser#listId.
    def exitListId(self, ctx:ExprParser.ListIdContext):
        pass


    # Enter a parse tree produced by ExprParser#tip.
    def enterTip(self, ctx:ExprParser.TipContext):
        pass

    # Exit a parse tree produced by ExprParser#tip.
    def exitTip(self, ctx:ExprParser.TipContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdComp.
    def enterCmdComp(self, ctx:ExprParser.CmdCompContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdComp.
    def exitCmdComp(self, ctx:ExprParser.CmdCompContext):
        pass


    # Enter a parse tree produced by ExprParser#listCmd.
    def enterListCmd(self, ctx:ExprParser.ListCmdContext):
        pass

    # Exit a parse tree produced by ExprParser#listCmd.
    def exitListCmd(self, ctx:ExprParser.ListCmdContext):
        pass


    # Enter a parse tree produced by ExprParser#cmd.
    def enterCmd(self, ctx:ExprParser.CmdContext):
        pass

    # Exit a parse tree produced by ExprParser#cmd.
    def exitCmd(self, ctx:ExprParser.CmdContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdIf.
    def enterCmdIf(self, ctx:ExprParser.CmdIfContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdIf.
    def exitCmdIf(self, ctx:ExprParser.CmdIfContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdIfElse.
    def enterCmdIfElse(self, ctx:ExprParser.CmdIfElseContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdIfElse.
    def exitCmdIfElse(self, ctx:ExprParser.CmdIfElseContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdWhile.
    def enterCmdWhile(self, ctx:ExprParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdWhile.
    def exitCmdWhile(self, ctx:ExprParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdRead.
    def enterCmdRead(self, ctx:ExprParser.CmdReadContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdRead.
    def exitCmdRead(self, ctx:ExprParser.CmdReadContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdWrite.
    def enterCmdWrite(self, ctx:ExprParser.CmdWriteContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdWrite.
    def exitCmdWrite(self, ctx:ExprParser.CmdWriteContext):
        pass


    # Enter a parse tree produced by ExprParser#listW.
    def enterListW(self, ctx:ExprParser.ListWContext):
        pass

    # Exit a parse tree produced by ExprParser#listW.
    def exitListW(self, ctx:ExprParser.ListWContext):
        pass


    # Enter a parse tree produced by ExprParser#elemW.
    def enterElemW(self, ctx:ExprParser.ElemWContext):
        pass

    # Exit a parse tree produced by ExprParser#elemW.
    def exitElemW(self, ctx:ExprParser.ElemWContext):
        pass


    # Enter a parse tree produced by ExprParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:ExprParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by ExprParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:ExprParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#exprAd.
    def enterExprAd(self, ctx:ExprParser.ExprAdContext):
        pass

    # Exit a parse tree produced by ExprParser#exprAd.
    def exitExprAd(self, ctx:ExprParser.ExprAdContext):
        pass


    # Enter a parse tree produced by ExprParser#exprMult.
    def enterExprMult(self, ctx:ExprParser.ExprMultContext):
        pass

    # Exit a parse tree produced by ExprParser#exprMult.
    def exitExprMult(self, ctx:ExprParser.ExprMultContext):
        pass


    # Enter a parse tree produced by ExprParser#exprDif.
    def enterExprDif(self, ctx:ExprParser.ExprDifContext):
        pass

    # Exit a parse tree produced by ExprParser#exprDif.
    def exitExprDif(self, ctx:ExprParser.ExprDifContext):
        pass



del ExprParser
# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\6\5\60\n\5\r\5\16\5\61")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\6\13V\n\13\r\13\16\13")
        buf.write("W\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2U\2\27\3\2\2")
        buf.write("\2\4#\3\2\2\2\6%\3\2\2\2\b+\3\2\2\2\n\63\3\2\2\2\f8\3")
        buf.write("\2\2\2\16?\3\2\2\2\20D\3\2\2\2\22K\3\2\2\2\24Q\3\2\2\2")
        buf.write("\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2")
        buf.write("\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34\5\24\13\2\34\35\7")
        buf.write("\b\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37$\5\6\4\2 $\5\b\5")
        buf.write("\2!$\5\f\7\2\"$\5\16\b\2#\37\3\2\2\2# \3\2\2\2#!\3\2\2")
        buf.write("\2#\"\3\2\2\2$\5\3\2\2\2%&\7\t\2\2&\'\7\n\2\2\'(\7\3\2")
        buf.write("\2()\7\t\2\2)*\7\13\2\2*\7\3\2\2\2+,\7\t\2\2,-\7\n\2\2")
        buf.write("-/\7\4\2\2.\60\5\n\6\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2")
        buf.write("\2\2\61\62\3\2\2\2\62\t\3\2\2\2\63\64\7\t\2\2\64\65\7")
        buf.write("\n\2\2\65\66\7\t\2\2\66\67\7\17\2\2\67\13\3\2\2\289\7")
        buf.write("\t\2\29:\7\n\2\2:;\7\7\2\2;<\7\t\2\2<=\7\f\2\2=>\7\t\2")
        buf.write("\2>\r\3\2\2\2?@\7\t\2\2@A\7\n\2\2AB\7\6\2\2BC\5\20\t\2")
        buf.write("C\17\3\2\2\2DE\7\t\2\2EF\7\22\2\2FG\5\22\n\2GH\7\20\2")
        buf.write("\2HI\5\22\n\2IJ\7\21\2\2J\21\3\2\2\2KL\7\r\2\2LM\7\t\2")
        buf.write("\2MN\7\20\2\2NO\7\t\2\2OP\7\16\2\2P\23\3\2\2\2QR\7\t\2")
        buf.write("\2RS\7\n\2\2SU\7\5\2\2TV\7\t\2\2UT\3\2\2\2VW\3\2\2\2W")
        buf.write("U\3\2\2\2WX\3\2\2\2X\25\3\2\2\2\6\31#\61W")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PREGUNTA'", "'RESPOSTA'", "'ENQUESTA'", 
                     "'ALTERNATIVA'", "'ITEM'", "'END'", "<INVALID>", "':'", 
                     "'?'", "'->'", "'('", "')'", "';'", "','", "']'", "'['" ]

    symbolicNames = [ "<INVALID>", "PREGUNTA", "RESPOSTA", "ENQUESTA", "ALTERNATIVA", 
                      "ITEM", "END", "PARAULA", "DOS_PUNTS", "INTERROGACIO", 
                      "FLETXA", "L_P", "R_P", "PUNT_COMA", "COMA", "R_B", 
                      "L_B", "WS", "RET" ]

    RULE_root = 0
    RULE_opcio = 1
    RULE_pregunta = 2
    RULE_resposta = 3
    RULE_possible_resposta = 4
    RULE_item = 5
    RULE_alternativa = 6
    RULE_implicacio = 7
    RULE_canvi = 8
    RULE_enquesta = 9

    ruleNames =  [ "root", "opcio", "pregunta", "resposta", "possible_resposta", 
                   "item", "alternativa", "implicacio", "canvi", "enquesta" ]

    EOF = Token.EOF
    PREGUNTA=1
    RESPOSTA=2
    ENQUESTA=3
    ALTERNATIVA=4
    ITEM=5
    END=6
    PARAULA=7
    DOS_PUNTS=8
    INTERROGACIO=9
    FLETXA=10
    L_P=11
    R_P=12
    PUNT_COMA=13
    COMA=14
    R_B=15
    L_B=16
    WS=17
    RET=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def opcio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 20
                    self.opcio()

                else:
                    raise NoViableAltException(self)
                self.state = 23 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 25
            self.enquesta()
            self.state = 26
            self.match(EnquestesParser.END)
            self.state = 27
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pregunta(self):
            return self.getTypedRuleContext(EnquestesParser.PreguntaContext,0)


        def resposta(self):
            return self.getTypedRuleContext(EnquestesParser.RespostaContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def alternativa(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativaContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_opcio




    def opcio(self):

        localctx = EnquestesParser.OpcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_opcio)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.pregunta()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.resposta()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.item()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.alternativa()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreguntaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def INTERROGACIO(self):
            return self.getToken(EnquestesParser.INTERROGACIO, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_pregunta




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pregunta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(EnquestesParser.PARAULA)
            self.state = 36
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 37
            self.match(EnquestesParser.PREGUNTA)
            self.state = 38
            self.match(EnquestesParser.PARAULA)
            self.state = 39
            self.match(EnquestesParser.INTERROGACIO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self):
            return self.getToken(EnquestesParser.PARAULA, 0)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def possible_resposta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.Possible_respostaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.Possible_respostaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resposta




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(EnquestesParser.PARAULA)
            self.state = 42
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 43
            self.match(EnquestesParser.RESPOSTA)
            self.state = 45 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 44
                    self.possible_resposta()

                else:
                    raise NoViableAltException(self)
                self.state = 47 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Possible_respostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def PUNT_COMA(self):
            return self.getToken(EnquestesParser.PUNT_COMA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_possible_resposta




    def possible_resposta(self):

        localctx = EnquestesParser.Possible_respostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_possible_resposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(EnquestesParser.PARAULA)
            self.state = 50
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 51
            self.match(EnquestesParser.PARAULA)
            self.state = 52
            self.match(EnquestesParser.PUNT_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def FLETXA(self):
            return self.getToken(EnquestesParser.FLETXA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(EnquestesParser.PARAULA)
            self.state = 55
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 56
            self.match(EnquestesParser.ITEM)
            self.state = 57
            self.match(EnquestesParser.PARAULA)
            self.state = 58
            self.match(EnquestesParser.FLETXA)
            self.state = 59
            self.match(EnquestesParser.PARAULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self):
            return self.getToken(EnquestesParser.PARAULA, 0)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def implicacio(self):
            return self.getTypedRuleContext(EnquestesParser.ImplicacioContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_alternativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(EnquestesParser.PARAULA)
            self.state = 62
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 63
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 64
            self.implicacio()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImplicacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self):
            return self.getToken(EnquestesParser.PARAULA, 0)

        def L_B(self):
            return self.getToken(EnquestesParser.L_B, 0)

        def canvi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.CanviContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.CanviContext,i)


        def COMA(self):
            return self.getToken(EnquestesParser.COMA, 0)

        def R_B(self):
            return self.getToken(EnquestesParser.R_B, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_implicacio




    def implicacio(self):

        localctx = EnquestesParser.ImplicacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(EnquestesParser.PARAULA)
            self.state = 67
            self.match(EnquestesParser.L_B)
            self.state = 68
            self.canvi()
            self.state = 69
            self.match(EnquestesParser.COMA)
            self.state = 70
            self.canvi()
            self.state = 71
            self.match(EnquestesParser.R_B)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CanviContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_P(self):
            return self.getToken(EnquestesParser.L_P, 0)

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def COMA(self):
            return self.getToken(EnquestesParser.COMA, 0)

        def R_P(self):
            return self.getToken(EnquestesParser.R_P, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_canvi




    def canvi(self):

        localctx = EnquestesParser.CanviContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_canvi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(EnquestesParser.L_P)
            self.state = 74
            self.match(EnquestesParser.PARAULA)
            self.state = 75
            self.match(EnquestesParser.COMA)
            self.state = 76
            self.match(EnquestesParser.PARAULA)
            self.state = 77
            self.match(EnquestesParser.R_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def DOS_PUNTS(self):
            return self.getToken(EnquestesParser.DOS_PUNTS, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(EnquestesParser.PARAULA)
            self.state = 80
            self.match(EnquestesParser.DOS_PUNTS)
            self.state = 81
            self.match(EnquestesParser.ENQUESTA)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.match(EnquestesParser.PARAULA)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.PARAULA):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






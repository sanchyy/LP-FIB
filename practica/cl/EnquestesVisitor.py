# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

import networkx as nx

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
class EnquestesVisitor(ParseTreeVisitor):
    items = {} 
    primera_pregunta = None
    ultima_pregunta = None

    def __init__(self):
        self.G = nx.DiGraph()


    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        p_id, preg = ctx.getText().split(':PREGUNTA')
        self.G.add_node("PREGUNTA:{}:{}".format(p_id, preg))
        if self.primera_pregunta is None:
            self.primera_pregunta = p_id
        else:
            self.G.add_edge(self.ultima_pregunta, p_id)
        self.ultima_pregunta = p_id
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        r_id, resp = ctx.getText().split(':RESPOSTA') 
        self.G.add_node("RESPOSTA:{}:{}".format(r_id, resp))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#possible_resposta.
    def visitPossible_resposta(self, ctx:EnquestesParser.Possible_respostaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        i_id, _ = ctx.getText().split(':ITEM')
        p_id, r_id = _.split('->')
        self.items[i_id] = (p_id, r_id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#implicacio.
    def visitImplicacio(self, ctx:EnquestesParser.ImplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#canvi.
    def visitCanvi(self, ctx:EnquestesParser.CanviContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        ids = ctx.getText().replace(':ENQUESTA', ' ').split(' ')
        e_id = ids[0]
        items_id = list(filter(lambda x: x in self.items, ids[1:]))
        for item in items_id:
            self.G.add_edges_from([self.items[item]])
        print(self.primera_pregunta)
        self.G.add_edge(e_id, self.primera_pregunta)
        nx.draw(self.G)
        
        return self.visitChildren(ctx)



# del EnquestesParser

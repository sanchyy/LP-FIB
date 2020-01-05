grammar Enquestes;

root : opcio+ enquesta END EOF   ;

opcio : pregunta
    |   resposta
    |   item
    |   alternativa
    ;

pregunta            : PARAULA DOS_PUNTS PREGUNTA PARAULA INTERROGACIO   ;
resposta            : PARAULA DOS_PUNTS RESPOSTA possible_resposta+     ;
possible_resposta   : PARAULA DOS_PUNTS PARAULA PUNT_COMA               ; 
item                : PARAULA DOS_PUNTS ITEM  PARAULA FLETXA PARAULA    ; 
alternativa         : PARAULA DOS_PUNTS ALTERNATIVA implicacio          ;
implicacio          : PARAULA L_B canvi COMA canvi R_B                  ;
canvi               : L_P PARAULA COMA PARAULA R_P                      ; 
enquesta            : PARAULA  DOS_PUNTS ENQUESTA PARAULA+              ;

//TOKENS


//PARAULES
PREGUNTA    : 'PREGUNTA'    ;
RESPOSTA    : 'RESPOSTA'    ;
ENQUESTA    : 'ENQUESTA'    ;
ALTERNATIVA : 'ALTERNATIVA' ;
ITEM        : 'ITEM'        ;
END         : 'END'         ;

PARAULA: [a-zA-Z0-9]+ ( ' ' PARAULA)* ;

//SIGNES PUNTUACIO o SIMBOLS
DOS_PUNTS   : ':'           ;
INTERROGACIO: '?'           ;
FLETXA      : '->'          ;
L_P         : '('           ;
R_P         : ')'           ;
PUNT_COMA   : ';'           ;
COMA        : ','           ;
R_B         : ']'           ;
L_B         : '['           ;

//SKIPS
WS  : [ \n]+  -> skip       ;
RET : [\r]+ -> skip         ;

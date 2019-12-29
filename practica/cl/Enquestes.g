grammar Enquestes;

root : opcio+ enquesta END EOF   ;

opcio : pregunta
    |   resposta
    |   item
    |   alternativa
    ;

pregunta : ID DOS_PUNTS PREGUNTA FRASE INTERROGACIO     ;
resposta : ID DOS_PUNTS RESPOSTA possible_resposta+     ;
possible_resposta : ID DOS_PUNTS FRASE PUNT_COMA        ; 
item : ID DOS_PUNTS ITEM  ID FLETXA ID                  ; 
alternativa : ID DOS_PUNTS ALTERNATIVA implicacio       ;
implicacio : L_B canvi COMA canvi R_B                   ;
canvi : L_P NUM COMA ID R_P                             ; 
enquesta : ID DOS_PUNTS ENQUESTA ID+                    ;

//TOKENS

//SKIPS
WS: [ \n]+ -> skip                      ;

//PARAULES
PREGUNTA : 'PREGUNTA'                   ;
RESPOSTA : 'RESPOSTA'                   ;
ENQUESTA : 'ENQUESTA'                   ;
ALTERNATIVA : 'ALTERNATIVA'             ;
ITEM : 'ITEM'                           ;
END : 'END'                             ;

//REGEX
FRASE : [a-zA-Z0-9]+                    ;
ID : [a-zA-Z0-9]+                       ;
NUM : [0-9]+                            ;

//SIGNES PUNTUACIO o SIMBOLS
DOS_PUNTS : ':'                         ;
INTERROGACIO : '?'                      ;
FLETXA : '->'                           ;
L_P : '('                               ;
R_P : ')'                               ;
PUNT_COMA : ';'                         ;
COMA : ','                              ;
R_B : ']'                               ;
L_B : '['                               ;

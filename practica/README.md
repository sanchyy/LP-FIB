# Pràctica QuizBot LP

## Instal·lació
```bash
virtualenv venv --python=python3
. venv/bin/activate
pip install -r requirements.txt
```

## Ús del compilador
Per a usar el compilador d'enquestes caldra omplir un _.txt_ seguin el format de les opcions següents:   
· La pregunta serà una pregunta del qüestionari  
· La resposta serà un conjunt de posslbes respostes  
· L'item, unirà una pregunta amb un conjunt de respostes  
· L'alternativa unirà una resposta d'una pregunta amb una nova pregunta  
· Enquesta dirà quins items formaran part de l'enquesta   

### Format
* PREGUNTA: _id pregunta_ : PREGUNTA _pregunta_
* RESPOSTA: _id resposta_ : RESPOSTA 
    * POSSIBLE RESPOSTA: _id_ : _resposta_ ; 
* ITEM: _id item_ : ITEM _id pregunta_ -> _id resposta_
* ALTERNATIVA: _id alt_ : ALTERNATIVA _id item_ [(_possible resposta_ , _id item_)]
* ENQUESTA: _id item_ ...

· Quan es crea una enquesta cal crear un fitxer a /resultats amb el nom=idenquesta i que contingui el valor dels id de les preguntes amb les possibles respostes inicialitzades a 0. Tot això en format .json
### Execució compilador
```bash
python cl.py enquestes/<nom_enquesta>.txt
```

## Ús bot
Al fitxer config.py omplir la variable TOKEN amb el vostre token de telegram
```python
TOKEN='#############'
```

### Execució del bot
```bash
python bot.py
```

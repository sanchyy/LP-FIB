from config import TOKEN
from telegram.ext import Updater
from telegram.ext import CommandHandler
import networkx as nx
import pickle

class Bot:
    ''' /start: Inicialitzar el bot 
/help: Desplegarà el menú d'ajuda amb les possibles comandes 
/author: Es retorna el nom i correu electrònic de l'autor del projecte 
/quiz id_enquesta: s'iniciarà l'enquesta amb id = id_enquesta 
/bar id_pregunta: es retornarà mitjançant un gràfic de barres la distribució de les respostes donades 
/pie id_pregunta: es retorna amb una gràfica tipus formatget amb percentatge de respostes a la pregunta 
/report es retorna una taula amb el nombre de respostes obtingudes per cada valor de cada pregunta
    '''

    def __init__(self, token):
        self.token = token
        self.updater = Updater(token=self.token)
        self.dispatcher = self.updater.dispatcher
        self.id_enquesta = None
        
    def init_commands(self):
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(CommandHandler('author', self.author))
        self.dispatcher.add_handler(CommandHandler('quiz', self.quiz))
        self.dispatcher.add_handler(CommandHandler('bar', self.bar))
        self.dispatcher.add_handler(CommandHandler('pie', self.pie))
        self.dispatcher.add_handler(CommandHandler('report', self.report))

    def start(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Benvingut al QuizBot!")

    def help(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.__doc__)

    def author(self, bot, update):
        msg = '''
Autor: Víctor Sánchez Gassull
e-mail: victor.sanchez.gassull@est.fib.upc.edu
        '''
        bot.send_message(chat_id=update.message.chat_id, text=msg)

    def quiz(self, bot, update):
        self.id_enquesta = update.message.text[6:]  # remove string: "/quiz "
        if len(self.id_enquesta) < 1:
            bot.send_message(chat_id=update.message.chat_id, text='Usage: /Quiz identificador')
            return
        try:
            self.enquesta = pickle.load(open('../data/{}.dat'.format(self.id_enquesta), 'rb')) 
        except:
            bot.send_message(chat_id=update.message.chat_id, text='No hi ha cap enquesta amb aquest identificador')
            return

        # Do some loop waiting for the answer
        print(nx.neighbors(self.id_enquesta))
        print(self.enquesta)
        sep = msg.split(':')

        # actualitzar puntuacio
        with open('../resultats/{}.json'.format(self.id_enquesta), 'r') as f:
            data = json.load(f.readi())
        data[question] += 1
        with open('../resultats/{}.json'.format(self.id_enquesta), 'w') as f:
            json.dump(f, data)

        # op.update_grade(update.message.text)
        

    def bar(self, bot, update):
        question = update.message.text[5:]  # remove string "/bar " 
        with open('../resultats/{}.json', 'r') as f:
            data = json.load(f.readi())
        k, v = data.items() 
        plt.bar(k,v)
        plt.savefig('../static/{}_{}.png'.format(id_enquesta, question))
        bot.send_photo(chat_id=update.message.chat_id, photo=open('../static/{}_{}.png'.format(id_enquesta, question)))

    def pie(self, bot, update):
        question = update.message.text[5:]  # remove string "/pie "
        with open('../resultats/{}.json', 'r') as f:
            data = json.load(f.readi())
        k, v = data.items() 
        plt.bar(k,v)
        plt.savefig('../static/{}_{}.png'.format(id_enquesta, question))
        bot.send_photo(chat_id=update.message.chat_id, photo=open('../static/{}_{}.png'.format(id_enquesta, question)))

    def report(self, bot, update):
        return "uwu"
    def start(self):
        self.updater.start_polling()

if __name__ == '__main__':
    bot = Bot(TOKEN)
    bot.init_commands()
    bot.start()

import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '383554977:AAFWErULgIZ9492Kp_nWWALfL4ckNijEWhw'
WEBHOOK_URL = 'https://5774681b.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
		'intro',
		'circle_fork',
		'circle_fork_start',
		'circle_fork_end',
		'mora',
		'mora_end'
    ],
    transitions=[
		{
		    'trigger':'advance',
			'source':'user',
			'dest':'intro',
			'conditions':'askIntro'
		},
		{
		    'trigger':'advance',
			'source':'user',
			'dest':'circle_fork',
			'conditions':'playCircleFork'
		},
		{
		    'trigger':'advance',
			'source':'circle_fork',
			'dest':'circle_fork_start',
			'conditions':'startCircleFork'
		},
		{
		    'trigger':'advance',
			'source':'circle_fork_start',
			'dest':'circle_fork_start',
			'conditions':'chooseCircleFork'
		},
		{
			'trigger':'end',
			'source':'circle_fork_start',
			'dest':'circle_fork_end',
			'conditions':'endCircleFork'
		},
		{
		    'trigger':'advance',
			'source':'circle_fork_end',
			'dest':'circle_fork',
			'conditions':'againCircleFork'
		},
		{
		    'trigger':'advance',
			'source':'user',
			'dest':'mora',
			'conditions':'play_mora'
		},
		{
		    'trigger':'advance',
			'source':'mora',
			'dest':'mora_end',
			'conditions':'chooseHand'
		},
		{
		    'trigger':'advance',
			'source':'mora_end',
			'dest':'mora',
			'conditions':'moraPlayAgain'
		},
        {
            'trigger': 'go_back',
            'source': [
				'intro',
				'mora_end',
				'circle_fork_end'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
   byte_io = BytesIO()
   machine.graph.draw(byte_io, prog='dot', format='png')
   byte_io.seek(0)
   return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()

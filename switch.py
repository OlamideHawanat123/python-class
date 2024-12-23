nokia = (input
('''
1) phonebook
2) Messages
3) chat
4) Call register
5) Tones
6) Settings
7) Call divert
8) Games
9) Calculator
10) Reminders
11) Clock
12) Profiles
13) SIM services
'''))

match nokia:
	case "phonebook":
		one = (input
('''
1) Search
2) Service nos
3) Add name
4) Erase
5) Edit
6) Asign tone
7) Send b'card 
8) Options
9) Speed dials
10) Voice tags
'''))
		case "options":
			eight = (input

('''
1) Type of view
2) Memory status
'''))

	case "messages":
		two = (input
('''
1) Write Messages 
2) Inbox
3) Outbox
4) Picture messages
5) Templates
6) Smileys
7) Message settings
8) Info service
9) Voice mailbox number
10) Service Command Editor
'''))

	case "Message settings":
		seven = (input
('''
1) Set
2) Common
'''))

	case "set":
		one = (input
('''
1) Message centre number
2) Message sent as
3) Message validity
'''))
	case "common":
		two = (input
('''
1) Delivery reports
2) Reply via same centre
3) Character support
'''))
	













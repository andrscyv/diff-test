from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'editor',
        'name': 'first_name',
        'message': 'What\'s your first name',
        'default':'vim'
    }
]

answers = prompt(questions)
print_json(answers)  # use the answers as input for your app

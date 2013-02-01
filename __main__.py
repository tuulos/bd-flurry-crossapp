
from bitdeli import profiles
from bitdeli.widgets import Widget, Text, Title, Description, set_theme
from itertools import imap, chain
from datetime import datetime 

set_theme('eighties')

MINUTES = 60

class Matrix(Widget):
    defaults = {'size': [3,3]}

data = []
for profile in profiles():
    row = [0] * MINUTES
    for session in profile['sessions']:
        for event in session['l']:
           col = min(MINUTES - 1, event['o'] / 60000)
           row[col] = min(row[col] + 0.1, 1.0)
    data.append(row)

data.sort(key=lambda r: sum(r), reverse=True)
data = data[:3000]

Text(size=(12,2),
     data={'head': "Session activity over the first 60 minutes",
           'text': "%d most active users" % len(data)})

Matrix(size=[12,12],
       color=2,
       data=data)

Title('Retention')
Description('Active segments: **9 / 32 / 234**')
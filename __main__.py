
from bitdeli import profiles
from bitdeli.widgets import Widget, Text, Title, Description, set_theme
from itertools import imap, chain
from datetime import datetime 

set_theme('purple')

DAYS = 100

class Matrix(Widget):
    defaults = {'size': [3,3]}

def day(session):
    return datetime.utcfromtimestamp(session['t'] / 1000.).toordinal()

data = []
for profile in profiles():
    days = frozenset(imap(day, profile['sessions']))
    first = min(days)
    row = [0] * DAYS
    for i in range(DAYS):
        if i + first in days:
            row[i] = 1
        data.append(row)

data.sort(key=lambda r: sum(r), reverse=True)
data = data[:3000]

Text(size=(2,2),
     data={'head': len(data)})

Matrix(size=[12,12],
       color=2,
       data=data)

Title('Retention')
Description('Active segments: **9 / 32 / 234**')
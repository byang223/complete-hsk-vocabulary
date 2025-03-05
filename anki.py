import genanki
import json
from hanziconv import HanziConv

_filename = 'complete.json'
with open(_filename, 'r') as file:
    data = json.load(file)

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Vocab'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Vocab}}',
      'afmt': '{{FrontSide}}<hr id="Answer">{{Answer}}',
    },
  ])

my_deck = genanki.Deck(
  2059400110,
  'Traditional Chinese')

for e in data:
    try:
        tradChar = HanziConv.toTraditional(e['simplified'])
    except:
        print(e)
        exit(1)
    forms = []
    for form in e['forms']:
        meanings = '\n'.join(form['meanings'])
        forms.append(f'{form['transcriptions']['pinyin']}\n{meanings}')
    answer = '\n\n'.join(forms)
    my_note = genanki.Note(
        model=my_model,
        fields=[tradChar, answer])
    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('chinese.apkg')

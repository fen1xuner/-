#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QLineEdit, QListWidget, QTextEdit, QInputDialog)








app = QApplication([])
notes = []
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900,600)

field_text = QTextEdit()
list_notes_label = QLabel('Список заметок')
list_notes = QListWidget()




button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')


list_tags_label = QLabel('Список тегов')
list_tags = QListWidget()
field_tag = QLineEdit()
field_tag.setPlaceholderText('Введите тег ...')
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')


layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)



layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)


def add_note():
    note_name, ok = QInputDialog.getText(notes_win,'Добавить заметку','Название заметки:')
    if ok and note_name != '':
        note = [note_name, '',[]]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        with open(str(len(notes)-1)+ '.txt', 'w',encoding='utf-8') as f:
            f.write(note[0] + '\n')
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index) + '.txt', 'w',encoding='utf-8') as f:
                    f.write(note[0]+'\n')
                    f.write(note[1]+'\n') 
                    for tag in note[2]:
                        f.write(tag)
                    f.write('\n')
            zindex += 1







list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)

button_note_save.clicked.connect(save_note)

#button_tag_save.clicked.connect(save_tag)





name = 0
note = []
while True:
    filename = str(name) + '.txt'
    try:
        with open(filename, 'r',encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n','')
                note.append(line)
            tags = note[2].split(' ')
            note[2] = tags

            notes.append(note)
            note = []
            name += 1 
    
    except:
        break







print(notes)
for note in notes:
    list_notes.addItem(note[0])






notes_win.show()
app.exec()
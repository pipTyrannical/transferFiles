# Use this if you don't want to run the .exe file

import shutil
import time
from pathlib2 import Path
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit


def show_curency(src, suff, dst, min_age):
    filepaths = Path(src).iterdir()
    for path in filepaths:
        if path.is_file():
            age = time.time() - path.stat().st_ctime
            if path.suffix == suff and age < min_age:
                print(f"Moving {path.name}")
                newpath = dst
                print((age / 3600, "hours since creation"))
                shutil.move(path, newpath)
                print(f"Moving {path.name}...")
            elif path.suffix == suff and age > min_age:
                print(f"Skipping {path.name}, older than 1 day. {age / 3600} hours since creation)")
    output_label.setText('Done')



app = QApplication([])
window = QWidget()
window.setWindowTitle('Transfer Files | Specify Age & Suffix')

layout = QVBoxLayout()

layout.addWidget(QLabel(r'↓ Enter the path to extract files from. (i.e C://, D:\folder, etc). ↓'))
src = QLineEdit()
layout.addWidget(src)

layout.addWidget(QLabel(r'↓ Enter the filetype to extract from the directory. (i.e .mp4, .dll, etc) ↓'))
suff = QLineEdit()
layout.addWidget(suff)

layout.addWidget(QLabel(r'↓ Enter the path to moves the files to. (i.e C://, D:\folder, etc) ↓'))
dst = QLineEdit("")
layout.addWidget(dst)

layout.addWidget(QLabel(r'↓ Enter the maximum age for the file in hours. (i.e 24, 168, etc) ↓'))
min_age = QLineEdit()
layout.addWidget(min_age)

btn = QPushButton('Transfer')
layout.addWidget(btn)

btn.clicked.connect(lambda:show_curency(str(src.text()), str(suff.text()), str(dst.text()), int(min_age.text())))

output_label = QLabel('')
layout.addWidget(output_label)


window.setWindowIcon(QtGui.QIcon('icon.png'))
window.setLayout(layout)
window.show()
app.exec()

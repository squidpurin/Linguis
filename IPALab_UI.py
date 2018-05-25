import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from T2SIC import Ui_ot as Uii
from text_2_speechFIN import *
from ipa_chart_soundsFIN import *
from user import *

class IPALabUI(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
        self.ui = Uii()
        self.ui.setupUi(self)
        self.ui.p.clicked.connect(self.clickPhoneme)
        self.ui.b.clicked.connect(self.clickPhoneme)
        self.ui.m.clicked.connect(self.clickPhoneme)
        self.ui.br.clicked.connect(self.clickPhoneme)
        self.ui.vh.clicked.connect(self.clickPhoneme)
        self.ui.fh.clicked.connect(self.clickPhoneme)
        self.ui.mh.clicked.connect(self.clickPhoneme)
        self.ui.vr.clicked.connect(self.clickPhoneme)
        self.ui.v.clicked.connect(self.clickPhoneme)
        self.ui.f.clicked.connect(self.clickPhoneme)
        self.ui.vi.clicked.connect(self.clickPhoneme)
        self.ui.z_.clicked.connect(self.clickPhoneme)
        self.ui.n_.clicked.connect(self.clickPhoneme)
        self.ui.d_.clicked.connect(self.clickPhoneme)
        self.ui.r_.clicked.connect(self.clickPhoneme)
        self.ui.l_.clicked.connect(self.clickPhoneme)
        self.ui.rh_.clicked.connect(self.clickPhoneme)
        self.ui.s.clicked.connect(self.clickPhoneme)
        self.ui.lh.clicked.connect(self.clickPhoneme)
        self.ui.dh.clicked.connect(self.clickPhoneme)
        self.ui.th.clicked.connect(self.clickPhoneme)
        self.ui.t.clicked.connect(self.clickPhoneme)
        self.ui.sh.clicked.connect(self.clickPhoneme)
        self.ui.zh_2.clicked.connect(self.clickPhoneme)
        self.ui.t_.clicked.connect(self.clickPhoneme)
        self.ui.s_.clicked.connect(self.clickPhoneme)
        self.ui.ny.clicked.connect(self.clickPhoneme)
        self.ui.ghy.clicked.connect(self.clickPhoneme)
        self.ui.c.clicked.connect(self.clickPhoneme)
        self.ui.j.clicked.connect(self.clickPhoneme)
        self.ui.xy.clicked.connect(self.clickPhoneme)
        self.ui.ly.clicked.connect(self.clickPhoneme)
        self.ui.jy.clicked.connect(self.clickPhoneme)
        self.ui.g.clicked.connect(self.clickPhoneme)
        self.ui.k.clicked.connect(self.clickPhoneme)
        self.ui.ng.clicked.connect(self.clickPhoneme)
        self.ui.x.clicked.connect(self.clickPhoneme)
        self.ui.gh.clicked.connect(self.clickPhoneme)
        self.ui.lg.clicked.connect(self.clickPhoneme)
        self.ui.jg.clicked.connect(self.clickPhoneme)
        self.ui.ghq.clicked.connect(self.clickPhoneme)
        self.ui.nq.clicked.connect(self.clickPhoneme)
        self.ui.xq.clicked.connect(self.clickPhoneme)
        self.ui.q.clicked.connect(self.clickPhoneme)
        self.ui.gq.clicked.connect(self.clickPhoneme)
        self.ui.rq.clicked.connect(self.clickPhoneme)
        self.ui.h.clicked.connect(self.clickPhoneme)
        self.ui.hhh.clicked.connect(self.clickPhoneme)
        self.ui.hh.clicked.connect(self.clickPhoneme)
        self.ui.ha.clicked.connect(self.clickPhoneme)
        self.ui.xa.clicked.connect(self.clickPhoneme)
        self.ui.rh.clicked.connect(self.clickPhoneme)
        self.ui.n.clicked.connect(self.clickPhoneme)
        self.ui.zh.clicked.connect(self.clickPhoneme)
        self.ui.r.clicked.connect(self.clickPhoneme)
        self.ui.l.clicked.connect(self.clickPhoneme)
        self.ui.d.clicked.connect(self.clickPhoneme)
        self.ui.rr.clicked.connect(self.clickPhoneme)
        self.ui.lzh.clicked.connect(self.clickPhoneme)
        self.ui.ac.clicked.connect(self.clickPhoneme)
        self.ui.dc.clicked.connect(self.clickPhoneme)
        self.ui.bc.clicked.connect(self.clickPhoneme)
        self.ui.alc.clicked.connect(self.clickPhoneme)
        self.ui.pac.clicked.connect(self.clickPhoneme)
        self.ui.gqi.clicked.connect(self.clickPhoneme)
        self.ui.gi.clicked.connect(self.clickPhoneme)
        self.ui.ji.clicked.connect(self.clickPhoneme)
        self.ui.bi.clicked.connect(self.clickPhoneme)
        self.ui.di.clicked.connect(self.clickPhoneme)
        self.ui.pe.clicked.connect(self.clickPhoneme)
        self.ui.te.clicked.connect(self.clickPhoneme)
        self.ui.ke.clicked.connect(self.clickPhoneme)
        self.ui.se.clicked.connect(self.clickPhoneme)
        self.ui.wy.clicked.connect(self.clickPhoneme)
        self.ui.wh.clicked.connect(self.clickPhoneme)
        self.ui.heg.clicked.connect(self.clickPhoneme)
        self.ui.w.clicked.connect(self.clickPhoneme)
        self.ui.aeg.clicked.connect(self.clickPhoneme)
        self.ui.xeg.clicked.connect(self.clickPhoneme)
        self.ui.zy.clicked.connect(self.clickPhoneme)
        self.ui.lll.clicked.connect(self.clickPhoneme)
        self.ui.kp.clicked.connect(self.clickPhoneme)
        self.ui.sy.clicked.connect(self.clickPhoneme)
        self.ui.i.clicked.connect(self.clickPhoneme)
        self.ui.y.clicked.connect(self.clickPhoneme)
        self.ui.il.clicked.connect(self.clickPhoneme)
        self.ui.yl.clicked.connect(self.clickPhoneme)
        self.ui.oe.clicked.connect(self.clickPhoneme)
        self.ui.e.clicked.connect(self.clickPhoneme)
        self.ui.et.clicked.connect(self.clickPhoneme)
        self.ui.oet.clicked.connect(self.clickPhoneme)
        self.ui.oett.clicked.connect(self.clickPhoneme)
        self.ui.a.clicked.connect(self.clickPhoneme)
        self.ui.ae.clicked.connect(self.clickPhoneme)
        self.ui.ih.clicked.connect(self.clickPhoneme)
        self.ui.uh.clicked.connect(self.clickPhoneme)
        self.ui.eh.clicked.connect(self.clickPhoneme)
        self.ui.oh.clicked.connect(self.clickPhoneme)
        self.ui.a_.clicked.connect(self.clickPhoneme)
        self.ui.eht.clicked.connect(self.clickPhoneme)
        self.ui.aw.clicked.connect(self.clickPhoneme)
        self.ui.oht.clicked.connect(self.clickPhoneme)
        self.ui.eu.clicked.connect(self.clickPhoneme)
        self.ui.u.clicked.connect(self.clickPhoneme)
        self.ui.ul.clicked.connect(self.clickPhoneme)
        self.ui.ue.clicked.connect(self.clickPhoneme)
        self.ui.o.clicked.connect(self.clickPhoneme)
        self.ui.aht.clicked.connect(self.clickPhoneme)
        self.ui.pushButton_110.clicked.connect(self.clickPhoneme)
        self.ui.ah.clicked.connect(self.clickPhoneme)
        self.ui.ao.clicked.connect(self.clickPhoneme)

        self.ui.pron_mode.setChecked(True)
        self.mode = 0
        self.player = AudioPlayer()
        self.ui.pron_mode.pressed.connect(self.modeSwitch)
        self.ui.t2s_mode.pressed.connect(self.modeSwitch)
        self.ui.t2s_input.setDisabled(True)
        self.ui.t2s_pronunce.setDisabled(True)
        self.ui.savePron.setDisabled(True)
        self.ui.t2s_pronunce.clicked.connect(self.pronunceAll)
        
        self.ui.fav_mode.pressed.connect(self.modeSwitch)
        self.ui.addfav.clicked.connect(self.addFavorite)

        self.ui.savePron.clicked.connect(self.savePronunciation)
        
    def modeSwitch(self):
        if self.sender().text() == "Pronunce alphabet mode":
            self.player = AudioPlayer()
            self.mode = 0
            self.ui.t2s_input.setText('')
            self.ui.t2s_input.setDisabled(True)
            self.ui.t2s_pronunce.setDisabled(True)
            self.ui.savePron.setDisabled(True)
        elif self.sender().text() == "Text-to-speech mode":
            self.player = Text2Speech()
            self.mode = 1
            self.ui.t2s_input.setDisabled(False)
            self.ui.t2s_pronunce.setDisabled(False)
            self.ui.savePron.setDisabled(False)
        else:
            self.mode = 2
            self.ui.t2s_input.setText('')
            self.ui.t2s_input.setDisabled(False)
            self.ui.t2s_pronunce.setDisabled(True)
            self.ui.savePron.setDisabled(True)

    def clickPhoneme(self):
        phoneme = self.sender().text()
        if self.mode == 0:
            self.player.play_audio(phoneme)
        elif self.mode == 1:
            self.ui.t2s_input.setText(self.ui.t2s_input.text() + phoneme)
        else:
            self.ui.t2s_input.setText(self.ui.t2s_input.text() + phoneme)

    def savePronunciation(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"Save pronunciation file...")
        sequence = self.player.decode(self.ui.t2s_input.text())
        if fileName.find(".wav") == -1:
            fileName += ".wav"
        self.player.wav_combine(sequence, fileName)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Pronunciation saved.")
        msg.setWindowTitle("Saved")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()        
          
    def pronunceAll(self):
        sequence = self.player.decode(self.ui.t2s_input.text())
        self.player.wav_combine(sequence)

    def addFavorite(self):
        listOfPhonemes = self.ui.t2s_input.text()
        decoder = Text2Speech()
        listOfPhonemes = decoder.decodeNoMap(listOfPhonemes)
        for phon in listOfPhonemes:
            if phon not in self.user.getFavoritePhoneme():
                self.user.addFavoritePhoneme(phon)
        self.ui.t2s_input.setText('')        
        
def main():
    app = QApplication(sys.argv)
    bufferUser = User("A", "B", "C", "12354", "aA7;aaaa")
    w = IPALabUI(bufferUser)
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

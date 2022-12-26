import sys
from design import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem) # Quando clicar no botão, chama a função abrir_imagem
        self.btnRedimensionar.clicked.connect(self.redimensionar) # Quando clicar no botão, chama a função redimensionar
        self.btnOriginalImg.clicked.connect(self.original) # Quando clicar no botão, chama a função salvar
        self.btnSalvar.clicked.connect(self.salvar_imagem) # Quando clicar no botão, chama a função salvar

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget, #Pai da caixa de diálogo
            'Abrir Imagem', #Titulo da caixa de diálogo
            r'/home/dayan/Imagens/', #Diretório inicial
        )
        self.inputAbrirArquivo.setText(imagem) #Coloca o caminho da imagem no input
        self.original_img = QPixmap(imagem) #Cria um objeto QPixmap com a imagem original
        self.labelImg.setPixmap(self.original_img) #Coloca a imagem original no label
        
        self.inputLargura.setText(str(self.original_img.width())) #Coloca a largura da imagem no input
        self.inputAltura.setText(str(self.original_img.height())) #Coloca a altura da imagem no input

    def redimensionar(self):
        largura = int(self.inputLargura.text()) #Pega a largura digitada no input
        self.nova_imagem = self.original_img.scaledToWidth(largura) #Redimensiona a imagem original para a largura desejada
        
        self.labelImg.setPixmap(self.nova_imagem) #Coloca a imagem redimensionada no label
        self.inputLargura.setText(str(self.nova_imagem.width())) #Coloca a largura da imagem redimensionada no input
        self.inputAltura.setText(str(self.nova_imagem.height())) #Coloca a altura da imagem redimensionada no input

    def original(self):
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def salvar_imagem(self):

        if self.inputAltura.text() == '': # Verifica se alguma imagem foi escolhida antes de salvar
            QMessageBox.information(None, "Erro", 'Nenhuma imagem foi redimensionada')
            return

        #verifica se a imagem escolhida foi redimensionada
        if str(self.original_img.width()) == self.inputLargura.text():
            QMessageBox.information(None, "Aviso", 'A imagem escolhida não teve alteração')
            return

        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget, #Pai da caixa de diálogo
            'Salvar Imagem', #Titulo da caixa de diálogo
            r'/home/dayan/Desktop/', #Diretório inicial
        )

        self.nova_imagem.save(imagem, 'png') # Salvar nova imagem 
        
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
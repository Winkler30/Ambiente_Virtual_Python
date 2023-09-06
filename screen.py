import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton

def exibir_mensagem():
    nome = campo_nome.text()
    mensagem = campo_mensagem.text()

    mensagem_formatada = f"Olá {nome}! Minha mensagem é: {mensagem}"
    mensagem_formatada = mensagem_formatada.replace(' ', '%20')

    url_whatsapp = f"https://wa.me/5543991549529?text={mensagem_formatada}"

    webbrowser.open(url_whatsapp)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    janela = QMainWindow()
    janela.setWindowTitle('Envio de Mensagem via WhatsApp')
    janela.setFixedSize(400, 300)

    conjunto_widget = QWidget()
    v_layout = QVBoxLayout()
    conjunto_widget.setLayout(v_layout)

    label1 = QLabel('Envie uma mensagem para o meu WhatsApp')
    label1.setStyleSheet("font-size: 18px; margin-bottom: 20px; font-weight: bold;")
    v_layout.addWidget(label1)

    form_layout = QFormLayout()

    campo_nome = QLineEdit()
    campo_nome.setPlaceholderText('Digite seu nome')
    campo_nome.setStyleSheet("font-size: 14px; height: 30px;")
    form_layout.addRow('Nome:', campo_nome)

    campo_mensagem = QLineEdit()
    campo_mensagem.setPlaceholderText('Digite sua mensagem')
    campo_mensagem.setStyleSheet("font-size: 14px; height: 30px;")
    form_layout.addRow('Mensagem:', campo_mensagem)

    v_layout.addLayout(form_layout)

    botao_enviar = QPushButton('Enviar Mensagem')
    botao_enviar.setStyleSheet("font-size: 14px; height: 40px; background-color: #55acee; color: white;"
                               "border-radius: 5px;")
    botao_enviar.clicked.connect(exibir_mensagem)
    v_layout.addWidget(botao_enviar)

    janela.setCentralWidget(conjunto_widget)
    janela.setStyleSheet("background-color: #f1f1f1;")

    conjunto_widget.setStyleSheet("""
        QLabel {
            font-size: 18px;
            margin-bottom: 20px;
            font-weight: bold;
            color: #333333;
        }

        QLineEdit {
            font-size: 14px;
            height: 30px;
        }

        QPushButton {
            font-size: 14px;
            height: 40px;
            color: white;
            border-radius: 5px;
        }
    """)

    janela.show()

    sys.exit(app.exec())
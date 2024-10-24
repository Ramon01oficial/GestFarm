from PySide6.QtCore import Qt
from PySide6.QtGui import  QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from ui_login import Ui_login_ui
from ui_main import Ui_MainWindow
from coneccao import conexao
from reportlab.pdfgen import canvas
from datetime import datetime
import sys




class Login(QWidget, Ui_login_ui):
    def __init__(self) -> None:
        super(Login,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')

        self.btn_login.clicked.connect(self.abrirSistema)
    # ************autenticando o usuario **********
    def abrirSistema(self):
        # *********consulta ao banco de dados********
        nome_usuario = self.txt_user.text()
        senha_usuario = self.txtpassword.text()
        cursor = conexao.cursor()
        comandoSql = "SELECT * FROM funcionario WHERE nome = %s AND senha = %s;"
        cursor.execute(comandoSql, (nome_usuario,senha_usuario))

        # *********validação******
        resultado = cursor.fetchone()
        if resultado:
             self.w = MainWindow()
             self.w.show()
             self.close()

        else:
            #  *****mensagem de erro******
             msg= QMessageBox()
             msg.setIcon(QMessageBox.Warning)
             msg.setWindowTitle("Erro no Login")
             msg.setText("Usuário ou Senha estão Incorretos")
             msg.exec_()
             return None

     
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema GestFarm')
        # ****APLICANDO MASCARAS***
        
        self.txt_cpf.setInputMask('000.000.000-00')
        #self.txt_cnpj.setInputMask('00.000.000/0000-00')

        # *********ACESSANDO AS PÁGINAS *********
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.mostrarTabela())
        self.btn_cadastro_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuario))
        self.btn_cadastro_cliente.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_cliente))
        self.btn_cadastro_produto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_produto))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_cliente.clicked.connect(lambda: self.mostrarCliente())
        self.btn_excluir.clicked.connect(lambda: self.excuir_dados())
        self.btn_excluir_cliente.clicked.connect(lambda: self.excuir_cliente())
        self.btn_gerar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_vendas))
        self.btn_realizarvenda.clicked.connect(lambda: self.realizar_venda())
        self.btn_relatorio.clicked.connect(lambda: self.mostrarTabelaProximoVencimento())
        self.btn_buscar.clicked.connect(lambda: self.realizar_pesquisa())
        self.btn_buscar_cliente.clicked.connect(lambda: self.exibir_cliente())
        self.btn_pdf.clicked.connect(lambda: self.pdf())
    #    ***************botão que cadastra o produto no Banco de dados*****
        self.btn_cadastro_produto_no_banco.clicked.connect(lambda:self.funcaocadastroProduto())

    #    ***************botão que cadastra o acesso/usuário/funcionário no Banco de dados*****
        self.btn_cadastrar_usuario_no_banco.clicked.connect(lambda:self.funcaocadastroUsuario())


    #    ***************botão que cadastra o cliente no Banco de dados*****
        self.btn_cadastrar_cliente_no_banco.clicked.connect(lambda:self.funcaocadastroCliente())

        # *********chamada para exibir os produtos na tw_estoque*******

    def mostrarTabela(self):
            self.Pages.setCurrentWidget(self.pg_table)
            self.exibe_estoque()

    def mostrarCliente(self):
            self.Pages.setCurrentWidget(self.pg_cliente)
            self.exibir_cliente()

    def mostrarTabelaProximoVencimento(self):
            self.Pages.setCurrentWidget(self.pg_prox_venc)
            self.exibe_proximosaovencimeto()

    def funcaocadastroProduto(self):
            nomeProd= self.txt_nomeprod.text()
            print('nome prod',nomeProd)

            quantidade= self.txt_quantidade.text()
            print('quantidade:',quantidade)

            dataValidade = self.txt_validade.text()
            try:
                dataValidade_formatada = datetime.strptime(dataValidade, '%d/%m/%Y').strftime('%Y-%m-%d')
                print('Data validade:', dataValidade_formatada)
            except ValueError:
                print('Data em formato inválido')
                return
            preco= self.txt_preco.text()
            print('preco: ',preco)

            cursor = conexao.cursor()
            comandoSql = "call sp_cadastro_produto(%s, %s, %s, %s);"
            dados = (str(nomeProd),str(quantidade),str(dataValidade_formatada),str(preco))
            cursor.execute(comandoSql,dados)
            conexao.commit()
            # ***LIMPANDO OS DADOS DO FORMULÁRIO DE CADASTRO DE PRODUTO*****
            self.txt_nomeprod.setText("")
            self.txt_quantidade.setText("")
            self.txt_validade.setText("")
            self.txt_preco.setText("")

    
           

    def funcaocadastroUsuario(self):
                if self.txt_senha.text() != self.txt_senha2.text():
                     msg= QMessageBox()
                     msg.setIcon(QMessageBox.Warning)
                     msg.setWindowTitle("Senha divergentes")
                     msg.setText("As senhas estão diferentes")
                     msg.exec_()
                     return None
                     
                nomeUsuario= self.txt_nome_usuario.text()
                cpf= self.txt_cpf.text()
                senha = self.txt_senha.text()
                senha2 = self.txt_senha2.text()
                print('Senha: ',senha)
                print('Comfirmação de senha: ',senha2)

                cursor = conexao.cursor()
                comandoSql = "call sp_cadastro_funcionario(%s, %s,%s);"
                dados = (str(nomeUsuario),str(cpf),str(senha))
                cursor.execute(comandoSql,dados)
                conexao.commit()

                # ***MENSAGEM QUANDO O USUARIO É CADASTRADO *****
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Cadastro de Usuário")
                msg.setText("Cadastro realizado com sucesso")
                msg.exec_()

                # ***LIMPANDO OS DADOS DO FORMULÁRIO DE CADASTRO DE USUARIO*****
                self.txt_nome_usuario.setText("")
                self.txt_cpf.setText("")
                self.txt_senha.setText("")
                self.txt_senha2.setText("")

    
    # **********exibe produto na table widget**********
    def exibe_estoque(self):
        cursor = conexao.cursor()
        comandoSql = "select idproduto, nomeProduto, quantidade, DATE_FORMAT(validade, '%d/%m/%Y') AS validade, valorProd from produto;"
        cursor.execute(comandoSql)
        dados_lidos = cursor.fetchall()
        print(dados_lidos[0],[0])

        # **********configurando a exibição do teble widget******
        self.tw_estoque.setRowCount(len(dados_lidos))
        self.tw_estoque.setColumnCount(5)

 # ***PERCORRENDO CADAD LINHA E CADA COLUNA NO BANCO E ATRIBUINDO A CADA CELULA DA TABELA******
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                self.tw_estoque.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))

    
        
        cursor = conexao.cursor()
        comandoSql1 = "SELECT * from view_detalhes_venda;"
        cursor.execute(comandoSql1)
        dados_lidos1 = cursor.fetchall()
        print(dados_lidos1[0],[0])
        # **********configurando a exibição do teble widget******
        self.tw_saida.setRowCount(len(dados_lidos1))
        self.tw_saida.setColumnCount(8)

    # ***PERCORRENDO CADAD LINHA E CADA COLUNA NO BANCO E ATRIBUINDO A CADA CELULA DA TABELA******
        for s in range(0, len(dados_lidos1)):
            for d in range(0, 8):
                self.tw_saida.setItem(s, d, QTableWidgetItem(str(dados_lidos1[s][d])))
    

    # *********consulta no banco para exibir produtos proximos do vencimento*****
    def exibe_proximosaovencimeto(self):
        cursor = conexao.cursor()
        comandoSql = "select idproduto, nomeProduto, quantidade, DATE_FORMAT(validade, '%d/%m/%Y') AS validade, valorProd from produto ORDER BY validade DESC;"
        cursor.execute(comandoSql)
        dados_lidos = cursor.fetchall()
        print(dados_lidos[0],[0])
        # **********configurando a exibição do teble widget******
        self.tw_proximo_vencimento.setRowCount(len(dados_lidos))
        self.tw_proximo_vencimento.setColumnCount(5)


        # ********EXIBINDO A TABELA COM CORES ********
          
        for i in range(len(dados_lidos)):
            cor = QColor(255, 255, 255)

            for j in range(5):
                valor = dados_lidos[i][j]

                if j == 3:
                    try:
                        validade = datetime.strptime(valor, '%d/%m/%Y')  
                        dias_restantes = (validade - datetime.now()).days
                        if dias_restantes < 0:
                            cor = QColor(255, 0, 0)
                        elif dias_restantes <= 7:
                            cor = QColor(0, 0, 255)
                        else:
                            cor = QColor(0, 255, 0) 

                        item = QTableWidgetItem(valor)

                        item.setBackground(cor)

                        self.tw_proximo_vencimento.setItem(i, j, item)

                    except ValueError:
                        self.tw_proximo_vencimento.setItem(i, j, QTableWidgetItem(str(valor)))
                else:
                    item = QTableWidgetItem(str(valor))
                    item.setBackground(cor)
                    self.tw_proximo_vencimento.setItem(i, j, item)
                    

    # *********cadastrar cliente*******
    def funcaocadastroCliente(self):
            nomeCliente= self.txt_nome_cliente.text()
            print('nome prod',nomeCliente)

            cnpj= self.txt_cnpj.text()
            print('cnpj:',cnpj)

            cursor = conexao.cursor()
            comandoSql = "call sp_cadastro_cliente(%s, %s);"
            dados = (str(nomeCliente),str(cnpj))
            cursor.execute(comandoSql,dados)
            conexao.commit()
            # ***LIMPANDO OS DADOS DO FORMULÁRIO DE CADASTRO DE PRODUTO*****
            self.txt_nome_cliente.setText("")
            self.txt_cnpj.setText("")



    # ***************Buscando Produtos*************
    def realizar_pesquisa(self):
        termo_pesquisa = self.txt_buscar_produto.text()

        if not termo_pesquisa:
            print("Digite um termo de pesquisa.")
            return
        
        cursor = conexao.cursor()
        comandoSql = f"SELECT idproduto, nomeProduto, quantidade, DATE_FORMAT(validade, '%d-%m-%Y'), valorProd FROM produto WHERE nomeProduto LIKE '%{termo_pesquisa}%';"
        cursor.execute(comandoSql)
        dados_lidos = cursor.fetchall()

        self.tw_proximo_vencimento.setRowCount(len(dados_lidos))
        self.tw_proximo_vencimento.setColumnCount(5)

        for i in range(len(dados_lidos)):
            cor = QColor(255, 255, 255) 

            for j in range(5):
                valor = dados_lidos[i][j]

                if j == 3:
                    try:
                        validade = datetime.strptime(valor, '%d-%m-%Y')

                        dias_restantes = (validade - datetime.now()).days

                        if dias_restantes < 0:
                            cor = QColor(255, 0, 0)
                        elif dias_restantes <= 7:
                            cor = QColor(0, 0, 255) 
                        else:
                            cor = QColor(0, 255, 0)

                        
                        item = QTableWidgetItem(valor)
                        item.setData(Qt.BackgroundRole, cor)

                        self.tw_proximo_vencimento.setItem(i, j, item)

                    except ValueError:
                        self.tw_proximo_vencimento.setItem(i, j, QTableWidgetItem(str(valor)))
                else:
                    item = QTableWidgetItem(str(valor))
                    item.setData(Qt.BackgroundRole, cor)
                    self.tw_proximo_vencimento.setItem(i, j, item)
    

    def exibir_cliente(self):
        termo_pesquisa = self.txt_buscar_cliente.text()

        
        cursor = conexao.cursor()
        comandoSql = f"SELECT idcliente, nomeCliente, cnpj FROM cliente WHERE nomeCliente LIKE '%{termo_pesquisa}%';"
        cursor.execute(comandoSql)
        dados_lidos = cursor.fetchall()

        self.tw_cliente.setRowCount(len(dados_lidos))
        self.tw_cliente.setColumnCount(3)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 3):
                self.tw_cliente.setItem(i, j, QTableWidgetItem(str(dados_lidos[i][j])))


    #*********excluir produto esta com problema não exclui kkdkdkdkdkdkd******
    def excuir_dados(self):
        linha = self.tw_estoque.currentRow()
        self.tw_estoque.removeRow(linha)

        cursor = conexao.cursor()
        cursor.execute("SELECT idproduto FROM produto")
        dados_lidos =cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM produto WHERE idproduto= "+ str(valor_id))
        conexao.commit()

    def excuir_cliente(self):
        linha = self.tw_cliente.currentRow()
        self.tw_cliente.removeRow(linha)

        cursor = conexao.cursor()
        cursor.execute("SELECT idcliente FROM cliente")
        dados_lidos =cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM cliente WHERE idcliente= "+ str(valor_id))
        conexao.commit()

# ***********PDF********
    def pdf(self):
        cursor = conexao.cursor()
        comandoSql = "SELECT * FROM produtosmaioresquantidades"
        cursor.execute(comandoSql)
        dados_lidos = cursor.fetchall()
        y = 0

        pdf = canvas.Canvas("produtos.pdf")
        pdf.setFont("Times-Bold", 25)

        pdf.drawString(200, 800, "Produtos cadastrados:")
        pdf.setFont("Times-Bold", 18)

        pdf.drawString(10, 750, "Código")
        pdf.drawString(108, 750, "Nome")
        pdf.drawString(210, 750, "Quantidade")
        pdf.drawString(310, 750, "Validade")
        pdf.drawString(410, 750, "Preço")

        y = 0
        for i in range(0, len(dados_lidos)):
            y = y + 25 
            pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
            pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
            pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
            pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
            pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

        pdf.save()
        print("PDF GERADO COM SUCESSO")
        self.btn_pdf.clicked.connect(lambda: self.pdf())
    


# *********** VENDA***********
    def realizar_venda(self):
        try:
            
            codprod = int(self.txt_codprod.text())
            quantidade_vendida = int(self.txt_quantidade_2.text())
            codclient = int(self.txt_codcliente.text())
            
            
            if not codprod or not quantidade_vendida or not codclient:
                raise ValueError("Todos os campos devem ser preenchidos.")

            comando_sql = f"SELECT nomeProduto, quantidade, validade, valorProd FROM produto WHERE idproduto = {codprod};"
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            produto = cursor.fetchone()
            cursor.close()

            if not produto:
                raise ValueError(f"Produto com ID {codprod} não encontrado.")

            nome_produto, quantidade_estoque, validade, valor_produto = produto

            
            if quantidade_vendida > quantidade_estoque:
                raise ValueError(f"Quantidade insuficiente em estoque. Disponível: {quantidade_estoque}")

            
            comando_sql = f"SELECT nomeCliente FROM cliente WHERE idcliente = {codclient};"
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            cliente = cursor.fetchone()
            cursor.close()

            if not cliente:
                raise ValueError(f"Cliente com ID {codclient} não encontrado.")

            nome_cliente = cliente[0]

            
            preco_total = quantidade_vendida * valor_produto

            nova_quantidade = quantidade_estoque - quantidade_vendida
            comando_atualizar_estoque = f"UPDATE produto SET quantidade = {nova_quantidade} WHERE idproduto = {codprod};"
            cursor = conexao.cursor()
            cursor.execute(comando_atualizar_estoque)
            conexao.commit()

            
            data_venda = datetime.now().strftime('%Y-%m-%d')
            comando_inserir_venda = (
                "INSERT INTO vendas (dataVenda, idCliente, idProduto, valortotal, quantidade) "
                "VALUES (%s, %s, %s, %s, %s);"
            )
            
            valores_venda = (data_venda, codclient, codprod, preco_total, quantidade_vendida)
            cursor.execute(comando_inserir_venda, valores_venda)
            conexao.commit()
            cursor.close()

            QMessageBox.information(self, "Venda", f"Venda realizada com sucesso! Preço total: R${preco_total:.2f}")

        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Login()
    window.show()
    app.exec_()
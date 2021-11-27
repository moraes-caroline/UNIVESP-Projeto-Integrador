import pyodbc, csv

# from app import getName

# Nome = getName()
Senha = ''
#Seleciona o nome do usuário

# try:
#     con = pyodbc.connect(r"DRIVER={SQL Server};server=projeto-integrador-univesp.database.windows.net;database=projeto-integrador;uid=Caroline;pwd=Mniebsuv21")
#     cur = con.cursor()
#     # cur.execute("EXEC SELECT_loginUser '" + str(Nome) + "', '" + str(Email) +  "', '" + str(Senha) + "'")
#     Nome = cur.execute("EXEC SELECT_loginUser '" + str(Nome) + "'")

#     dbData = cur.fetchall()
#     Nome = dbData[0][0]
#     cur.close()
#     con.close()

#     print(Nome)
# except Exception as e:
#     print('Error DB_loginUser:', e)

class Select():
    #Seleciona a senha do usuário
    def DB_SELECT_loginPassword(Nome, Senha):

        # Nome = DB_SELECT_loginUser(Nome)
        try:
            con = pyodbc.connect(r"DRIVER={SQL Server};server=projeto-integrador-univesp.database.windows.net;database=projeto-integrador;uid=Caroline;pwd=Mniebsuv21")
            cur = con.cursor()
            # cur.execute("EXEC SELECT_loginUser '" + str(Nome) + "', '" + str(Email) +  "', '" + str(Senha) + "'")
            cur.execute("EXEC SELECT_loginPassword '" + str(Nome) + "'")

            dbData = cur.fetchall()
            plainPassword = dbData[0][0]
            cur.close()
            con.close()

            print(Senha)
        except Exception as e:
            print('Error DB_loginUser:', e)

def DB_INSERT_data(Qualitor, Tipo, Quantidade, Filial, Solicitante, Status, Observacao):
    try: 
        con = pyodbc.connect(r"DRIVER={SQL Server};server=projeto-integrador-univesp.database.windows.net;database=projeto-integrador;uid=Caroline;pwd=Mniebsuv21")
        con.autocommit = True
        cur = con.cursor()
        
        # cur.execute("exec sp_InsertWorkTickets '" + str(WO.strip()) + "', '" + str(UPN_Add.strip())  +"', '"+ str(NetworkId.strip())  +"', '"+ str(RequestedFor.strip()) +"', '"+ str(RequestedBy.strip()) +"', '"+ str(UserPrincipalName.strip()) + "', '" + str(UPN_Remove.strip()) + "', '" + str(TargetAddress.strip()) + "', '" + str(SubmitDate.strip()) + "', '" + str(Status.strip()) + "', '"  + str(TicketType.strip()) + "' , '" + str(State.strip()) + "' , '" + str(summary.strip()) + "' , '" + str(Country.strip()) + "','" + Action +"'")
        cur.execute("exec INSERT_data '" + str(Qualitor) + "', '" + str(Tipo)  +"', '"+ str(Quantidade)  +"', '"+ str(Filial) +"', '"+ str(Solicitante) +"', '"+ str(Status) + "', '" + str(Observacao)  +"'")


        # row = cur.fetchone()

        cur.close()
        con.close()
        exit
    except Exception as e:
        print (e)

def read_csv():
    
    with open(r'C:\Projetos\PI\csv\SolicitaçãodeComprasTI.csv' , encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    
        for row in csv_reader:
            try: 

                Qualitor = row[1]
                Tipo = row[2]
                Quantidade = row[3]
                Filial = row[7]
                Solicitante = row[9]
                Status = row[14]
                Observacao = row[15]

                if Qualitor == "QLT":
                    continue

                DB_INSERT_data(Qualitor, Tipo, Quantidade, Filial, Solicitante, Status, Observacao)
            except Exception as e:
                print(e)

read_csv()
# DB_SELECT_loginUser(Nome)
# DB_SELECT_loginPassword(Nome, Senha)

# def getLogin(Nome, Email, Senha):

#     DB_loginUser(Nome, Email, Senha)
#     print (Nome, Email, Senha)

# getLogin()
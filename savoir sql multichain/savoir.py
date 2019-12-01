from Savoir import Savoir
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

class MultichainCommitter(Savoir):
    line = "global"
    def __init__(self, rpcuser, rpcpasswd, rpchost, rpcport, chainname):
        self.rpcuser = rpcuser
        self.rpcpasswd = rpcpasswd
        self.rpchost = rpchost
        self.rpcport = rpcport
        self.chainname = chainname
        try:
            super().__init__(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
            self.getinfo()
        except Exception as ex:
            print(ex)

    def commit(self, key, data, stream="root"):
        return self.publish(stream, key, str(data).encode().hex())

    def run_cmd_input(self):
        try:
            while True:
                line = input("Input data")
                #start sql insert
                mycursor = mydb.cursor()
                sql = "INSERT INTO data (input) VALUES (%s)"
                val = (line,)
                mycursor.execute(sql, val)
                mydb.commit()
                #end dql insert
                print(mycursor.rowcount, "record inserted.")
                print(self.commit('cmd_line_input_py', line))
        except KeyboardInterrupt:
            print('shutting down.')

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="test"
    )



    bc = MultichainCommitter('multichainrpc', '2b47bbv4JmHy3e63tRRyAC5ARWRiKPeif5SEa3RJZtDh', '127.0.0.1', '9540', 'chain1')
    print(bc.getinfo())

    bc.run_cmd_input()




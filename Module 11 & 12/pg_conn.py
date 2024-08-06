from config import load_config
import psycopg2
import psycopg2.extras
import logging


logging.basicConfig(filename="application.log",filemode='a',level=logging.DEBUG,
					format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()


class PGConnect:
    
    def __init__(self):
        self.__connection = None


    @property
    def db_connection(self):
        # if connection is not alive, then create a new one.
        if not (self.__connection is not None and self.__connection.closed == 0):
            self.__connection = PGConnect.get_db_connection()
        return self.__connection
    

    def read(self, query=''):
        """
        Execute query string as query statement
        :param query: query statement in string
        :return: list of tuple
        """
        data = []
        log.debug('Fetching data : ' + query)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
        except Exception as error:
            log.error("Error happened at fetching data - " + str(error).capitalize())

        return data

    def close(self):
        self.__connection.close()
        log.debug("Database connection is closed.")
             

    def write(self, query=''):
        """
        Execute query string as query statement
        :param query: query statement in string
        :return: list of tuple
        """

        log.debug('Writing data : ' + query)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            cursor.close()
            return True
        except Exception as error:
            log.error("Error happened at writting data - " + str(error).capitalize())

        return False

    @staticmethod
    def get_db_connection():
        """
        Initialize DB env variables for connection
        :return:
        """
        log.debug('initializing db...')

        config = load_config()
        pg_connection = psycopg2.connect(**config)
        pg_connection.set_session(autocommit=True)
        log.debug(pg_connection)

        return pg_connection



def main():

    db = PGConnect()
    db.get_db_connection()
    sql = "INSERT INTO user_app (name, last_name, email) values ('Susan', 'Smith', 'ssmith@gmail.com')"
    db.write(sql)

    sql = "SELECT id, name, last_name, email FROM user_app"    
    data = db.read(sql)

    header = ('id','name', 'last_name', 'email') 
    for row in data:
        print(dict(zip(header, row)))

    db.close()


if __name__ == '__main__':
    main()
    

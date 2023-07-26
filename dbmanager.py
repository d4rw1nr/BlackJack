import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql

class DBManager:
    def __init__(self) -> None:
        load_dotenv() # take environment variables from .env.
        self.connection = None
        self._games = {'start_time':None,
                        'end_time':None,
                        'bot':None,
                        'initial_balance':None,
                        'final_balance':None}
        self._rounds = {'game_id':None,
                        'round_number':None,
                        'p_initial_cards':None,
                        'c_initial_cards':None,
                        'p_final_cards':None,
                        'c_final_cards':None,
                        'initial_balance':None,
                        'final_balance':None,
                        'initial_bet':None,
                        'final_bet':None,
                        'outcome':None}
        self._moves = {'round_id':None,
                        'move_number':None,
                        'move':None,
                        'p_cards':None,
                        'c_cards':None,
                        'bet':None}
        self._game_id = 0
        self._round_id = 0

    # GETTERS AND SETTERS
    @property
    def games(self):
        return self._games
    
    @games.setter
    def games(self, attributes):
        if isinstance(attributes, dict):
            for key, value in attributes:
                if key in self._games:
                    self._games[key] = value
                else:
                    raise ValueError(f"{key} isn't a valid key for 'games")
        else:
            raise ValueError("Attributes must be in a dictionary")

    @property
    def rounds(self):
        return self._rounds
    
    @rounds.setter
    def rounds(self, attributes):
        if isinstance(attributes, dict):
            for key, value in attributes:
                if key in self._rounds:
                    self._rounds[key] = value
                else:
                    raise ValueError(f"{key} isn't a valid key for 'rounds")
        else:
            raise ValueError("Attributes must be in a dictionary")

    @property
    def moves(self):
        return self._moves
    
    @moves.setter
    def moves(self, attributes):
        if isinstance(attributes, dict):
            for key, value in attributes:
                if key in self._moves:
                    self._moves[key] = value
                else:
                    raise ValueError(f"{key} isn't a valid key for 'moves")
        else:
            raise ValueError("Attributes must be in a dictionary")

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, id):
        if isinstance(id, int):
            self._game_id = id
        else:
            raise ValueError("id must be a integer")

    @property
    def round_id(self):
        return self._round_id
    
    @round_id.setter
    def round_id(self, id):
        if isinstance(id, int):
            self._round_id = id
        else:
            raise ValueError("id must be a integer")

    # CONNECT AND DISCONNECT THE CONNECTION TO THE DB
    def connect(self):
        try:
        # Establecer conexión con la base de datos
            self.connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            print("Conexion Exitosa")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
    
    # PUSH THE DATA TO THE DB
    # Inserts for games table
    def insert_games(self): # First part of insert in the games table
        if self.connection is None: #Cheking if the connection is active
            self.connect()
        
        try: # Inserting the data in the table games
            cursor = self.connection.cursor()
            insert = sql.SQL("INSERT INTO games ({}) VALUES ({}) RETURNING game_id").format(
                sql.SQL(', ').join(map(sql.Identifier, self.games.keys())),
                sql.SQL(', ').join(map(sql.Placeholder, self.games.keys()))
            )
            cursor.execute(insert, self.games)
            game_id = cursor.fetchone()[0] # return the game_id
            return game_id
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
    

    def insert_games_final(self, game_id:int): # Second part of insert in the games table
        if self.connection is None: #Cheking if the connection is active
            self.connect()

        try: # Inserting end_time and final_balance in the games table
            cursor = self.connection.cursor()
            insert = """
            UPDATE games 
            SET end_time = %s, final_balance = %s
            WHERE game_id = %s
            """
            values = (self.games['end_time'], self.games['final_balance'], game_id)
            cursor.execute(insert, values)
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    # Inserts for rounds table
    def insert_rounds(self, game_id): # First part of insert in the rounds table
        if self.connection is None: #Cheking if the connection is active
            self.connect()

        try:
            cursor = self.connection.cursor()
            insert = sql.SQL("INSERT INTO rounds ({}) VALUES ({}) RETURNING round_id").format(
                sql.SQL(', ').join(map(sql.Identifier, self.rounds.keys())),
                sql.SQL(', ').join(map(sql.Placeholder, self.rounds.keys()))
            )
            cursor.execute(insert, self.rounds)
            round_id = cursor.fetchone()[0] # return the game_id
            return round_id
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
    
    def insert_rounds_final(self, round_id):
        if self.connection is None: #Cheking if the connection is active
            self.connect()
        
        try: # Inserting end_time and final_balance in the games table
            cursor = self.connection.cursor()
            insert = """
            UPDATE rounds 
            SET p_final_cards = %s, c_final_cards = %s, final_balance = %s, final_bet = %s, outcome = %s
            WHERE round_id = %s
            """
            values = (self.rounds['p_final_cards'], self.rounds['c_final_cards'],
                    self.rounds['final_balance'], self.rounds['final_bet'], 
                    self.rounds['outcome'], round_id)
            cursor.execute(insert, values)
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

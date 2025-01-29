# Práctica: Juego de Guerra Naval
# El jugador debe tener la capacidad de registrar 3 tipos de barcos en el tablero tanto vertical como horizontal
# El jugador debe tener la capacidad de disparar a las coordenadas del tablero
# Los tipos de barcos son los siguientes: Submarino(3 espacios), Destructor(4 espacios), Portaaviones(5 espacios)
# El juego debe tener un sistema de puntaje y un sistema de vidas
# El juego debe tener un sistema de turnos
# El juego debe tener un sistema de mensajes de error
# El juego debe tener un sistema de mensajes de victoria
# El juego debe tener un sistema de mensajes de derrota
# El juego debe tener un sistema de mensajes de disparo acertado
# El juego debe tener un sistema de mensajes de disparo fallido
# El juego debe tener un sistema de mensajes de barco hundido
# El juego debe tener un sistema de mensajes de barco tocado
# El juego debe tener un sistema de juego para un solo jugador contra la máquina
# El juego debe tener un sistema de juego para dos jugadores
# El tablero debe tener un tamaño de 15x15

import random

class Ship:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.hits = 0

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(15)] for _ in range(15)]
        self.ships = []

    def place_ship(self, ship, x, y, horizontal):
        # Check boundaries
        if horizontal and x + ship.size > 15:
            return False
        if not horizontal and y + ship.size > 15:
            return False

        # Check overlap
        for i in range(ship.size):
            check_x = x + (i if horizontal else 0)
            check_y = y + (0 if horizontal else i)
            if self.board[check_y][check_x] != " ":
                return False

        # Place ship
        for i in range(ship.size):
            place_x = x + (i if horizontal else 0)
            place_y = y + (0 if horizontal else i)
            self.board[place_y][place_x] = "O"
        self.ships.append(ship)
        return True

    def fire(self, x, y):
        if self.board[y][x] == "X" or self.board[y][x] == "•":
            return "ALREADY_SHOT", None
        elif self.board[y][x] == "O":
            self.board[y][x] = "X"
            for ship in self.ships:
                ship.hits += 1
                if ship.hits == ship.size:
                    return "SUNK", ship.name
            return "HIT", None
        else:
            self.board[y][x] = "•"
            return "MISS", None

    def print_board(self):
        print("   " + " ".join(str(i) for i in range(10)) + " " + " ".join(str(i) for i in range(10, 15)))
        for i, row in enumerate(self.board):
            print(f"{i:2d} {' '.join(row)}")

class Game:
    def __init__(self):
        self.player1_board = Board()
        self.player2_board = Board()
        self.ships = [
            Ship(3, "Submarine"),
            Ship(4, "Destroyer"),
            Ship(5, "Aircraft Carrier")
        ]
        self.shots = 50
        self.player1_score = 0
        self.player2_score = 0
        self.vs_computer = True

    def setup_game(self):
        # Elegir modo de juego
        mode = input("Select game mode (1 for vs Computer, 2 for vs Player): ")
        self.vs_computer = mode != "2"

        # Configurar jugador 1
        print("\nPlayer 1, place your ships!")
        self._setup_player_ships(self.player1_board)

        if self.vs_computer:
            self._setup_computer_ships()
        else:
            print("\nPlayer 2, place your ships!")
            self._setup_player_ships(self.player2_board)

    def _setup_player_ships(self, board):
        for ship in self.ships:
            board.print_board()
            placed = False
            while not placed:
                print(f"\nPlacing {ship.name} (size: {ship.size})")
                try:
                    x = int(input("Enter X coordinate: "))
                    y = int(input("Enter Y coordinate: "))
                    direction = input("Enter direction (h for horizontal, v for vertical): ").lower()
                    horizontal = direction == 'h'
                    placed = board.place_ship(Ship(ship.size, ship.name), x, y, horizontal)
                    if not placed:
                        print("Invalid position! Try again.")
                except ValueError:
                    print("Please enter valid numbers!")

    def _setup_computer_ships(self):
        for ship in self.ships:
            placed = False
            while not placed:
                x = random.randint(0, 14)
                y = random.randint(0, 14)
                horizontal = random.choice([True, False])
                placed = self.player2_board.place_ship(Ship(ship.size, ship.name), x, y, horizontal)

    def computer_turn(self):
        while True:
            x = random.randint(0, 14)
            y = random.randint(0, 14)
            result, ship_name = self.player1_board.fire(x, y)
            if result != "ALREADY_SHOT":
                if result == "HIT":
                    self.player2_score += 10
                    return f"Computer hits at ({x},{y})! +10 points"
                elif result == "SUNK":
                    self.player2_score += 50
                    return f"Computer sunk your {ship_name} at ({x},{y})! +50 points"
                else:
                    return f"Computer misses at ({x},{y})!"

    def play_turn(self, x, y, is_player1):
        if self.shots <= 0:
            return "Game Over! Out of shots!"

        target_board = self.player2_board if is_player1 else self.player1_board
        result, ship_name = target_board.fire(x, y)
        self.shots -= 1

        if is_player1:
            if result == "HIT":
                self.player1_score += 10
                return "Player 1 Hit! +10 points"
            elif result == "SUNK":
                self.player1_score += 50
                return f"Player 1 sunk the {ship_name}! +50 points"
        else:
            if result == "HIT":
                self.player2_score += 10
                return "Player 2 Hit! +10 points"
            elif result == "SUNK":
                self.player2_score += 50
                return f"Player 2 sunk the {ship_name}! +50 points"

        return "Miss!" if result == "MISS" else "Already shot there!"

    def print_boards(self, is_player1=True):
        if self.vs_computer:
            print("\nYour Board:")
            self.player1_board.print_board()
            print("\nComputer's Board:")
            self._print_opponent_board(self.player2_board.board)
        else:
            if is_player1:
                print("\nPlayer 1's Board:")
                self.player1_board.print_board()
                print("\nPlayer 2's Board:")
                self._print_opponent_board(self.player2_board.board)
            else:
                print("\nPlayer 2's Board:")
                self.player2_board.print_board()
                print("\nPlayer 1's Board:")
                self._print_opponent_board(self.player1_board.board)

    def _print_opponent_board(self, board):
        # Mostrar el tablero del oponente ocultando los barcos no golpeados
        print("   " + " ".join(str(i) for i in range(10)) + " " + " ".join(str(i) for i in range(10, 15)))
        for i, row in enumerate(board):
            print(f"{i:2d} {' '.join(['O' if cell == 'X' else '•' if cell == '•' else ' ' for cell in row])}")

    def is_game_over(self):
        if self.shots <= 0:
            return True
        return (all(ship.hits == ship.size for ship in self.player1_board.ships) or 
                all(ship.hits == ship.size for ship in self.player2_board.ships))

    def get_final_score(self):
        if self.vs_computer:
            winner = "Player" if self.player1_score > self.player2_score else "Computer"
            return f"Game Over!\nPlayer score: {self.player1_score}\nComputer score: {self.player2_score}\nWinner: {winner}!"
        else:
            winner = "Player 1" if self.player1_score > self.player2_score else "Player 2"
            return f"Game Over!\nPlayer 1 score: {self.player1_score}\nPlayer 2 score: {self.player2_score}\nWinner: {winner}!"

# Bucle principal del juego
game = Game()
game.setup_game()
player1_turn = True

while not game.is_game_over():
    if game.vs_computer:
        game.print_boards()
        try:
            x = int(input("Enter X coordinate to shoot: "))
            y = int(input("Enter Y coordinate to shoot: "))
            if 0 <= x < 15 and 0 <= y < 15:
                print(game.play_turn(x, y, True))
                print("\nComputer's turn:")
                print(game.computer_turn())
            else:
                print("Coordinates must be between 0 and 14!")
        except ValueError:
            print("Please enter valid numbers!")
    else:
        current_player = "Player 1" if player1_turn else "Player 2"
        game.print_boards(player1_turn)
        print(f"\n{current_player}'s turn")
        try:
            x = int(input("Enter X coordinate to shoot: "))
            y = int(input("Enter Y coordinate to shoot: "))
            if 0 <= x < 15 and 0 <= y < 15:
                print(game.play_turn(x, y, player1_turn))
                player1_turn = not player1_turn
            else:
                print("Coordinates must be between 0 and 14!")
        except ValueError:
            print("Please enter valid numbers!")

print(game.get_final_score())

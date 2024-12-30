from logik import Logik
from players.player import Player
from players.auto_player import AutoPlayer
from printer import ConsolePrinter
from reader import ConsoleReader
from time import time

def load_game_parameters(reader, printer):
    printer.print_line()
    printer.print_highlighted(r"""
  _                 _ _    
 | |               (_) |   
 | |     ___   __ _ _| | __
 | |    / _ \ / _` | | |/ /
 | |___| (_) | (_| | |   < 
 |______\___/ \__, |_|_|\_\
               __/ |       
              |___/        
""")
    printer.print_line()
    printer.print("Zadej počet pozic (N): (default 5)")
    positions_count = reader.read_number_with_default_value(5, min_value=1, max_value=20)
    printer.print("Zadej počet barev (M): (default 8)")
    colors_count = reader.read_number_with_default_value(8, min_value=2, max_value=20)
    printer.print("Hraješ jako hádající (1) nebo vybíráš barvy (2): (default 1)")
    player_type = reader.read_number_with_default_value(1, min_value=1, max_value=2)
    printer.print_line()
    printer.print(f"Počet barev: {colors_count}, Počet pozic: {positions_count}")
    printer.print("Hraješ jako hádající" if player_type == 1 else "Hraješ jako vybírající")
    printer.print_line()
    return positions_count, colors_count, player_type

def main():
    printer = ConsolePrinter()
    reader = ConsoleReader(printer)

    positions_count, colors_count, player_type = load_game_parameters(reader, printer)

    logik = None
    player = None
    if player_type == 1:
        player = Player()
        logik = Logik(player, colors_count, positions_count, debug=False)
    else:
        printer.print(f"Zadej tajnou kombinaci s {positions_count} pozicemi oddělenými mezerou: (platné hodnoty 1-{colors_count})")
        secret = reader.read_combination(positions_count, colors_count)
        logik = Logik(AutoPlayer(positions_count, colors_count), colors_count, positions_count, secret)

    game_start = time()
    while not logik.win:
        if player_type == 1:
            printer.print_line()
            printer.print_game(logik.history)
            printer.print_line()
            printer.print(f"Zadej kombinaci s {positions_count} pozicemi oddělenými mezerou: (platné hodnoty 1-{colors_count})")
            player.set_next_combination(reader.read_combination(positions_count, colors_count))
        logik.next_turn()

    printer.print_line()
    printer.print_game(logik.history)
    printer.print_line()
    printer.print_line()
    printer.print("Vyhrál jsi!" if player_type == 1 else "Počítač uhodl tvou kombinaci")
    printer.print(f"Tajná kombinace byla: {" ".join([str(i) for i in logik.secret])}")
    printer.print(f"Počet pokusů: {len(logik.history)}")
    printer.print(f"Doba hraní: {time() - game_start} s")
    printer.print_line()


if __name__ == '__main__':
    main()
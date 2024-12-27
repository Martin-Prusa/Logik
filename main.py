from logik import Logik
from players.player import Player
from players.auto_player import AutoPlayer
from printer import ConsolePrinter
from reader import ConsoleReader

def load_game_parameters(reader, printer):
    printer.print_line()
    printer.print_highlighted('Hra Logic')
    printer.print_line()
    printer.print("Zadej počet pozic (N): (default 5)")
    positions_count = reader.read_number_with_default_value(5)
    printer.print("Zadej počet barev (M): (default 8)")
    colors_count = reader.read_number_with_default_value(8)
    printer.print("Hraješ jako hádající (1) nebo vybíráš barvy (2): (default 1)")
    player_type = reader.read_number_with_default_value(1)
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
        logik = Logik(player, colors_count, positions_count)
    else:
        printer.print(f"Zadej tajnou kombinaci s {positions_count} pozicemi oddělenými mezerou: (platné hodnoty 1-{colors_count})")
        secret = reader.read_combination(positions_count, colors_count)
        logik = Logik(AutoPlayer(), colors_count, positions_count, secret)


if __name__ == '__main__':
    main()
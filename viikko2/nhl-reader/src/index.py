from rich.table import Table
from rich.console import Console

import requests

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()

    seasons_url = "https://studies.cs.helsinki.fi/nhlstats/"
    data = requests.get(seasons_url).text
    seasons = data.split("\n")[3][38:99]
    print(seasons)

    console.print("[italic]NHL statistics by season")

    console.print(f"Select season from: [bold cyan][{seasons}]", end="")
    season = input()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationalities = ", ".join(stats.get_nationalities())
        console.print(
            f"Select nationality from: [bold cyan][{nationalities}]", end="")
        nationality = input("")

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")

        table.add_column(header="name", justify="left", style="cyan")
        table.add_column(header="team", justify="center", style="magenta")

        headers = ["goals", "assists", "points"]
        for header in headers:
            table.add_column(header=header, justify="center", style="magenta")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals),
                          str(player.assists), str(player.assists+player.goals))

        console.print(table)


if __name__ == "__main__":
    main()

from typing import Optional

import typer

from src.controller.coins import CoinController
from src.utils.date import validate_format_input_date

app = typer.Typer()


@app.command()
def get_coins(
    id_coin: str,
    start_date: Optional[str] = typer.Option(None),
    end_date: Optional[str] = typer.Option(None),
    to_db: bool = typer.Option(False, "--to-db")
):

    if not validate_format_input_date(start_date):
        exit(1)

    controller = CoinController(id_coin, start_date, to_db)

    if end_date:
        res = controller.get_coins(end_date)
        controller.persist_coins(res)
    else:
        res = controller.get_coin()
        controller.persist_coin(res)


if __name__ == "__main__":
    app()

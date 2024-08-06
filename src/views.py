import json
import logging

from src.utils import (fetch_and_show_currency_rates, get_greeting,
                       get_xlsx_data_dict, show_cards, show_top_5_transactions, get_time_data)

logger = logging.getLogger("main_page.log")
file_handler = logging.FileHandler("main_page.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def main_page(date: str) -> str:
    """Записывает информацию для главной страницы в файл json"""
    logger.info("Start")
    logger.info("Converting Excel file to list of dictionaries")
    transactions = get_xlsx_data_dict("../data/operations.xlsx")
    logger.info("Getting greeting")
    greeting = get_greeting(get_time_data)
    logger.info("Getting card info")
    cards = show_cards(date, transactions)
    logger.info("Getting top transactions")
    top_transcations = show_top_5_transactions(date, transactions)
    logger.info("Getting currency_rates")
    currency_rates = fetch_and_show_currency_rates()
    logger.info("Creating dictionary of dictionaries")
    main_dict = {"greeting": greeting, "cards": cards, "top_transcations": top_transcations,
                 "currency_rates": currency_rates}  # "stock_prices": stock_prices
    logger.info("Writing info into json-file")
    main_dict_jsons = json.dumps(main_dict)
    logger.info("Stop")
    return main_dict_jsons

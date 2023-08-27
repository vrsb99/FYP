import numpy as np
import pandas as pd
import psycopg2
from typing import List, Tuple


def get_optimal_weights(
    _connection: psycopg2.extensions.connection, run_id: int
) -> np.ndarray:
    cursor = _connection.cursor()
    query = "SELECT weight FROM optimal_weights WHERE run_id=%s"
    cursor.execute(query, [run_id])
    row = cursor.fetchone()
    cursor.close()
    if row:
        return np.array(list(map(float, row[0].split(","))))
    return np.array([])


def get_ticker_data(
    _connection: psycopg2.extensions.connection, run_id: int
) -> List[str]:
    cursor = _connection.cursor()
    query = "SELECT tickers FROM ticker_run WHERE id=%s"
    cursor.execute(query, [run_id])
    row = cursor.fetchone()
    cursor.close()
    return row[0].split(",") if row else []


def filter_tickers(
    tickers: List[str], weights: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame({"Ticker": tickers, "Weight": weights})
    df = df[df["Weight"] > 0]
    return df["Ticker"].to_numpy(), df["Weight"].to_numpy()

#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# basic data munging, taking the raw csv files from OpenData

def get_pct_counts(year):
    print(year)
    df = pd.read_csv(f"/data/raw/{year}.csv", encoding="cp1252")
    return df.groupby(["year", "pct", "race"])["ser_num"].count()

df = pd.concat(get_pct_counts(y) for y in range(2003, 2017))

pd.DataFrame(df).rename(columns={"ser_num": "count"}).to_csv("precinct_sqf.csv")

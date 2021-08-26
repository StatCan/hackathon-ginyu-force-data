"""
The post-processing script to generate the various ESTMA tables.
"""
import pandas as pd
from os import mkdirs

ESTMA_PATH = "SAMPLE-ESTMA-data.csv"
ALL_PAYMENTS_PATH = "System_All_Payments_DataDump.csv"
OUTFILE="data/estma_gb_3.csv"

mkdirs('data', exists_ok=True)

sample_estma = pd.read_csv(ESTMA_PATH, thousands=",")

component_17 = sample_estma[["entity", "country", "period_start_date", "payment_category", "amount_reported_cad"]]
component_17["count"] = 1

component_17 = component_17.groupby(["entity", "country", "period_start_date", "payment_category"]).agg({
    "count": "count",
    "amount_reported_cad": "sum"
}).reset_index()

component_17.to_csv(OUTFILE)


###############################
### Clean up data locations
###############################

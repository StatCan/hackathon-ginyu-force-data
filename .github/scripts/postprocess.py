"""
The post-processing script to generate the various ESTMA tables.
"""
import pandas as pd
from os import makedirs
from datetime import datetime
import json
import sys

from os.path import exists



ESTMA_PATH = "SAMPLE-ESTMA-data.csv"
ALL_PAYMENTS_PATH = "System_All_Payments_DataDump.csv"
OUTFILE="data/estma_gb_3.csv"

if not exists(ESTMA_PATH):
    sys.exit(0)

#makedirs('data', exist_ok=True)
#
#sample_estma = pd.read_csv(ESTMA_PATH, thousands=",")
#
#component_17 = sample_estma[["entity", "country", "period_start_date", "payment_category", "amount_reported_cad"]]
#component_17["count"] = 1
#
#component_17 = component_17.groupby(["entity", "country", "period_start_date", "payment_category"]).agg({
#    "count": "count",
#    "amount_reported_cad": "sum"
#}).reset_index()
#
#component_17.to_csv(OUTFILE)


###############################
### Clean up data locations
###############################

print("Generating Summary")

today = datetime.today()

df = sample_estma
#df = pd.read_csv(sys.argv[1], thousands=',')

# If we only want one year?
# df = df.loc[df['period_start_date'].str.endswith('19')]

THOUSAND = 1000
MILLION  = THOUSAND * 1000
BILLION  = MILLION  * 1000
TRILLION = BILLION  * 1000

def human_dollar(num: int) -> str:
    if num > TRILLION:
        num = num / TRILLION
        return "{:.1f}T".format(num)
    elif num > BILLION:
        num = num / BILLION
        return "{:.1f}B".format(num)
    elif num > MILLION:
        num = num / MILLION
        return "{:.1f}M".format(num)
    else:
        return str(num)

d = {
    'date' : today.strftime('%Y-%m-%d'),
    'estma_countries' : df['country'].nunique(),
    'estma_dollars': human_dollar(pd.to_numeric(df['amount_reported_cad']).sum()),
    'estma_reports_count': df['estma_id'].nunique(),
    'estma_payees': df['payee_project_name'].nunique()
}

print("Writing summary.jsonfile")
with open('summary.jsonfile','w') as f:
    f.write(json.dumps(d, indent=4))

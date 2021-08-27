#!/bin/python3

import pandas as pd
from datetime import datetime
import json
import sys

today = datetime.today()

df = pd.read_csv(sys.argv[1], thousands=',')

# If we only want one year?
# df = df.loc[df['period_start_date'].str.endswith('19')]

THOUSAND = 1000
MILLION  = THOUSAND * 1000
BILLION  = MILLION  * 1000
TRILLION = MILLION  * 1000

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

with open('summary.json','w') as f:
    f.write(json.dumps(d, indent=4))

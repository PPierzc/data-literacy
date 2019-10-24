"""
A flask parser
@author: Paweł A. Pierzchlewicz
"""

import re
import pandas as pd
from tqdm import tqdm


def load_flask(pathname):
	with open(pathname, 'r') as f:
		df = pd.DataFrame()

		header_rgx = re.compile(r'^# (.*):(.*)$')

		for line in tqdm(f):
			header_row = header_rgx.match(line)

			if header_row:
				key, value = header_row.groups()
				value = value.strip()

				if key == 'data_fields':
					value = value.split(' ')

					df = pd.DataFrame(columns=value, dtype=str)
				continue

			row = list(filter(lambda x: x, line.strip().split(' ')))
			df.loc[len(df)] = row

	return df


if __name__ == '__main__':
	df = load_flask('../../data/co2_hpb_surface-flask_1_ccgg_event.txt')
	print(df)

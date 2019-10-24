"""
An Insitu parser
@author: Paweł A. Pierzchlewicz
"""

import pandas as pd
from tqdm import tqdm


def load_insitu(pathname):
	with open(pathname, 'r') as f:
		header = []
		rows = []

		for line in tqdm(f):
			if '#' in line[0]:
				continue

			splitted = list(filter(lambda x: x, line.strip().split(' ')))
			if not len(header):
				header = splitted
				continue

			rows.append(splitted)

	return pd.DataFrame(rows, columns=header)


if __name__ == '__main__':
	df = load_insitu('../../data/co2_mlo_surface-insitu_1_ccgg_DailyData.txt')
	print(df)

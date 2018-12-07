import numpy as numpy
import pandas as pd 
import math

season_09_10=pd.read_csv('season-0910_csv.csv')
season_10_11=pd.read_csv('season-1011_csv.csv')
season_11_12=pd.read_csv('season-1112_csv.csv')
season_12_13=pd.read_csv('season-1213_csv.csv')
season_13_14=pd.read_csv('season-1314_csv.csv')
season_14_15=pd.read_csv('season-1415_csv.csv')
season_15_16=pd.read_csv('season-1516_csv.csv')
season_16_17=pd.read_csv('season-1617_csv.csv')
season_17_18=pd.read_csv('season-1718_csv.csv')

def update_data(data):
	HTPTN=[]
	ATPTN=[]
	HGSTN=[]
	HGCTN=[]
	AGSTN=[]
	AGCTN=[]

	for i in range(380):
		HT_count=0
		AT_count=0
		value_HTPTN=0.0
		value_ATPTN=0.0
		value_HGSTN=0.0
		value_HGCTN=0.0
		value_AGSTN=0.0
		value_AGCTN=0.0
		for j in range(i):
			print(i,j)
			if(data.iloc[j].HomeTeam==data.iloc[i].HomeTeam):
				HT_count+=1
				if(data.iloc[j].FTR=='H'):
					value_HTPTN=value_HTPTN+3.0
				elif(data.iloc[j].FTR=='D'):
					value_HTPTN=value_HTPTN+1.0
				value_HGSTN=value_HGSTN+data.iloc[j].FTHG
				value_HGCTN=value_HGCTN+data.iloc[j].FTAG
			elif(data.iloc[j].AwayTeam==data.iloc[i].HomeTeam):
				HT_count+=1
				if(data.iloc[j].FTR=='A'):
					value_HTPTN=value_HTPTN+3.0
				elif(data.iloc[j].FTR=='D'):
					value_HTPTN=value_HTPTN+1.0
				value_HGSTN=value_HGSTN+data.iloc[j].FTAG
				value_HGCTN=value_HGCTN+data.iloc[j].FTHG

			if(data.iloc[j].HomeTeam==data.iloc[i].AwayTeam):
				AT_count+=1
				if(data.iloc[j].FTR=='H'):
					value_ATPTN=value_ATPTN+3.0
				elif(data.iloc[j].FTR=='D'):
					value_ATPTN=value_ATPTN+1.0
				value_AGSTN=value_AGSTN+data.iloc[j].FTHG
				value_AGCTN=value_AGCTN+data.iloc[j].FTAG
			elif(data.iloc[j].AwayTeam==data.iloc[i].AwayTeam):
				AT_count+=1
				if(data.iloc[j].FTR=='A'):
					value_ATPTN=value_ATPTN+3.0
				elif(data.iloc[j].FTR=='D'):
					value_ATPTN=value_ATPTN+1.0
				value_AGSTN=value_HGSTN+data.iloc[j].FTAG
				value_AGCTN=value_HGCTN+data.iloc[j].FTHG

		HTPTN.append(value_HTPTN)
		ATPTN.append(value_ATPTN)
		HGSTN.append(value_HGSTN)
		HGCTN.append(value_HGCTN)
		AGSTN.append(value_AGSTN)
		AGCTN.append(value_AGCTN)

	data['HTPTN']=HTPTN
	data['ATPTN']=ATPTN
	data['HGSTN']=HGSTN
	data['HGCTN']=HGCTN
	data['AGSTN']=AGSTN
	data['AGCTN']=AGCTN

	return data


season_09_10=update_data(season_09_10)
season_10_11=update_data(season_10_11)
season_11_12=update_data(season_11_12)
season_12_13=update_data(season_12_13)
season_13_14=update_data(season_13_14)
season_14_15=update_data(season_14_15)
season_15_16=update_data(season_15_16)
season_16_17=update_data(season_16_17)
season_17_18=update_data(season_17_18)

concat_stat=pd.concat([season_09_10,season_10_11,season_11_12,season_12_13,season_13_14,season_14_15,season_15_16,season_16_17,season_17_18],ignore_index=True)

teams = {}
for i in concat_stat.groupby('HomeTeam').mean().T.columns:
	teams[i] = 0
for i in range(3420):
	print(i)
	if (concat_stat.iloc[i].FTR=='H'):
		teams[concat_stat.iloc[i].HomeTeam]+=3
	if (concat_stat.iloc[i].FTR=='D'):
		teams[concat_stat.iloc[i].HomeTeam]+=1
		teams[concat_stat.iloc[i].AwayTeam]+=1
	if (concat_stat.iloc[i].FTR=='A'):
		teams[concat_stat.iloc[i].AwayTeam]+=3
histhome=[]
histaway=[]
for i in range(3420):
	print(i)
	histhome.append(teams[concat_stat.iloc[i].HomeTeam])
	histaway.append(teams[concat_stat.iloc[i].AwayTeam])

concat_stat['histhome']=histhome
concat_stat['histaway']=histaway

concat_stat.to_csv("final_dataset.csv")


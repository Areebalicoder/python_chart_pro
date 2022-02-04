#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:31:26 2022

@author: areebalishivji
"""

import pandas as pd
import plotly.express as px

df = pd.read_csv('data1.csv')
print(df)
fig = px.bar(df, x='country', y='cases')
fig.show()
fig2=px.scatter(df, x='country', y='date', size='cases', color='country')
fig2.show()

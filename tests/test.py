import centroid_lookup as cl
import pandas as pd


df = cl.parse_input_file('test-adm0.csv')
df = cl.lookup(df, ['name_0'])

df = cl.parse_input_file('test-adm0.xlsx')
df = cl.lookup(df, ['name_0'])

df = cl.parse_input_file('test-adm2.csv')
df = cl.lookup(df, ['name_0', 'name_1', 'name_2'])

df = cl.parse_input_file('test-adm2.xlsx')
df = cl.lookup(df, ['name_0', 'name_1', 'name_2'])

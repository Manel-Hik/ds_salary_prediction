import scraper as gs
import pandas as pd
path = "/usr/lib/chromium-browser/chromedriver"
df = gs.get_jobs('data scientist', 'Belgium', 420, False, path, 15)

df.to_csv('Jobs_list.csv')
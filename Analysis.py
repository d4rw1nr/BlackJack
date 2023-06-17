import play

import pandas as pd

games = play.play(50,0)
print(games)

games.to_csv()

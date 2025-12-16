import pandas as pd
import os
from sklearn.model_selection import train_test_split

current_dir = os.path.dirname(__file__)


csv_path = os.path.join(current_dir, '..', 'data', 'raw','ranked_10min.csv')

df = pd.read_csv(csv_path)

print('df cargado')

df = df.drop(columns=['blueTotalExperience','redTotalExperience','blueGoldDiff',
                      'redGoldDiff','blueExperienceDiff','blueCSPerMin','redCSPerMin',
                      'blueEliteMonsters','redEliteMonsters','blueDeaths','redDeaths',
                      'blueFirstBlood','blueTotalJungleMinionsKilled','redTotalJungleMinionsKilled',
                      'redExperienceDiff','redWardsDestroyed','blueWardsDestroyed','gameId',
                      'blueGoldPerMin','redGoldPerMin',"blueWardsPlaced","redWardsPlaced",'blueTotalGold','redTotalGold'])

print('Columnas eliminadas')


df['blueWins'] = df['blueWins'].replace({0: 1, 1: 0})

df = df.rename(columns={'blueWins':'equipo_ganador'})
df = df.rename(columns={'redFirstBlood':'equipo_primera_sangre'})
df = df.rename(columns={'blueKills':'azul_asesinatos'})
df = df.rename(columns={'redKills':'rojo_asesinatos'})
df = df.rename(columns={'blueAssists':'azul_asistencias'})
df = df.rename(columns={'redAssists':'rojo_asistencias'})
df = df.rename(columns={'blueAvgLevel':'azul_nivel_medio'})
df = df.rename(columns={'redAvgLevel':'rojo_nivel_medio'})
df = df.rename(columns={'blueTotalMinionsKilled':'azul_subditos'})
df = df.rename(columns={'redTotalMinionsKilled':'rojo_subditos'})
df = df.rename(columns={'blueTowersDestroyed':'azul_torretas_destruidas'})
df = df.rename(columns={'redTowersDestroyed':'rojo_torretas_destruidas'})
df = df.rename(columns={'blueDragons':'azul_dragones'})
df = df.rename(columns={'redDragons':'rojo_dragones'})
df = df.rename(columns={'blueHeralds':'azul_heraldos'})
df = df.rename(columns={'redHeralds':'rojo_heraldos'})

print('Columnas renombradas')

df["asesinatos_dif"] = df["azul_asesinatos"] - df["rojo_asesinatos"]
df["asistencias_dif"] = df["azul_asistencias"] - df["rojo_asistencias"]
df["nivel_dif"] = df["azul_nivel_medio"] - df["rojo_nivel_medio"]
df["minions_dif"] = df["azul_subditos"] - df["rojo_subditos"]
df["torretas_dif"] = df["azul_torretas_destruidas"] - df["rojo_torretas_destruidas"]
df["dragones_dif"] = df["azul_dragones"] - df["rojo_dragones"]
df["heraldos_dif"] = df["azul_heraldos"] - df["rojo_heraldos"]

df = df.drop(columns=["azul_asesinatos",'rojo_asesinatos',"azul_asistencias",
                       "rojo_asistencias","azul_nivel_medio",
                         "rojo_nivel_medio", "azul_subditos","rojo_subditos","azul_torretas_destruidas",
                         "rojo_torretas_destruidas", "azul_dragones", "rojo_dragones","azul_heraldos","rojo_heraldos"])

train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['equipo_ganador'])

print('df separado')

os.makedirs(os.path.join(current_dir, '..', 'data', 'processed'), exist_ok=True)
os.makedirs(os.path.join(current_dir, '..', 'data', 'train'), exist_ok=True)
os.makedirs(os.path.join(current_dir, '..', 'data', 'test'), exist_ok=True)


df.to_csv(os.path.join(current_dir, '..', 'data', 'processed', 'processed.csv'), index=False)

train.to_csv(os.path.join(current_dir, '..', 'data', 'train', 'train.csv'), index=False)

test.to_csv(os.path.join(current_dir, '..', 'data', 'test', 'test.csv'), index=False)


print("Archivos guardados correctamente.")
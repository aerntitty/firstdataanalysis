import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
    draw_cat_plot()
    draw_heat_map()

# 1
df =pd.read_csv(r'/workspace/boilerplate-medical-data-visualizer/medical_examination.csv')


# 2
df['overweight'] =((df['weight']/(df['height']/100)**2 )>25 ).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'].replace(1,0,inplace=True)
df['gluc'].replace(1,0,inplace=True)

# 4
def draw_cat_plot():
    # 5 cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(df ,id_vars=['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6

    df_cat = df_cat.rename(columns={'variable': 'feature'})  


     # 7
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'feature', 'value'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    

   

      

    # 8
    fig =sns.catplot(x='feature', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    fig.set_axis_labels("variable", "total")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
             & (df['height'] >= df['height'].quantile(0.025))
             & (df['height'] <= df['height'].quantile(0.975))
             & (df['weight'] >= df['weight'].quantile(0.025))
             & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask =np.triu(np.ones_like(corr, dtype=bool))





    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, annot=True, mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig
if '__name__'=='__main__':
    main()
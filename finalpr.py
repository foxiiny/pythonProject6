import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry
import geopandas
import plotly.graph_objs as go
import plotly.express as px

st.set_page_config(
    page_title="KPOP", page_icon="💜", layout="centered"
)
st.title("💜 K-Pop")


def get_data(x):
    return pd.read_csv(x)


""" 

### This is overview page about K-Pop and idols

We used data about 4th generation kpop groups sales:

"""

df = get_data('Kpop 4th gen Sales - Sheet1.csv')
df.head()

df['sales'] = df['sales'].str.replace(',', '').str.strip().astype('int64')

df['date'] = pd.to_datetime(df['date'])

fig, ax = plt.subplots()
sns.lineplot(x=df.date, y=df.sales, hue=df.Artist, ax=ax)
st.pyplot(fig)


@st.experimental_memo(ttl=60 * 60 * 24)
def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="k-Pop sales")
        .mark_line()
        .encode(
            x="date",
            y="sales",
            color="Artist",
            # strokeDash="category",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="date",
            y="sales",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("sales", title="Sales"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()


st.write("You can look on sales of the artist you are interested in:")

col1, col2, col3 = st.columns(3)
with col1:
    art = st.multiselect("Choose an artist (⬇💬)", df['Artist'].unique())
with col2:
    art_dx = st.slider(
        "Horizontal offset", min_value=-30, max_value=30, step=1, value=0
    )
with col3:
    art_dy = st.slider(
        "Vertical offset", min_value=-30, max_value=30, step=1, value=-10
    )

annotation_layer = (
    alt.Chart(df)
    .mark_text(size=15, text='Artist', align="center")
    .encode(
        x="date:T",
        y=alt.Y("y:Q"),
    )
    .interactive()
)


if art != []:
    df = df.loc[df['Artist'].isin(art)]
chart = get_chart(df)

st.altair_chart(chart.interactive(), use_container_width=True)


girl_gr = pd.read_csv('kpop_idols_girl_groups.csv')
boy_gr = pd.read_csv('kpop_idols_boy_groups.csv')
sales = pd.read_csv('Kpop 4th gen Sales - Sheet1.csv')
idols = pd.read_csv('kpop_idols.csv')

""" 

For our project we used several datasets, so we can have a look on them. This is data frame about kpop groups:

"""
all_gr = pd.concat([girl_gr, boy_gr], axis=0, join='outer', ignore_index=False, copy=True)
all_gr

""" 

And this is merged dataframe that consists of the previous ones, so here we have info about the track and sales plus 
info about the group, such as company name, debut date, etc.:

"""
mer = sales.merge(all_gr, how='inner', left_on='Artist', right_on='Name')
mer

""" 

We also have the dataframe about idols:

"""

idols


idols.loc[(idols.Country == 'USA'), 'Country'] = 'United States'


def alpha3code(column):
    code = []
    for country in column:
        try:
            c = pycountry.countries.get(name=country).alpha_3
            code.append(c)
        except:
            code.append('None')
    return code


idols['CODE'] = alpha3code(idols.Country)
idols.loc[(idols.Country == 'South Korea'), 'CODE'] = 'KOR'
idols.loc[(idols.Country == 'Taiwan'), 'CODE'] = 'TWN'
idols


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.columns = ['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']
new = idols.groupby(['CODE']).count()
new = pd.merge(world, new, how='outer', on='CODE')
new['Country'] = new['Country'].fillna(0)
fig, ax = plt.subplots(figsize=(25, 20))
new = new.set_index('CODE')
new['Country']['KOR'] = new['Country']['KOR']/20
new.plot(column='Country', ax=ax, legend=True, cmap='PuRd')
plt.title('Origin of kpop idols', fontsize=25)
st.pyplot(fig)


""" 

Now we can have a look at the size of kpop groups:

"""


#fig, ax = plt.subplots()
#all_gr.plot(subplots=True, figsize=(10, 10), ax=ax, sharex=False, sharey=False)
#st.pyplot(fig)

fig, ax = plt.subplots(figsize=[10,7])
sns.countplot(all_gr['Members'], color=sns.xkcd_rgb['light violet'])
plt.title('Kpop Idols Groups')
st.pyplot(fig)


fig = go.Figure()
fig.add_trace(go.Scatter(x=all_gr['Members'].head(10),y=all_gr['Orig. Memb.'],
                    mode='lines+markers',
                    name='Orig. Memb.'))
fig.update_traces(mode='lines+markers', marker_line_width=2, marker_size=10)
fig.update_layout(autosize=False, width=1000, height=700, legend_orientation="h")
st.plotly_chart(fig, use_container_width=True)

fig = px.pie(all_gr,
             values="Members",
             names="Orig. Memb.",
             template="seaborn")
fig.update_traces(rotation=90, pull=0.05, textinfo="percent+label")
st.plotly_chart(fig, use_container_width=True)



#primaryColor="#e0b5fb"
#backgroundColor="#000000"
#secondaryBackgroundColor="#cc5cf5"
#textColor="#ffffff"
#font="monospace"


import folium
import pandas as pd


url = (
    "https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data"
)
state_geo = f"{url}/counties.geojson"
state_unemployment = "data.csv"
state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[-1.289772712474131, 36.78426333871622], zoom_start=6)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["COUNTY_ CODE", "VOTERS"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)

m.save('kenya_maps.html')
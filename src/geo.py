import geopandas as gpd
import plotly.express as px

# Leia o arquivo shapefile
gdf = gpd.read_file("data/RN_Municipios_2022.shp")

# Reprojetar para um CRS projetado (por exemplo, EPSG:3857)
gdf_projected = gdf.to_crs(epsg=3857)

# Calcular os centróides no CRS projetado
gdf_projected["centroid"] = gdf_projected.geometry.centroid

# Reprojetar os centróides de volta para o CRS original
gdf["centroid"] = gdf_projected["centroid"].to_crs(gdf.crs)

# Extrair latitude e longitude dos centróides no CRS original
gdf["latitude"] = gdf["centroid"].y
gdf["longitude"] = gdf["centroid"].x

# Criar o gráfico scatter_geo
fig = px.scatter_geo(
    gdf,
    lat="latitude",
    lon="longitude",
    hover_name=gdf.NM_MUN,  # Nome para exibição ao passar o mouse
    title="Centroides dos Municípios de RN",
)

# Mostrar o gráfico
fig.show()

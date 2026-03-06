import yaml
import geopandas as gpd
from shapely.geometry import Point
import pyproj
from shapely.ops import transform
import os

# Ayarları yükle
config_path = "../6_repro/configs/config.yaml"
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# Config dosyasından verileri doğru şekilde çekiyoruz
lon = config
lat = config
core_radius_km = config
ext_radius_km = config

core_radius_m = core_radius_km * 1000
ext_radius_m = ext_radius_km * 1000

print(f"Merkez Koordinat: Lon={lon}, Lat={lat}")

# Merkez noktayı oluştur (WGS84)
center_pt = Point(lon, lat)

# Metrik projeksiyon (Azimuthal Equidistant - Mesafe bazlı buffer alabilmek için)
local_azimuthal_crs = f"+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"

# Projeksiyon dönüşüm fonksiyonları
project_to_meters = pyproj.Transformer.from_crs("EPSG:4326", local_azimuthal_crs, always_xy=True).transform
project_to_wgs84 = pyproj.Transformer.from_crs(local_azimuthal_crs, "EPSG:4326", always_xy=True).transform

# Merkezi metreye çevir, buffer (yarıçap) al, tekrar WGS84'e (Enlem/Boylam) çevir
center_pt_m = transform(project_to_meters, center_pt)

core_poly_m = center_pt_m.buffer(core_radius_m, resolution=128)
core_poly_wgs84 = transform(project_to_wgs84, core_poly_m)

ext_poly_m = center_pt_m.buffer(ext_radius_m, resolution=128)
ext_poly_wgs84 = transform(project_to_wgs84, ext_poly_m)

# GeoDataFrame oluştur
gdf = gpd.GeoDataFrame({
    'id':,
    'name':,
    'radius_km':
}, geometry=, crs="EPSG:4326")

output_path = "../0_admin/roi.geojson"
gdf.to_file(output_path, driver="GeoJSON")
print(f"✅ roi.geojson başarıyla oluşturuldu: {os.path.abspath(output_path)}")
import netCDF4
import pandas as pd

fin = netCDF4.Dataset("data/tasmin_day_BCSD_historical_r1i1p1_BNU-ESM_2005.nc", "r")

print fin.variables
print fin.variables["tasmin"].shape

tm = fin.variables["tasmin"]
lat = fin.variables['lat']
lon = fin.variables['lon']

tm_s = tm[0][0:450, 0:1].data.flatten()
tm_s -= 273.15  # Convert kelvin to celsius

lat_s = lat[0:450]
lon_s = [lon[0]] * 450

s = pd.DataFrame({
    'minTemperature': tm_s,
    'latitude': lat_s,
    'longitude': lon_s
})

print s
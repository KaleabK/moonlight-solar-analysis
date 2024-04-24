# Solar Radiation Measurement Data

This directory contains the solar radiation measurement data used for this week's challenge. The data is extracted and aggregated from [Solar Radiation Measurement Data](https://energydata.info/dataset/?q=Solar+Radiation+Measurement&vocab_regions=AFR).

## Data Description

Each row in the data represents a single observation and contains the following values:

- **Timestamp (_yyyy-mm-dd hh:mm_):** Date and time of the observation.
- **GHI (_W/m²_):** Global Horizontal Irradiance - total solar radiation received per square meter on a horizontal surface.
- **DNI (_W/m²_):** Direct Normal Irradiance - amount of solar radiation received per square meter on a surface perpendicular to the sun's rays.
- **DHI (_W/m²_):** Diffuse Horizontal Irradiance - solar radiation received per square meter on a horizontal surface that does not arrive on a direct path from the sun.
- **ModA (_W/m²_):** Measurements from Module/Sensor A (similar to irradiance).
- **ModB (_W/m²_):** Measurements from Module/Sensor B (similar to irradiance).
- **Tamb (_°C_):** Ambient Temperature in degrees Celsius.
- **RH (_%_):** Relative Humidity - percentage of moisture in the air.
- **WS (_m/s_):** Wind Speed in meters per second.
- **WSgust (_m/s_):** Maximum Wind Gust Speed in meters per second.
- **WSstdev (_m/s_):** Standard Deviation of Wind Speed - indicates variability.
- **WD (_°N (to east)_):** Wind Direction in degrees from north.
- **WDstdev:** Standard Deviation of Wind Direction - shows directional variability.
- **BP (_hPa_):** Barometric Pressure in hectopascals.
- **Cleaning (_1 or 0_):** Indicates whether cleaning (possibly of the modules or sensors) occurred.
- **Precipitation (_mm/min_):** Precipitation rate measured in millimeters per minute.
- **TModA (_°C_):** Temperature of Module A in degrees Celsius.
- **TModB (_°C_):** Temperature of Module B in degrees Celsius.
- **Comments:** This column may contain additional notes.

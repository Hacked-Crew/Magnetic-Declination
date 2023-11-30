# Magnetic-Declination
QGIS plugin
```
begin                : 2015-04-08
copyright            : (C) 2015 by Aldo Scorza
email                : hacked dot crew at gmail dot com
```
```
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or   
(at your option) any later version.
```
Calculates the magnetic heading from a true geographic heading and vice versa.
Impress on map a Nautical Compass Rose (conformal) with obtained values.

A function in the Expression editor retrieve the center-point and crs of a given map within a Print Layout, and return a double representing the magnetic declination (many thanks to Matthew Cengia https://github.com/mattcen)


Use "geomag package"
by Christopher Weiss 
https://github.com/cmweiss/geomag
(Adapted from the geomagc software and World Magnetic Model of the NOAA Satellite and Information Service, National Geophysical Data Center
http://www.ngdc.noaa.gov/geomag/WMM/)

Model values by NCEI Geomagnetic Modeling Team and British Geological Survey. 2019. World Magnetic Model 2020. NOAA National Centers for Environmental Information.
doi: 10.25921/11v3-da71 (https://doi.org/10.25921/11v3-da71), 2020, [date accessed]

__author__ = 'Aldo Scorza'

__date__ = '2023-11-30'

__copyright__ = '(C) 2015, Aldo Scorza'

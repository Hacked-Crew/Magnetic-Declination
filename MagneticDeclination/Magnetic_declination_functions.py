# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MagneticDeclination
                              -------------------
        begin                : 2015-04-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Matt Cengia
        email                : mattcen@mattcen.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from datetime import date
from MagneticDeclination.geomag.geomag import GeoMag
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProject,
    QgsExpression,
)
from qgis.utils import qgsfunction

group_name = "Magnetic Declination"


def InitMagDecFunctions():
    QgsExpression.registerFunction(layout_map_mag_dec)


def UnloadMagDecFunctions():
    QgsExpression.unregisterFunction("layout_map_mag_dec")


@qgsfunction(args="auto", group=group_name)
def layout_map_mag_dec(layout_map, feature, parent):
    """Calculate the magnetic declination of a given point
    <h2>Arguments</h2>
    <ul>
      <li>layout_map -- A layout map to find the magnetic declination of</li>
    </ul>
    <h2>Example</h2>
    Within a print layout text area:

    <pre>
    format_number(abs(layout_map_mag_dec(item_variables('Map 1'))), 2)
    </pre>
    """
    my_point = layout_map['map_extent_center'].asPoint()
    crs = QgsCoordinateReferenceSystem(layout_map['map_crs'])
    altitude = 0
    my_date = date.today()
    project = QgsProject.instance()
    wgs84 = QgsCoordinateReferenceSystem('EPSG:4326')
    transformContext = project.transformContext()
    xform = QgsCoordinateTransform(crs, wgs84, transformContext)

    new_point = xform.transform(my_point)
    return GeoMag().GeoMag(new_point.x(), new_point.y(), h=altitude, time=my_date).dec

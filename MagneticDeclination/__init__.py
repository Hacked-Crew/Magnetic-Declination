# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MagneticDeclination
                              -------------------
        begin                : 2015-04-08
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Aldo Scorza
        email                : hacked dot crew at gmail dot com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
__author__ = 'Aldo Scorza'
__date__ = '2019-02-13'
__copyright__ = '(C) 2015, Aldo Scorza'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MagneticDeclination class from file MagneticDeclination.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Magnetic_declination import MagneticDeclination
    return MagneticDeclination(iface)

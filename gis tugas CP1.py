import mapnik
m = mapnik.Map(3000,2000)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

# line_symbolizer = mapnik.LineSymbolizer()
# line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),2)
# line_symbolizer.stroke_width = 10.0
# r.symbols.append(line_symbolizer)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# point_sym = mapnik.MarkersSymbolizer()
# point_sym.filename
# r.symbols.append(point_sym)

# basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Point]'), 'DejaVu Sans Bold',9,mapnik.Color('red'))
# basinsLabels.halo_fill = mapnik.Color('yellow')
# basinsLabels.halo_radius = 2
# r.symbols.append(basinsLabels)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# r.symbols.append(point_sym)
# s.rules.append(r)


s.rules.append(r)
m.append_style('yusuf1',s)
ds = mapnik.Shapefile(file="D:\cp1-gis\INDONESIA_PROP.shp")
layer = mapnik.Layer('peta')
layer.datasource = ds
layer.styles.append('yusuf1')
m.layers.append(layer)

# s = mapnik.Style()
# r = mapnik.Rule()

# line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
# r.symbols.append(line_symbolizer)
# s.rules.append(r)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# point_sym = mapnik.MarkersSymbolizer()
# r.symbols.append(point_sym)
# s.rules.append(r)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[point]'), 'DejaVu Sans Bold',3,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

s.rules.append(r)
m.append_style('yusuf2',s)
ds = mapnik.Shapefile(file="D:\cp1-gis\cuks.shp")
layer = mapnik.Layer('peta')
layer.datasource = ds
layer.styles.append('yusuf2')
m.layers.append(layer)

#2
#basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[wisata]'), 'DejaVu Sans Bold',3,mapnik.Color('red'))
##basinsLabels.halo_fill = mapnik.Color('blue')
#basinsLabels.halo_radius = 1
#r.symbols.append(basinsLabels)

#r = mapnik.Rule()

#ds = mapnik.Shapefile(file="D:\GIS tugas\wisata baru.shp")
#layer = mapnik.Layer('peta')
#layer.datasource = ds
#layer.styles.append('yusuf3')
#m.layers.append(layer)
m.append_style('yusuf',s)
POSTGIS_TABLE =dict(
    host='localhost',
    port=5432,
    user='postgres',
    password="1",
    dbname='yusuf',

        table='(select ST_Buffer(ST_Centroid(geom),1) as geom,point from yusufgis)as gis',
)
ds = mapnik.PostGIS(**POSTGIS_TABLE)
layer = mapnik.Layer('peta')
layer.datasource = ds
layer.styles.append('yusuf')
m.layers.append(layer)





m.zoom_all()
mapnik.render_to_file(m,'peta.tiff','tiff')
print "rendered image to 'peta.tiff"

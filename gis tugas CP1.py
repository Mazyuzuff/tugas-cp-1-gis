import mapnik

m = mapnik.Map(2000,1000)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

s.rules.append(r)
m.append_style('yusuf1',s)
ds = mapnik.Shapefile(file="D:\cp1-gis\INDONESIA_PROP.shp")
layer = mapnik.Layer('peta')
layer.datasource = ds
layer.styles.append('yusuf1')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[point]'), 'DejaVu Sans Bold',3,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
point_sym.opacity = 0.5
point_sym.file = ()
r.symbols.append(point_sym)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
point = mapnik.PointSymbolizer()
r.symbols.append(point)
s.rules.append(r)

m.append_style('yusuf2',s)
POSTGIS_TABLE = dict(
	host='localhost',
	port=5432,
	user='postgres',
	password="1",
	dbname='yusuf',

	table='(select ST_Buffer(ST_Centroid(geom),1) as geom, point from yusufgis) as coba',
)
ds = mapnik.PostGIS(**POSTGIS_TABLE)
layer = mapnik.Layer('peta')
layer.datasource = ds
layer.styles.append('yusuf2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'peta.pdf','pdf')
print "rendered image to 'peta.pdf"

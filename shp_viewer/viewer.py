import shapefile
import xlrd
import pdb

sf = shapefile.Reader("./Manzanas/Manzanas.shp")
wb = xlrd.open_workbook("./plot_manzanas.xls")

lst = wb.sheet_names()


for i in lst:
	sh = wb.sheet_by_name(i)
	w = shapefile.Writer(shapefile.POINT)
	w.field("ID")
	for rownum in range(sh.nrows):
		RowList = sh.row_values(rownum)
		x = RowList[2]
        y = RowList[1]
        z = RowList[3]
        w.point(x,y,z)
        w.record(ID)
    w.save(str(i))


"""
shapes = sf.shapes()
#pdb.set_trace()

# Calculate x and y length
for s in range(0,len(shapes)):
	x=0
	y=0
	for cd in range(0,len(shapes[s].points)):
		x = x + shapes[s].points[cd][0] #
		y = y + shapes[s].points[cd][1]
		print x, y


"""
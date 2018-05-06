from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(plot_width=500, plot_height=500)
circlesx,circlesy = [1, 2, 3, 4, 5,6,8], [7,2,1,4,8,3,6,7]
edges = [(1,3),(1,5),(3,2),(4,5),(6,3),(6,4),(0,5),(0,6),(0,2)]
for (i,f) in edges:
	linex,liney= [circlesx[i]],[circlesy[i]]
	linex.append(circlesx[f])
	liney.append(circlesy[f])
	line = p.line(linex, liney, line_width=2)

# add a circle renderer with a size, color, and alpha
p.circle(circlesx,circlesy, size=20, color="navy", alpha=0.5)

# show the results
show(p)

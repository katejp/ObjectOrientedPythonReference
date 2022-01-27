def main():
	height_rectangle_1, width_rectangle_1 = getRectangle1HeightWidth()
	surface_area_Rec1 = getSurfaceAreaRectangle1(height_rectangle_1, width_rectangle_1)
	height_rectangle_2, width_rectangle_2 = getRectangle2HeightWidth()
	surface_area_Rec2 = getSurfaceAreaRectangle2(height_rectangle_2, width_rectangle_2)
	compareSurfaceAreas(surface_area_Rec1, surface_area_Rec2)
	

def getRectangle1HeightWidth():
	rec_1_height = int(input("What is the height in inches of Rectangle 1?   "))
	rec_1_width = int(input("What is the width in inches of Rectangle 1?   "))
	return rec_1_height, rec_1_width

def getSurfaceAreaRectangle1(height, width):
	surface_area = height * width
	print("Surface Area Rectangle 1:   ", surface_area)
	return surface_area

def getRectangle2HeightWidth():
	rec_2_height = int(input("What is the height in inches of Rectangle 2?   "))
	rec_2_width = int(input("What is the width in inches of Rectangle 2?   "))
	return rec_2_height, rec_2_width

def getSurfaceAreaRectangle2(height, width):
	surface_area = height * width
	print("Surface Area Rectangle 2:   ", surface_area)
	return surface_area

def compareSurfaceAreas(surface1, surface2):
	if surface1 == surface2:
		print("The surface areas of Rectangle 1 and 2 are equal.")
	elif surface1 < surface2:
		print("The surface area of Rectangle 1 is less than the surface area of Rectangle 2.")
	else:
		print("The surface area of Rectangle 1 is greater than the surface area of Rectangle 2.")


main()
	

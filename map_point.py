from PIL import Image, ImageDraw, ImageFont
import csv

arrowsize = (25, 95)
offset = {'1':(1400,1747), '2':(1400, 399), '3':(771, 203), '4':(775, 1749), \
          '5':(191, 1988), '6':(191, 409), '7':(108, 306)}

arrowImage = Image.open("indicator.png")
map1FImage = Image.open("1층전도.png")
map2FImage = Image.open("2층전도.png")

floor = {'1':map1FImage, '2':map1FImage, '3':map1FImage, '4':map1FImage, \
         '5':map1FImage, '6':map1FImage, '7':map2FImage}

def indicate():
    csvfile = open("horizontal.csv", "r")
    csvreader = csv.reader(csvfile)
    #textBoard = Image.new("RGB", (200,200), (255,255,255))

    for a_line in csvreader:
        # room_num, rownum, colnum, X, Y -> a_line[0,4]        
        
        mapImage = floor[a_line[0]].copy()
        pos = offset[a_line[0]]
        pixX = pos[0] + int(a_line[3]) - arrowsize[0]
        pixY = pos[1] + int(a_line[4]) - arrowsize[1]

        #textClone = textBoard.copy()

        #indexDraw = ImageDraw.Draw(textClone)
        font = ImageFont.truetype("arial.ttf", 50)

        #indexDraw.text((0,0), "Hello World!", (255, 255, 255), font = font)

        #mapImage.paste(textClone, (0,0))
        mapImage.paste(arrowImage, (pixX, pixY), mask = arrowImage)
        mapImage.save("{0}-{1}{2}.png".format(a_line[0], a_line[1], a_line[2]), "PNG")
        

    csvfile.close()
    

if __name__ == "__main__":
    indicate()

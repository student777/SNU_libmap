from PIL import Image
import csv

canvasXY = (600, 1600)
offsets = (0, 0)
bookImageSize = 20

refroom_num = 7

def main():
    f = open("ref{0}_idx.txt".format(refroom_num), "w")
    canvas = Image.new("RGBA", canvasXY, "White")
    bookImage = Image.open("A_shelf.png")
    bigBookImage = Image.open("A_big_shelf.png")
    nullImage = Image.open("A_null_shelf.png")

    csvfile = open("ref{0}.csv".format(refroom_num), "r")
    csvreader = csv.reader(csvfile)

    for idx_row, row in enumerate(csvreader):
        if idx_row % 2 == 1: continue

        angle = 0 if idx_row % 4 == 0 else 180

        for idx_col, col in enumerate(row):
            pixX = offsets[0] + (bookImageSize) * (idx_col)
            #pixX += 50 if idx_col > 9 else 0
            #pixX += 50 if idx_col > 11 else 0
            #pixX += 50 if idx_col > 6 else 0
            
            pixY = offsets[1] + int((bookImageSize/2)) * int(idx_row / 2)
            pixY += int(idx_row / 4) * 15
            #pixY += 50 if idx_row > 55 else 0
            #pixY += 100 if idx_row > 31 else 0

            if col == "":
                continue
            elif (col == "-") or (col == "/"):
                canvas.paste(nullImage.rotate(angle), (pixX, pixY))
            elif col.startswith("대"):
                print(refroom_num, idx_row/4+1, chr(idx_col+65), pixX, pixY, sep='\t', end='\n', file=f)
                canvas.paste(bigBookImage.rotate(angle), (pixX, pixY))
            else:
                print(refroom_num, idx_row/4+1, chr(idx_col+65), pixX, pixY, sep='\t', end='\n', file=f)
                canvas.paste(bookImage.rotate(angle), (pixX, pixY))

    csvfile.close()
    f.close()
    
    canvas.save("{0}자료실.png".format(refroom_num), "PNG")

if __name__ == "__main__":
    main()

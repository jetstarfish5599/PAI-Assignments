#Q4 Image Transformation

#sample 2x3 image
originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]

#image class
class Image:
    def __init__(self, pixels):
        self.pixels = pixels

    #apply any transformation func
    def applytransformation(self, transformationFunc):
        self.pixels = transformationFunc(self.pixels)

    #make deep copy (manual)
    def getcopy(self):
        copied = []
        for row in self.pixels:
            newRow = [val for val in row]
            copied.append(newRow)
        return Image(copied)


#flip horizontal
def fliphorizontal(pixels):
    return [row[::-1] for row in pixels]

#adjust brightness
def adjustbrightness(pixels, amount):
    return [[val + amount for val in row] for row in pixels]

#rotate 90 deg
def rotateninetydegrees(pixels):
    rows = len(pixels)
    cols = len(pixels[0])
    rotated = [[pixels[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]
    return rotated


#augmentation pipeline
class AugmentationPipeline:
    def __init__(self):
        self.steps = []

    #add step
    def addstep(self, transformFunc):
        self.steps.append(transformFunc)

    #apply all steps
    def processimage(self, originalImage):
        imgCopy = originalImage.getcopy()
        for func in self.steps:
            imgCopy.applytransformation(func)
        return imgCopy


#main
img = Image(originalPixels)
pipeline = AugmentationPipeline()

#add stepsfor brightness
pipeline.addstep(fliphorizontal)
pipeline.addstep(lambda p: adjustbrightness(p, 100))
pipeline.addstep(rotateninetydegrees)

#process image
result = pipeline.processimage(img)

#output
print("original image pixels:")
for row in originalPixels:
    print(row)

print("\ntransformed image pixels:")
for row in result.pixels:
    print(row)

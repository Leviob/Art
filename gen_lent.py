from PIL import Image

im1 = Image.open('face1.png')
im2 = Image.open('face2.png')

# Resize images to the same size
maxsize = (1024, 1024)
im1.thumbnail(maxsize, Image.ANTIALIAS)
im2.thumbnail(maxsize, Image.ANTIALIAS)

number_of_slices = 70

width = im1.size[0]
height = im1.size[1]
slice_width = (im1.size[0]) // number_of_slices 
slice_start = 0
slice_end = slice_width

# Copy and pastes slices from im1 to im2
while slice_start < width:
    if slice_end >= width:
        slice_end = width
    box = (slice_start, 0, slice_end, height)
    region = im1.crop(box)
    im2.paste(region, box)
    slice_start += (2*slice_width)
    slice_end += (2*slice_width)

im2.save('result.png')
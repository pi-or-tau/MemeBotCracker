from PIL import Image
import math
import random

random.seed()

dim = 8
color_offset = 5

class hasher:
    def __init__(self, image):
        self.image = image
        self.pix = self.image.load()
        self.width = self.image.size[0]
        self.height = self.image.size[1]


    def check_hash(self, hash1, hash2):
        if hash1 == hash2:
            return True
        else:
            return False

    def hash(self):
        im_resized = self.image.resize((dim,dim))
        im_grey = im_resized.convert(mode="L")
        pix = im_grey.load()

        total = 0
        for ii in range(dim):
            for jj in range(dim):
                total += pix[ii,jj]
        average = total / (dim*dim)

        hsh = ''
        for ii in range(dim):
            for jj in range(dim):
                if pix[ii,jj] > average:
                    hsh += '1'
                else:
                    hsh += '0'
        return hsh

    def random_pixel(self):
        #deprecated
        width_random = random.randrange(self.width)
        height_random = random.randrange(self.height)
        current = self.pix[width_random,height_random]
        self.pix[width_random,height_random] = (current[0] + color_offset, current[1] + color_offset, current[2] + color_offset)

    def random_block(self):
        random_block_w_end = random.randrange(1, self.width)
        random_block_w_start = random.randrange(random_block_w_end)
        random_block_h_end = random.randrange(1, self.height)
        random_block_h_start = random.randrange(random_block_h_end)
        for ii in range(random_block_w_start, random_block_w_end):
            for jj in range(random_block_h_start, random_block_h_end):
                current = self.pix[ii,jj]
                self.pix[ii,jj] = (current[0] + color_offset, current[1] + color_offset, current[2] + color_offset)
                
    def image_show(self):
        self.image.show()
    
    def image_save(self, filename):
        self.image.save(filename)

filename = input('What is the input file name w/ extension: ')
im = Image.open(filename)
a = hasher(im)
orig = a.hash()
a.random_block()
new = a.hash()

ii = 0
#while a.check_hash(orig, new):
while ii <= 10:
    a.random_block()
    new = a.hash()
    ii += 1
    print(ii)

a.image_save('edit-'+filename)
a.image_show()

if not a.check_hash(orig, a.hash()):
    print('Success!')
else:
    print('Failure!')
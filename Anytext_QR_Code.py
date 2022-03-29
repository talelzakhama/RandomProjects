import random
import qrcode 

def image_qr(URL):
	img = qrcode.make(URL)
	img.save(filename + '.png')


def run():
	characters = input ('Input any URL here:')
	print(f'Your new URL is: {characters}')
	image_qr (characters)
	print ('The URL was saved as a QR Code image in Downloads')

if __name__ == '__main__':
	run()

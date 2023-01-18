import random
import qrcode 

def generate_passwrod(n_charcater):
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers = '1234567890345678901234567890'
	symbols = '!"#$%&/()={}[]'
	all_characters = lower+upper+numbers+symbols
	password = ''.join(random.sample(all_characters,n_charcater))
	return password

def image_qr(password):
	filename = input('Digit name password: ')
	img = qrcode.make(password)
	img.save(filename + '.png')


def run():
	charcters = int(input ('Digit number of characters:'))
	password = generate_passwrod(charcters)
	print(f'Your new password is: {password}')
	image_qr (password)
	print ('The password was saved as a QR Code image')

if __name__ == '__main__':
	run()

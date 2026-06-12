# importing the qr code lib. which will help us to generate the qr code
import qrcode

# taking UPI iD as a input
upi_id = input("Enter your upi_id = ")

# formate of payment url 
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# pa = upi id where we will pay
# pn = recipent name
# am = amount
# cu = currency
# tn = message


# defining the payment url based on the upi id And the payment app
# you can modify these urls based on the payments apps you want to support


phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"


# create a qr code each payment app
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)


# saving this QR code to image file (optionals)
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')


# displayying the qr code using the pillow lib. (pip install pillow)
phonepay_qr.show()
paytm_qr.show()
googlepay_qr.show()
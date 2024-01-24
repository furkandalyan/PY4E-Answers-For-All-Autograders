text = "X-DSPAM-Confidence:    0.8475"
sira=text.find("0")
sayi=text[sira:]
sayi=float(sayi)
print(sayi)

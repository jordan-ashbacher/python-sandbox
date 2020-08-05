text = "X-DSPAM-Confidence:    0.8475";
x = text.find("0")
y = text.find("5")
s = slice(23, 29)
print(float(text[s]))

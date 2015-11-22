import requests

for x in range(0, 500):
	r = requests.post("https://docs.google.com/forms/d/1GENlgA2_yRpxZU6CqG6nz_0DQ4PYz2-sRplnzBFmjDg/formResponse", data = {
		#"entry.1178235425":"1st",
		"entry.1936424317":"1rs",
		"entry.740234507":"1st",
		"draftResponse":"%5B%2C%2C%221872098851085172076%22%5D%0D%0A",
		"fbzx":"1872098851085172076",
		"pageHistory":"0",
		"fvv":"0"
		})
	print(x)

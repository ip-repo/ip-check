
import argparse
import requests
import PySimpleGUI as PSG


def get_ip(url: str) -> str:
	"""
	this fucntion get the url to retrive the ip from and request for it.
	"""
	result = ""
	try:
		result = requests.get(url=url)
		result.raise_for_status()
		return True, result.text.rstrip()
		
	except requests.exceptions.HTTPError as errhttp:
		result = errhttp		
	except requests.exceptions.ConnectionError as errce:
		result = errce
	except requests.exceptions.Timeout as errtimeout:
		result = errtimeout		
	except requests.exceptions.RequestException as errgeneral:
		result = errgeneral
	return False, result



def show_gui() -> None:
	"""
	this function open a gui that allow user to get and copy his public address.
	"""
	layout = [
	[PSG.Text(text="public ipv4", key="-TEXT-", size=(35,1)),
	PSG.Button("get", key="-BUTTON-", tooltip="get ipv4."),
	PSG.Button("copy",key="-COPY-", disabled=True)
	],
	  
	[PSG.Text(text="public ipv6", key="-TEXT1-",size=(35,1)),
	PSG.Button("get", key="-BUTTON1-",tooltip="get ipv6."),
	PSG.Button("copy",key="-COPY1-", disabled=True)
	]]
	
	PSG.theme("DarkAmber")
	window = PSG.Window(title="Public Ip", layout=layout,icon="assets/app_icon.png")
	
	while True:
		events, values = window.read()
		if events == PSG.WIN_CLOSED:
			break
		if events == "-BUTTON-":
			result,ipv4 = get_ip("https://ipv4.icanhazip.com/")		
			if result == True:
				window["-TEXT-"].update(ipv4)
				window["-COPY-"].update(disabled=False)
			else:
		
				window["-TEXT-"].update("something went wrong.")
				window["-COPY-"].update(disabled=True)
		if events == "-BUTTON1-":
			result, ipv6 = get_ip("https://ipv6.icanhazip.com/")
			if result == True:
				window["-TEXT1-"].update(ipv6)
				window["-COPY1-"].update(disabled=False)
			else:
	
				window["-TEXT1-"].update("something went wrong.")
				window["-COPY1-"].update(disabled=True)
		if events == "-COPY-":
			PSG.clipboard_set(window["-TEXT-"].get())
		if events == "-COPY1-":
			PSG.clipboard_set(window["-TEXT1-"].get())		
	window.close()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog="get public ip",
		description="This tool use https://icanhazip.com/ to get user public ip address.\
		The user can choose the type of ip address he want and also to copy  it.")
	
	parser.add_argument("-1", "--ip4", action="store_true", help="get ipv4")
	parser.add_argument("-2", "--ip6", action="store_true", help="get ipv6")
	parser.add_argument("-3", "--both", action="store_true" ,help="get ipv4 and ipv6")
	parser.add_argument("-4", "--gui", action="store_true", help="launch gui")
	parser.add_argument("-c", "--copy", action="store_true", help="copy result")

	args = parser.parse_args()

	if args.ip4 == False and args.ip6 == False and args.both == False and args.gui == False: 
		args.ip4 = True 
	ipv4, ipv6 = "", ""
	if args.ip4 == True:
		result, ipv4 = get_ip(url="https://ipv4.icanhazip.com/")
		if result:
			print(ipv4)
			if args.copy:
				PSG.clipboard_set(ipv4)
		else:
			ipv4="something went wrong."

	if args.ip6:
		result, ipv6 = get_ip(url="https://ipv6.icanhazip.com/")
		if result:
			print(ipv6)
		else:
			ipv6="something went wrong."
		if args.copy:
				PSG.clipboard_set(ipv6)

	if args.both:
		result_v4, ipv4 = get_ip(url="https://ipv4.icanhazip.com/")
		result_v6, ipv6 = get_ip(url="https://ipv6.icanhazip.com/")

		if result_v4 and result_v6:
			print(ipv4 + " , " + ipv6)
		else:
			print("something went wrong.")
		if args.copy:
				PSG.clipboard_set(ipv4 + " , " + ipv6)
	
	if args.gui:
		show_gui()



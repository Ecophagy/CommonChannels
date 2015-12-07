__module_name__ = "Channels in Common" 
__module_version__ = "1.0.1" 
__module_description__ = "Upon using the command /COMMON, tells you what channels you have in common with the specified user."

print ("\0035",__module_name__, __module_version__,"has been loaded\003")

import hexchat 
import os 
import re

def on_common(word, word_eol, userdata):
	if len(word) < 2:
		print ("Second arg must be a nick")
	else :
		target = word[1]
		common_channels = list();
		for chan in hexchat.get_list('channels'):
			context = hexchat.find_context(None, chan.channel)
			for user in context.get_list('users'):
				if(user.nick == target):
					common_channels.append(chan.channel)
			
		hexchat.prnt("Channels in common with " + target + ":")
		for chan in common_channels:
			hexchat.prnt(chan + " ")
			
	return hexchat.EAT_ALL
	
hexchat.hook_command("COMMON", on_common, help="/COMMON <nick> tells you all channels you have in common with <nick>")
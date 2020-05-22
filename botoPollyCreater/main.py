#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
boto sample code.
AWS Polly Text-to-speech file creation test
main function
"""

import sys
import boto3
import botocore
import contextlib


AWS_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxx'
AWS_SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
REGION_NAME = 'ap-northeast-1'



# -----------------------------------------------------------------------------
def creat_func(inString):
	"""
	create mp3 file
	"""

	polly = boto3.client("polly", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)

	try:
		response = polly.synthesize_speech(Text=inString, OutputFormat="mp3", VoiceId="Takumi")
	except (BotoCoreError, ClientError) as error:
		print(error)
		return
	if "AudioStream" in response:
		with contextlib.closing(response["AudioStream"]) as stream:
			output = "speech.mp3"
			try:
				with open(output, "wb") as file:
					file.write(stream.read())
			except IOError as error:
				print(error)
				return
			print("create OK>>" + output)
	else:
		print("Could not stream audio")
		return

	return








# -----------------------------------------------------------------------------
def main():
	argvLen = len(sys.argv)
	if(argvLen != 2):
		print("[ERROR] please input speech string")
		sys.exit(0)

	creat_func(sys.argv[1])

	return

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse

import os

"""
404 and 500 and etc. will be redirected to the url one up to the current url. 
This will keep redirecting until you hit a real page that doesn't return an error.
"""
def page_not_found_custom(request):
	new_redirect_url = ''
	current_url = request.get_full_path()
	if current_url[0] != '/':
		# Add forward slash at the front if missing. This is a failsafe.
		current_url = '/' + current_url
	if current_url[-1] != '/':
		# Append forward slash if missing. Useful if APPEND_SLASH is set to False. 
		current_url += '/'
	if current_url == '/':
		# if current url where 404 encountered is root/index page then handle case.
		new_redirect_url = '/#page_not_found'
	else:
		new_redirect_url = os.path.abspath(os.path.join(os.path.dirname(current_url), '..', ''))
	return redirect(new_redirect_url)
	
def page_error_found_custom(request):
	new_redirect_url = ''
	current_url = request.get_full_path()
	if current_url[0] != '/':
		# Add forward slash at the front if missing. This is a failsafe.
		current_url = '/' + current_url
	if current_url[-1] != '/':
		# Append forward slash if missing. Useful if APPEND_SLASH is set to False. 
		current_url += '/'
	if current_url == '/':
		# if current url where 404 encountered is root/index page then handle case.
		new_redirect_url = '/#page_not_found'
	else:
		new_redirect_url = os.path.abspath(os.path.join(os.path.dirname(current_url), '..', ''))
	return redirect(new_redirect_url)

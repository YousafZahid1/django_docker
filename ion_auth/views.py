from django.shortcuts import render, redirect
# Using standard requests instead of requests_oauthlib to match previous steps
import requests
import json
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
# Assuming your IonAuthBackend is in blog.auth
from blog.auth import IonAuthBackend
from django.conf import settings
from django.contrib import messages
from django.views.generic import View
import logging

logger = logging.getLogger(__name__)

# Ion OAuth Views based on friend's setup

# This view initiates the OAuth flow
class IonLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # Redirect to blog list after login if accessed directly
            return redirect('post_list')

        # Redirect to Ion authorization endpoint
        redirect_uri = 'http://localhost:8000/oauth/redirect' # Corrected redirect URI
        authorization_url = (
            'https://ion.tjhsst.edu/oauth/authorize/' +
            '?client_id=' + settings.SOCIAL_AUTH_ION_KEY +
            '&response_type=code' +
            '&scope=read' +
            '&redirect_uri=' + redirect_uri
        )
        logger.debug(f"Redirecting to Ion authorization URL: {authorization_url}")
        return redirect(authorization_url)

# This view handles the redirect from Ion after authorization
class IonCallbackView(View):
    def get(self, request):
        logger.debug(f"Callback received with GET parameters: {request.GET}")
        code = request.GET.get('code')
        if not code:
            logger.error("No authorization code received in callback")
            messages.error(request, "Authorization code not received from Ion.")
            # Redirect to Ion login initiation if code is missing
            return redirect('oauth2')

        # Exchange authorization code for access token
        token_url = 'https://ion.tjhsst.edu/oauth/token/'
        redirect_uri = 'http://localhost:8000/oauth/redirect' # Ensure this is also correct
        payload = {
            'client_id': settings.SOCIAL_AUTH_ION_KEY,
            'client_secret': settings.SOCIAL_AUTH_ION_SECRET,
            'code': code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }

        try:
            logger.debug(f"Attempting to exchange code for token with payload: {payload}")
            response = requests.post(token_url, data=payload)
            logger.debug(f"Token response status: {response.status_code}")
            logger.debug(f"Token response content: {response.text}")
            response.raise_for_status() # Raise HTTPError for bad responses
            token_data = response.json()
            access_token = token_data.get('access_token')

            if not access_token:
                logger.error("No access token in response")
                messages.error(request, "Access token not received from Ion.")
                return redirect('oauth2')

            # Use access token to get user info from the correct endpoint
            user_info_url = 'https://ion.tjhsst.edu/api/profile'
            headers = {'Authorization': f'Bearer {access_token}'}
            logger.debug(f"Fetching user info with headers: {headers}")
            user_response = requests.get(user_info_url, headers=headers)
            logger.debug(f"User info response status: {user_response.status_code}")
            logger.debug(f"User info response content: {user_response.text}")
            user_response.raise_for_status()
            user_data = user_response.json()

            # Authenticate and login the user using your IonAuthBackend
            # The user_data structure from /api/profile seems compatible with IonAuthBackend
            user = IonAuthBackend().authenticate(request=request, username=user_data.get('ion_username'), **user_data)

            if user:
                login(request, user, backend='blog.auth.IonAuthBackend')
                messages.success(request, f"Logged in as {user_data.get('display_name', user.username)}!")
                return redirect('post_create') # Redirect to create post page after login
            else:
                logger.error("Failed to authenticate user with Ion data")
                messages.error(request, "Could not authenticate user with Ion data.")
                return redirect('oauth2')

        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {str(e)}")
            messages.error(request, f"Error communicating with Ion OAuth server: {e}")
            return redirect('oauth2')
        except json.JSONDecodeError:
            logger.error("Invalid JSON response from Ion")
            messages.error(request, "Invalid response from Ion OAuth server.")
            return redirect('oauth2')

# This view handles logout
class IonLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect('post_list') # Redirect to blog list after logout

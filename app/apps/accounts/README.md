<a href="http://www.djangoproject.com/" >
	<img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." style="float: right;" />
</a>

## 'accounts' App

Powered by django-allauth (http://www.intenct.nl/projects/django-allauth/) & includes a modified version of django-rest-auth (https://github.com/Tivix/django-rest-auth)

A basic app that deals with everything to do with front-end users include registration / activation / admin / user preferences.

- registration 
  - - deals with user registration & activation
- user details
  - - user preferences / accounts profiles / definition of accounts Model (User -- settings.AUTH_USER_MODEL)

# Built-in Django Admin?
The 'normal' django admin is for maintenance (super admin) only and will not be visible for users


# How to use

## Register with POST message
POST - /accounts/registration/    
{
"username": "james.tarball",
"email": "danvir.guram@googlemail.com",
"password1": "mirage27",
"password2": "mirage27"
}

## Receive key
HTTP 201 Created
Allow: POST, OPTIONS, HEAD
Content-Type: application/json
Vary: Accept

{
    "key": "d66914f69aee700c42e50317c2079dad1b073a31"
}


# ToDo / Future Work
- Emails via mailchimp
- Increase Complexity / Thorough testing of validators in serializers
- More social login interaction 
- Improved Stats & Logs 


# ChangeLog
- '0.0.1' version -- initial release 31/10/15
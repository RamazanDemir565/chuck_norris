from django.core.mail import send_mail

if 'list' in request.POST:
    # do some listing...
elif 'do-something-else' in request.POST:
    # do something else
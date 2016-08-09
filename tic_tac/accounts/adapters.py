from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('blog:posts')

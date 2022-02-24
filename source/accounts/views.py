from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from accounts.forms import MyUserCreationForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


def login_view(request):
    if request.user.is_authenticated:
        return redirect('To_Do_list:index')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('To_Do_list:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('To_Do_list:index')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_object"
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            self.get_object().projects.all(),
            self.paginate_related_by,
            self.paginate_related_orphans,
        )

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()

        return super(UserProfileView, self).get_context_data(**kwargs)


class UserList(PermissionRequiredMixin, ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = "profile_list.html"
    permission_required = "accounts.view_profile"


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    form_profile_class = ProfileUpdateForm
    template_name = "update_profile.html"
    context_object_name = "user_object"

    def get_success_url(self):
        return reverse("accounts:user_profile", kwargs={"pk": self.kwargs.get("pk")})

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        profile_form = self.get_profile_form()

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        profile_form.save()
        return super().form_valid(form)

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileUpdateForm(**form_kwargs)

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)
import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from users.models import User, Location
from v2 import settings


# Create your views here.
class UserListView(ListView):
    model = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(self, *args, **kwargs)
        self.object_list = self.object_list.order_by("username")
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        result = []
        for user in page_obj:
            result.append({'id': user.id,
                           'username': user.username,
                           'first_name': user.first_name,
                           'last_name': user.last_name,
                           'role': user.role,
                           'age': user.age,
                           'ads_count': user.ads.count(),
                           'location': [str(u) for u in user.location.all()]
                           })
        return JsonResponse({'users': result, 'pages': page_obj.number, 'total': page_obj.paginator.count},
                            safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'role', 'location']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role'],
            password=data['password'],
            age=data['age']
        )
        for loc in data['location']:
            location, _ = Location.objects.get_or_create(name=loc)
            user.location.add(location)

        return JsonResponse(
            {'id': user.id,
             'username': user.username,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'role': user.role,
             'age': user.age,
             'location': [str(u) for u in user.location.all()]
             })


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({'id': user.id,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name,
                             'age': user.age,
                             'role': user.role,
                             'location': [str(u) for u in user.location.all()]
                             }, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'age', 'role', 'location']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        self.object.username = data['username'] if 'username' in data else self.object.username
        self.object.password = data['password'] if 'password' in data else self.object.password
        self.object.first_name = data['first_name'] if 'first_name' in data else self.object.first_name
        self.object.last_name = data['last_name'] if 'last_name' in data else self.object.last_name
        self.object.age = data['age'] if 'age' in data else self.object.age
        self.object.role = data['role'] if 'role' in data else self.object.role
        if 'location' in data:
            for loc in data['location']:
                location, _ = Location.objects.get_or_create(name=loc)
                self.object.location.add(location)
        self.object.save()
        return JsonResponse({'id': self.object.id, 'username': self.object.username}, safe=False,
                            json_dumps_params={'ensure_ascii': False})

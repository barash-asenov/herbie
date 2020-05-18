"""herbie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from herbieapp.controllers.dependency_containers import ControllerDependencyContainerView


admin.site.site_header = 'Herbie'
admin.site.site_title = 'Herbie'
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:business_entity>/save',
         ControllerDependencyContainerView.save_business_entity_controller_as_view
         ),
    path('api/<str:business_entity>/delete', ControllerDependencyContainerView.delete_business_entity_controller_as_view),
    path('api/schema-registry/<str:business_entity>/<str:version>',
         ControllerDependencyContainerView.schema_registry_controller_as_view
         ),
    path('api/schema-registry/<str:business_entity>/',
         ControllerDependencyContainerView.schema_registry_controller_as_view, {'version': ''}
         ),
    path('oauth/', include('social_django.urls', namespace='social')),
]

from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import SignUpView
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('add_stock/', views.StockController().add_stock, name='add_stock'),
    path('farm_detail/<str:symbol>/', views.StockController().stock_detail, name='stock_detail'),
    path('delete_farm/<str:symbol>/', views.StockController().delete_stock, name='delete_stock'),
    path('update_farm/<str:symbol>/<str:name>/<str:date>/', views.StockController().update_stock, name='update_stock'),

    path('create_report/', views.ReportController().create_report, name='create_report'),
    path('create_analysis/', views.AnalysisController().create_analysis, name='create_analysis'),
    path('create_farm/', views.FarmController().create_farm, name='create_farm'),
    path('create_field/', views.FieldController().create_field, name='create_field'),

    path('report_list/', views.ReportController().report_list, name='report_list'),
    path('analysis_list/', views.AnalysisController().analysis_list, name='analysis_list'),
    path('farm_list/', views.FarmController().farm_list, name='farm_list'),
    path('field_list/', views.FieldController().field_list, name='field_list'),

    path('report_detail/', views.ReportController().report_detail, name='farm_detail'),
    path('analysis_detail/', views.AnalysisController().analysis_detail, name='analysis_detail'),
    path('farm_detail/', views.FarmController().farm_detail, name='farm_detail'),
    path('field_detail/', views.FieldController().field_detail, name='field_detail'),

    path('update_report/', views.ReportController().update_report, name='update_report'),
    path('update_analysis/', views.AnalysisController().update_analysis, name='update_analysis'),
    path('update_farm/', views.FarmController().update_farm, name='update_farm'),
    path('update_field/', views.FieldController().update_field, name='update_field'),

    path('delete_report/', views.ReportController().delete_report, name='delete_report'),
    path('delete_analysis/', views.AnalysisController().delete_analysis, name='delete_analysis'),
    path('delete_farm/', views.FarmController().delete_farm, name='delete_farm'),
    path('delete_field/', views.FieldController().delete_field, name='delete_field'),
]
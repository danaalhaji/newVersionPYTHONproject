from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.method),
    path('login', views.login),
    path('userlogin', views.userlogin),
    
    path('signup', views.signup),
    path('newuserRegistration', views.newuserRegistration),
    
    path('logout', views.logout),
    path('admin', views.writePassword),
    path('confirmAdminPassword', views.confirmAdminPassword),
    path('adminDashboard', views.ShowadminDashboard),
    path('showallUsers', views.showallUsers),
    path('showallEmployees', views.showallEmployees),
    path('admin/menu', views.addMenu),
    path('addemployee', views.addemployee),
    path('deleteEmployee/<int:id>', views.deleteEmployee),
    path('editEmployee/<int:id>', views.editEmployee),
    path('edit/<int:id>', views.updateEmployeee),
    path('showEmployee/<int:id>', views.showEmployee),
     path('showReports', views.showReports),
    
    path('bookTable', views.bookTable),
    path('ordernow', views.ordernow),
    path('error', views.error),
    path('sendmessage/<int:id>', views.sendmessage),
    path('deletemessage/<int:id>', views.deletemessage),

    # path('ordernow', views.ordernow),
    path('ordernow/<int:id>', views.addToCart),
    path('ordernow/success', views.completeOrder),
    path('showallOrders', views.showallOrders),
    path('processTrue/<int:id>', views.processTrue),
    path('destroyOrder/<int:id>', views.destroyOrder),
    
    
    
    
    
]
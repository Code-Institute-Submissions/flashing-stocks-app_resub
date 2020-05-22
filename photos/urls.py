from django.urls import path
import photos.views

urlpatterns = [
    path('', photos.views.list_photos, name='list_photos'),
    path('add', photos.views.add_photo, name='add_photo'),
    path('<photo_id>', photos.views.view_photo, name='view_photo'),
    path('edit/<photo_id>', photos.views.edit_photo, name="edit_photo"),
    path('delete/<photo_id>', photos.views.delete_photo, name="delete_photo"),
    path('tags/add', photos.views.add_tags, name="add_tags"),
    path('category/add', photos.views.add_category, name="add_category")
    ]
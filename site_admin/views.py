from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from photos.models import Tag, Category
from photos.forms import TagForm, CategoryForm


def admin_homepage(request):
    return render(request, 'site_admin/index.template.html')


def add_tags(request):

    tags = Tag.objects.all()

    form = TagForm()

    if request.method == 'POST':

        tag_form = TagForm(request.POST)

        if tag_form.is_valid():
            tag = tag_form.save()
            messages.success(
                request, f"Tag [{tag.name}] added successful"
            )
        else:
            messages.error(
                request, f"Unable to add new Tag"
            )
            return render(request, 'site_admin/add_tags.template.html', {
                'tags': tags,
                'form': tag_form
            })

    return render(request, 'site_admin/add_tags.template.html', {
        'tags': tags,
        'form': form
    })


def edit_tag(request, tag_id):

    try:
        tag = Tag.objects.get(id=tag_id)
    except ObjectDoesNotExist:
        tag = None

    if tag:
        form = TagForm(instance=tag)

    if request.method == 'POST':
        tag_form = TagForm(request.POST, instance=tag)

        if tag_form.is_valid():
            saved_tag = tag_form.save()
            messages.success(request, f"Tag {saved_tag.name} has been updated")
            return redirect(reverse(add_tags))
        else:
            messages.error(request, f"Update failed.")
            return render(request, 'site_admin/edit_tag.template.html', {
                'form': tag_form
            })

    return render(request, 'site_admin/edit_tag.template.html', {
        'form': form
    })


def delete_tag(request, tag_id):

    try:
        tag = Tag.objects.get(id=tag_id)
    except ObjectDoesNotExist:
        tag = None

    if request.method == 'POST':
        tag.delete()
        return redirect(reverse(add_tags))

    return redirect(reverse(add_tags))


def add_category(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)

        if category_form.is_valid():
            category = category_form.save()
            messages.success(
                request, f"Category [{category.name}] added successful"
            )
        else:
            messages.error(
                request, f"Unable to add new category"
            )
            return render(request, 'site_admin/add_category.template.html', {
                'categories': categories,
                'form': category_form
            })

    form = CategoryForm()

    return render(request, 'site_admin/add_category.template.html', {
        'categories': categories,
        'form': form
    })


def edit_category(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        category = None

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            saved_category = form.save()
            messages.success(
                request,
                f"Category Name [{saved_category.name}] has been updated"
                )
            return redirect(reverse(add_category))
        else:
            messages.error(request, "Unable to update category name")
            return render(request, 'site_admin/edit_category.template.html', {
                'form': form
            })

    form = CategoryForm(instance=category)

    return render(request, 'site_admin/edit_category.template.html', {
        'form': form
    })


def delete_category(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        category = None

    if request.method == 'POST':
        messages.success(
            request,
            f"Category [{category.name}] has been deleted"
        )
        category.delete()
        return redirect(reverse(add_category))
    else:
        messages.error(request, f"Unable to delete category")
        return redirect(reverse(add_category))

    return redirect(reverse(add_category))

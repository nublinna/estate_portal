from django.shortcuts import render
from flats.models import Flat
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from flats.forms import FlatForm


def flats_list(request):
    all_flats = Flat.objects.filter(available=True)
    return render(request, 'flats_list.html', context={
        'all_flats': all_flats,
    })

def flat_detail(request, flat_id):
    # filter -> list()
    # flat_from_db = Flat.objects.filter(id=flat_id).first()

    flat_from_db = get_object_or_404(Flat, id=flat_id)
    return render(request, 'flat_detail.html', context={
        'flat': flat_from_db,
    })

@login_required
def flat_create(request):
    if not request.user.is_owner():
        return redirect("flats:flats_list")

    if request.method == "POST":
        form = FlatForm(request.POST, request.FILES)
        if form.is_valid():
            flat = form.save(commit=False)
            flat.owner = request.user
            flat.save()
            return redirect("flats:flat_detail", flat_id=flat.id)
        else:
            form = FlatForm()

        return render(request, "flat_create.html", context={"form": form})
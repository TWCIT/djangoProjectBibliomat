from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from polls.models import Title
from .models import Deposit
from .microcontroller import open_tray


def main(request):
    titles = Title.objects.all()
    # Sortowanie według tytułu
    titles = titles.order_by('title')
    # lub sortowanie według autora
    titles = titles.order_by('author')
    context = {'titles': titles}
    return render(request, 'machine/main.html', context)


def deposit_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('machine-main')

    deposits = Deposit.objects.filter(loan__customer__user=user)
    context = {'deposits': deposits}
    return render(request, 'machine/deposit_list.html', context)


def pick_up_deposit(request, deposit_id):
    deposit = get_object_or_404(Deposit, id=deposit_id)
    user = request.user
    if (not user.is_authenticated) or deposit.loan.customer.user != user:
        raise PermissionDenied

    open_tray(deposit.tray)

    deposit.delete()
    return render(request, 'machine/deposit_pickup.html')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from .models import Title,Copy,Loan

def test_app(request, title_id):

    return render(request, 'test.html')
def title_list(request):
    titles = Title.objects.all()
    # Sortowanie według tytułu
    titles = titles.order_by('title')
    # lub sortowanie według autora
    titles = titles.order_by('author')
    context = {'titles': titles}
    return render(request, 'title_list.html', context)
def title_detail(request, title_id):
    title = get_object_or_404(Title, pk=title_id)
    copies = Copy.objects.filter(title=title, is_available=True)
    context = {'title': title, 'copies': copies}
    return render(request, 'title_detail.html', context)
def loan_list(request, customer_id):
    loans = Loan.objects.filter(customer=customer_id)
    # Sortowanie według daty wypożyczenia
    loans = loans.order_by('loan_date')
    # lub sortowanie według daty zwrotu
    loans = loans.order_by('return_date')
    context = {'loans': loans}
    return render(request, 'loan_list.html', context)
def order_form(request, copy_id):
    copy = get_object_or_404(Copy, pk=copy_id)
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Pobieranie danych z formularza
            customer = form.cleaned_data['customer']
            pick_up_in_bibliomat = form.cleaned_data['pick_up_in_bibliomat']
            # Sprawdzenie, czy klient ma dostępny limit
            if customer.loan_limit > customer.loans.count():
                # Ustawienie egzemplarza jako niedostępnego
                copy.is_available = False
                copy.save()
                # Tworzenie nowego wypożyczenia
                loan = Loan.objects.create(copy=copy, customer=customer, pick_up_in_bibliomat=pick_up_in_bibliomat)
                context = {'loan': loan}
                return render(request, 'order_success.html', context)
            else:
                error = "Nie masz dostępnego limitu wypożyczeń"
                context = {'form': form, 'error': error}
                return render(request, 'order_form.html', context)
    else:
        form = OrderForm()
        context = {'form': form, 'copy': copy}
    return render(request, 'order_form.html', context)
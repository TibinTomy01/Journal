from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Transaction
from django.db.models import Sum
# Create your views here.

# def login(request):
#     return render(request, 'login.html')

@login_required
def account_CD(request):

    
    if request.method == 'POST':
        date = request.POST['date']
        description = request.POST['description']
        transaction_type = request.POST['transaction_type']
        amount = request.POST['amount']

        Transaction.objects.create(
            user=request.user,
            date=date,
            description=description,
            transaction_type=transaction_type,
            amount=amount
        )
    list=Transaction.objects.all()
    return render(request, 'account_CD.html',{ 'data':list})

# def entry(request):
#     data=Transaction.objects.all()
#     total_amount = Transaction.objects.aggregate(Sum('amount'))['amount__sum']
#     total_debit=sum(Transaction.amount for )
#     return render(request, 'entry.html', {'data': data})



def entry(request):
    transactions = Transaction.objects.all()

    # Calculate total debit and credit
    total_debit = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 0)
    total_credit = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 1)

    # Calculate current balance
    current_balance = total_credit - total_debit

    return render(request, 'entry.html', {
        'transactions': transactions,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'current_balance': current_balance,
    })

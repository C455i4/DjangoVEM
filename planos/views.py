from django.views import View
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import stripe
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .models import PlanosModel


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "sucess.html"

class CancelView(TemplateView):
    template_name = "cancel.html"


class PlanosView(TemplateView):
    template_name = 'planos.html'

    def get_context_data(self, **kwargs):
        plano = PlanosModel.objects.get(nome="Plano Borboleta")
        context = super(PlanosView, self).get_context_data(**kwargs)
        context.update({
            "plano": plano,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context



class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        plano_id = self.kwargs["pk"]
        plano = PlanosModel.objects.get(id=plano_id)
        print(plano)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {

                    'price_data':{
                        'currency': 'brl',
                        'unit_amount': plano.preco,
                        'product_data':{
                            'name': plano.nome,
                        },
                    },
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    #'price': '{{PRICE_ID}}',

                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/sucess/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
         
        return JsonResponse({
            'id': checkout_session.id
        })
    
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    print(payload)

    return HttpResponse(status = 200)
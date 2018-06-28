from django.conf.urls import url


from fxbot import views

app_name = "fxbot"

urlpatterns = [

    url(r'^index/$', views.IndexView.as_view(), name="index")
    # url(r'^crypto/wallet/$', views.WalletListView.as_view(), name="wallet-list"),
    # url(r'^crypto/wallet/create/$', views.WalletCreateView.as_view(), name="wallet-create"),
    # url(r'^crypto/wallet/send-money/$', views.WalletTransactionView.as_view(), name="send-money"),
    # url(r'^crypto/wallet/wallet-address/$', views.WalletAddressView.as_view(), name="wallet-address"),
    # url(r'^crypto/wallet/coinbase-gdax-transfer/$', views.WalletCoinbaseGDAXTransferView.as_view(), name="coinbase-gdax-transfer"),
    # url(r'^crypto/buy-sell/$', views.BuySellView.as_view(), name="buy-sell"),
    # url(r'^crypto/buy-sell/orders/$', views.BuySellOrderView.as_view(), name="buy-sell-order"),
    # url(r'^crypto/buy-sell/accounts/$', views.BuySellAccountsView.as_view(), name="buy-sell-accounts"),
    # url(r'^crypto/profile/$', views.ProfileView.as_view(), name="profile"),
    # url(r'^crypto/swap-crypto/$', views.SwapCryptoView.as_view(), name="swap-crypto"),

]




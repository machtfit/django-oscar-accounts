from oscar.core.loading import is_model_registered

from accounts import abstract_models


if not is_model_registered('accounts', 'AccountType'):
    class AccountType(abstract_models.AccountType):
        class Meta:
            app_label = "accounts"


if not is_model_registered('accounts', 'Account'):
    class Account(abstract_models.Account):
        class Meta:
            app_label = "accounts"


if not is_model_registered('accounts', 'Transfer'):
    class Transfer(abstract_models.Transfer):
        class Meta:
            app_label = "accounts"


if not is_model_registered('accounts', 'Transaction'):
    class Transaction(abstract_models.Transaction):
        class Meta:
            app_label = "accounts"


if not is_model_registered('accounts', 'IPAddressRecord'):
    class IPAddressRecord(abstract_models.IPAddressRecord):
        class Meta:
            app_label = "accounts"

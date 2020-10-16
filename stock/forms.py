from django.forms import ModelForm
from .models import Product
from django.utils.translation import gettext_lazy as _


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['prodNm', 'stckQty', 'brnd', 'cate']
        labels = {
            'prodNm': _('상품명'),
            'stckQty': _('상품수량'),
            'brnd': _('브랜드'),
            'cate': _('카테고리'),
        }
        help_texts = {
            'prodNm': _('상품명을 입력해주세요'),
            'stckQty': _('상품수량을 입력해주세요'),
            'brnd': _('브랜드를 입력해주세요'),
            'cate': _('카테고리를 입력해주세요'),
        }
        error_messages = {
            'prodNm': {
                'max_length': _('상품이름은 30자 이하로 입력해주세요.'),
            }
        }


class UpdateProductForm(ProductForm):
    class Meta:
        model = Product
        exclude = ['id']

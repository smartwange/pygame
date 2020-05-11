from django import forms
from apps.operations.models import UserFavorite


# 表单验证直接取模型里定义的即可，fields是字段范围 不写默认是所有都验证
class addFavForm(forms.ModelForm):
      class Meta:
          model=UserFavorite
          fields=['fav_id','fav_type']

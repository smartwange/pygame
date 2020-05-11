from django import forms
from apps.operations.models import UserAsk


# 表单验证直接取模型里定义的即可，fields是字段范围 不写默认是所有都验证
class addAskForm(forms.ModelForm):
      class Meta:
          model=UserAsk
          fields=['name','mobile','course_name']

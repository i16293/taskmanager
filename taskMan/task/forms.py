from django import forms
from .models import Project, ProjectToUsers

""" プロジェクト作成 """
class ProjectCreate(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'name', 'leader',
            'start_date', 'end_date',
            'details'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['leader'].widget.attrs['hidden'] = 'true'
        self.fields['start_date'].widget.input_type = "date"
        self.fields['end_date'].widget.input_type="date"


""" プロジェクト更新 """
class ProjectUpdate(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'name',
            'start_date', 'end_date',
            'details'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = "date"
        self.fields['end_date'].widget.input_type="date"


""" プロジェクト削除 """
class ProjectDelete(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'is_delete',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_delete'].widget.attrs['hidden'] = 'true'

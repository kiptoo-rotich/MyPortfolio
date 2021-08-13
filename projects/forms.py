class Technologies(forms.ModelForm):
    
    languages = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Project
        fields = '__all__'
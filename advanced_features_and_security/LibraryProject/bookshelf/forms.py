from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        label="Book Title",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    author = forms.CharField(
        max_length=200,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    published_date = forms.DateField(
        required=False,
        label="Published Date",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

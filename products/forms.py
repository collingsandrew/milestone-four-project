from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_title', 'review_text', 'rating']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Review Title',
            'review_text': 'Write your review here',
            'rating': 'Rating (0-5)',
        }

        # Set autofocus on the first field (review_title)
        self.fields['review_title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Set placeholders for all fields
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add CSS class to each field
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

            # Remove labels
            self.fields[field].label = False
            
            # add min and max attributes to the product review rating field
            self.fields['rating'].widget.attrs['min'] = 0
            self.fields['rating'].widget.attrs['max'] = 5

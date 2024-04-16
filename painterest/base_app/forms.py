from django import forms
#from .models import Image
from base_app.models import UsersDB
from django.contrib.auth.hashers import make_password, check_password

class ImageForm(forms.Form):
    title = forms.CharField(max_length = 100,  widget=forms.TextInput(attrs={'class': 'form-control'}))  
    description = forms.CharField(max_length = 255,  widget=forms.TextInput(attrs={'class': 'form-control'})) 
    upload_image = forms.ImageField()

 #   class Meta:
 #       model = Image
 #       fields = ['title','image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100) 
    password = forms.CharField(widget = forms.PasswordInput()) 

    def is_valid_login(self): 
        if self.is_valid():
            cleaned_data = super().clean()
            username = cleaned_data.get('username')
            #Je check si le mdp est trouvé dans la bdd
            dbuser = UsersDB.objects.filter(username = username)

            if (not dbuser): 
                raise forms.ValidationError("User not found, please retry ! ") 
            
            user = UsersDB.objects.get(username=username)
        
            if check_password(cleaned_data.get('password'), user.password):
                #Todo Connexion session
                return True
            else:
                raise forms.ValidationError("Password incorrect ! ") 
        return False
    
class RegisterForm(forms.Form): 
    username_register = forms.CharField(max_length = 100) 
    password = forms.CharField(widget = forms.PasswordInput()) 
    password2 = forms.CharField(widget = forms.PasswordInput()) 

    def is_valid_register(self): 
        if self.is_valid():
            cleaned_data = super().clean()
            username = cleaned_data.get('username_register')
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')

            #Je check si le mdp est trouvé dans la bdd
            dbuser = UsersDB.objects.filter(username = username)
    
            if dbuser: 
                raise forms.ValidationError("This name already exist") 

            print(password , " ", password2)
            if password != password2 : 
                raise forms.ValidationError("Password not matching") 

            UsersDB(username= username, password= make_password(password)).save()

            #Todo Connexion session
            return True
        return False
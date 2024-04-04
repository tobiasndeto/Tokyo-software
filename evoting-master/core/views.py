from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Voting


# Create your views here.
def show_base(request):
    if request.method == "POST":
        btn = request.POST.get('btn')
        if btn == "register":
            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if username and email and password:
                User = get_user_model()
                user, created = User.objects.get_or_create(username=username, email=email)
                if created:
                    user.set_password(password)
                    user.save()
                    request.session['username'] = username
                    return redirect('voting-page')
                else:
                    return render(request, 'base.html',
                                  {'error_message': 'User with this username or email already exists'})
        elif btn == "login":
            username = request.POST.get('name')
            password = request.POST.get('password')
            if username and password:  # Check if both username and password are provided
                User = get_user_model()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    request.session['username'] = username
                    return redirect('voting-page')
                else:
                    error_message = "Invalid username or password."
                    return render(request, 'base.html', {'error_message': error_message})
            else:
                error_message = "Please provide both username and password."
                return render(request, 'base.html', {'error_message': error_message})

    return render(request, 'base.html')


def show_voting_page(request):
    if request.method == "POST":
        btn = request.POST.get('btnvote')
        name = request.session['username']
        if btn == "president":
            voters_email = name
            politician_name = request.POST.get('name')
            politician_position = request.POST.get('position')

            new_vote = Voting()

            # Assign values to its attributes
            new_vote.voters_name = voters_email
            new_vote.politician_name = politician_name
            new_vote.politician_position = politician_position
            # Save the instance to the database
            new_vote.save()
            return redirect('results-page')
        elif btn == "vice_president":
            voters_email = name
            politician_name = request.POST.get('name')
            politician_position = request.POST.get('position')

            new_vote = Voting()

            # Assign values to its attributes
            new_vote.voters_name = voters_email
            new_vote.politician_name = politician_name
            new_vote.politician_position = politician_position
            # Save the instance to the database
            new_vote.save()
            return redirect('results-page')
        elif btn == "senator":
            voters_email = name
            politician_name = request.POST.get('name')
            politician_position = request.POST.get('position')

            new_vote = Voting()

            # Assign values to its attributes
            new_vote.voters_name = voters_email
            new_vote.politician_name = politician_name
            new_vote.politician_position = politician_position
            # Save the instance to the database
            new_vote.save()
            return redirect('results-page')

    return render(request, 'voting_page.html')


def show_results(request):
    voting_instances = Voting.objects.all()

    # Create a list to hold dictionaries representing each instance
    voting_list = []

    # Iterate over each instance and add its data to the list
    for instance in voting_instances:
        voting_dict = {
            'voters_name': instance.voters_name,
            'politician_name': instance.politician_name,
            'politician_position': instance.politician_position
        }
        voting_list.append(voting_dict)
    return render(request, 'results.html', {'appdata': voting_list})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import ToDo
from .forms import ToDoForm
from django.utils import timezone


@login_required
def

{% extends 'uname/login/profile.html' %}

{% load staticfiles %}

{% block title %}{{ user.username }}{% endblock %}

{% block body_block %}
        {% if user.is_authenticated %}
        <h1>{{ user.username }} welcome to your profile page</h1>
        <img src="{{ user.userprofile.profile_picture.url }}" width = "150" height = "150"  />
        <h2>{{ user.userprofile.first_name }}</h2>
        <h2>{{ user.userprofile.second_name }}</h2>
        <h2>{{ user.userprofile.user_country }}</h2>
        {% endif %}

{% endblock %}
# urls.py — Root URL routing. Maps incoming requests to views (or includes app-level urls.py).
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# ===============
# Former Shape
# ===============

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# ============================================================
# URL Routing — Design Choice: Prefix or No Prefix?
# ============================================================

# Two valid ways to include an app's URLs. Neither is "wrong" —
# it's an architectural decision based on how the project will grow.

# ------------------------------------------------------------
# Option 1 — No prefix (root-level routing)
# ------------------------------------------------------------

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Intention:
#   This project only has one app (core), so why make URLs longer?
#   Requests go directly to the app from the site root (/).

# Best for:
#   - Single‑app projects
#   - A simple blog or site where one app handles everything
#   - Quick prototypes / learning projects

# Full URLs with Option 1 (no prefix):
#   http://127.0.0.1:8000/           -> Home page
#   http://127.0.0.1:8000/about/     -> About page
#   http://127.0.0.1:8000/post/42/   -> Post ID: 42


# ------------------------------------------------------------
# Option 2 — Prefix per app (namespace routing)
# ------------------------------------------------------------

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('core/', include('core.urls')),
# ]

# Intention:
#   A defensive, scalable pattern. Later you might add a second app
#   (e.g. 'users' or 'payments'). Giving each app its own prefix
#   (/core/..., /users/...) prevents URL collisions from the start.

# Best for:
#   - Multi‑app projects
#   - Building a habit of scalable, namespace‑clean structure
#   - Production projects where apps grow independently

# Full URLs with Option 2 (prefix):
#   http://127.0.0.1:8000/core/           -> Home page
#   http://127.0.0.1:8000/core/about/     -> About page
#   http://127.0.0.1:8000/core/post/42/   -> Post ID: 42

# ------------------------------------------------------------
# What changes if you use a prefix?
# ------------------------------------------------------------
# With path('core/', include('core.urls')), the URLs become:
#   /            -> /core/
#   /about/      -> /core/about/
#   /post/42/    -> /core/post/42/

# The views and logic stay exactly the same — only the address
# the user sees changes.

# ------------------------------------------------------------
# Which one is right for this project?
# ------------------------------------------------------------
# django_intro is a practice project that will always stay single‑app.
# So Option 1 (no prefix) is fully justified and clean.

# For Week 12 (the real project with multiple apps),
# Option 2 (prefix per app) will be the better choice.
# ============================================================
from django.shortcuts import render


def index(req, *args, **kwargs):
    return render(req, 'index.html')


def robots(req, *args, **kwargs):
    return render(req, 'robots.txt', content_type='text/plain')


def manifest(req, *args, **kwargs):
    return render(req, 'manifest.json', content_type='application/json')


def asset_manifest(req, *args, **kwargs):
    return render(req, 'asset-manifest.json', content_type='application/json')
